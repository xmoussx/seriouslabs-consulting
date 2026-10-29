"""Le tableau du marché français, tiré des données ouvertes de l'ANJ.

Télécharge le fichier publié sur data.gouv.fr, en extrait les séries utiles et
écrit deux choses :
  - assets/data/marche.json, lu par la page pour changer d'année ;
  - le graphique SVG, inscrit en dur entre les balises <!-- marche:graphique -->
    de index.html et fr/index.html, pour qu'il s'affiche sans script.

Usage, depuis la racine du dépôt :
    python3 outils/marche.py
"""
import csv, io, json, re, urllib.request
from pathlib import Path

SOURCE = ("https://static.data.gouv.fr/resources/donnees-sur-le-marche-des-jeux-en-ligne-"
          "paris-sportifs-hippiques-et-poker-de-2010-a-2024/20251208-095023/"
          "open-data-donnees-marche-des-jah-en-ligne-2024.csv")
PAGE = ("https://www.data.gouv.fr/datasets/donnees-sur-le-marche-des-jeux-en-ligne-"
        "paris-sportifs-hippiques-et-poker-de-2010-a-2024/")
RACINE = Path(__file__).resolve().parent.parent

# Libellé de la ligne dans le fichier de l'ANJ -> clé du JSON.
LIGNES = {
    "Nombre d’opérateurs": "operateurs",
    "Nombre d’agréments": "agrements",
    "Nombre de comptes joueurs actifs total (en milliers)": "comptes",
    "Nombre de joueurs uniques": "uniques",
    "Mises paris sportifs (en M€)": "mises_ps",
    "Mises paris hippiques (en M€)": "mises_ph",
    "PBJ paris sportifs (en M€)": "pbj_ps",
    "PBJ paris hippiques (en M€)": "pbj_ph",
    "PBJ poker (en M€)": "pbj_po",
}

# L'ordre des segments dans la pile, de bas en haut. Les couleurs vivent dans
# la feuille de style (classes s-ps, s-po, s-ph), validées pour le daltonisme
# sur le fond acier.
SEGMENTS = ["pbj_ps", "pbj_po", "pbj_ph"]
PLAFOND = 3000          # M€ : au-dessus du plus haut total (2 592 en 2024)
GRADUATIONS = (1000, 2000, 3000)


def lire():
    brut = urllib.request.urlopen(SOURCE, timeout=60).read().decode("cp1252")
    rangs = list(csv.reader(io.StringIO(brut), delimiter=";"))
    annees = [int(re.search(r"(\d{4})$", c).group(1)) for c in rangs[0][1:]]
    series = {}
    for r in rangs[1:]:
        if r and r[0] in LIGNES:
            series[LIGNES[r[0]]] = [int(v) if v.strip() else None for v in r[1:]]
    return annees, series


def graphique(annees, s, lang):
    """Barres empilées du produit brut des jeux, une par année.

    Le SVG ne porte que les barres et les filets : il s'étire à la hauteur que
    la feuille de style lui donne (preserveAspectRatio="none"). Les années et
    les graduations sont en HTML, pour rester lisibles à toutes les largeurs.
    """
    larg, haut, pas, barre = 600, 220, 40, 28
    echelle = haut / PLAFOND
    out = ['<svg class="chart__svg" viewBox="0 0 600 220" preserveAspectRatio="none" aria-hidden="true">']
    for g in GRADUATIONS:
        y = round(haut - g * echelle, 1)
        out.append(f'<line class="chart__grid" x1="0" x2="{larg}" y1="{y}" y2="{y}" vector-effect="non-scaling-stroke"/>')
    for i, a in enumerate(annees):
        x = i * pas + (pas - barre) / 2
        y0 = haut
        out.append(f'<g class="chart__bar" data-i="{i}">')
        for k in SEGMENTS:
            h = s[k][i] * echelle
            # 2 unités de fond entre les segments, comme entre les barres.
            hh = max(h - 2, 0) if k != SEGMENTS[-1] else h
            out.append(f'<rect class="s-{k[4:]}" x="{x:.1f}" y="{y0 - h:.1f}" width="{barre}" height="{hh:.1f}"/>')
            y0 -= h
        out.append(f'<rect class="chart__hit" x="{i * pas}" y="0" width="{pas}" height="{haut}"/>')
        out.append('</g>')
    out.append('</svg>')
    for g in GRADUATIONS:
        lib = f"€{g // 1000}bn" if lang == "en" else f"{g // 1000} Md€"
        out.append(f'<span class="chart__axis chart__axis--{g // 1000}" aria-hidden="true">{lib}</span>')
    out.append('<ol class="chart__years" aria-hidden="true">')
    for a in annees:
        etoile = "*" if a == 2010 else ""
        cls = ' class="is-tick"' if a % 2 == 0 else ""
        out.append(f'<li{cls}>{a}{etoile}</li>')
    out.append('</ol>')
    return "\n".join(out)


def tableau(annees, s, lang):
    """La table des valeurs, pour qui ne lit pas le graphique."""
    en = lang == "en"
    tete = (["Year", "Sports betting", "Poker", "Horse racing", "Total"] if en
            else ["Année", "Paris sportifs", "Poker", "Paris hippiques", "Total"])
    nb = (lambda v: f"{v:,}") if en else (lambda v: f"{v:,}".replace(",", "\u202f"))
    lignes = ['<table class="data__t">',
              f'<caption>{"Gross gaming revenue, € million, ANJ" if en else "Produit brut des jeux, en millions d’euros, ANJ"}</caption>',
              "<thead><tr>" + "".join(f'<th scope="col">{t}</th>' for t in tete) + "</tr></thead><tbody>"]
    for i, a in enumerate(annees):
        v = [s[k][i] for k in ("pbj_ps", "pbj_po", "pbj_ph")]
        lignes.append(f'<tr><th scope="row">{a}{"*" if a == 2010 else ""}</th>'
                      + "".join(f"<td>{nb(x)}</td>" for x in v) + f"<td>{nb(sum(v))}</td></tr>")
    lignes.append("</tbody></table>")
    return "\n".join(lignes)


def main():
    annees, s = lire()
    donnees = {"source": PAGE, "fichier": SOURCE, "annees": annees, **s}
    (RACINE / "assets/data/marche.json").write_text(
        json.dumps(donnees, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    for page, lang in (("index.html", "en"), ("fr/index.html", "fr")):
        svg = graphique(annees, s, lang)
        table = tableau(annees, s, lang)
        p = RACINE / page
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        t = re.sub(r"(<!-- marche:graphique -->).*?(<!-- /marche:graphique -->)",
                   lambda m: m.group(1) + "\n" + svg + "\n" + m.group(2), t, flags=re.S)
        t = re.sub(r"(<!-- marche:tableau -->).*?(<!-- /marche:tableau -->)",
                   lambda m: m.group(1) + "\n" + table + "\n" + m.group(2), t, flags=re.S)
        p.write_text(t, encoding="utf-8")
    i = annees.index(2024)
    print("2024 :", sum(s[k][i] for k in SEGMENTS), "M€ de PBJ,", s["comptes"][i], "k comptes,",
          s["uniques"][i], "k joueurs uniques,", s["operateurs"][i], "opérateurs,",
          s["agrements"][i], "agréments,", s["mises_ps"][i] + s["mises_ph"][i], "M€ de mises")


if __name__ == "__main__":
    main()
