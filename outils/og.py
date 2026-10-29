"""Fabrique assets/img/og-en.png et og-fr.png à partir de outils/og.html.

Usage, depuis la racine du dépôt :
    python3 -m http.server 8767 --bind 127.0.0.1 &
    python3 outils/og.py
"""
import asyncio
from playwright.async_api import async_playwright

TEXTES = {
    "en": ("Gambling,<br>seen from the inside.",
           ["French online GGR, 2024", "Active player accounts", "Licensed operators"],
           ["€2.59bn", "5.70M"], "Source: ANJ open data"),
    "fr": ("Le jeu d'argent,<br>vu de l'intérieur.",
           ["Produit brut des jeux en ligne, 2024", "Comptes joueurs actifs", "Opérateurs agréés"],
           ["2,59 Md€", "5,70 millions"], "Source : données ouvertes de l'ANJ"),
}

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        p = await b.new_page(viewport={"width": 1200, "height": 630})
        for lang, (titre, libelles, nombres, source) in TEXTES.items():
            await p.goto("http://127.0.0.1:8767/outils/og.html", wait_until="networkidle")
            await p.evaluate("""([t, l, n, s]) => {
                document.querySelector('[data-t]').innerHTML = t;
                l.forEach((v, i) => document.querySelector(`[data-l="${i}"]`).textContent = v);
                n.forEach((v, i) => document.querySelector(`[data-n="${i}"]`).textContent = v);
                document.querySelector('[data-s]').textContent = s;
            }""", [titre, libelles, nombres, source])
            await p.evaluate("document.fonts.ready")
            await p.wait_for_timeout(1200)
            await p.screenshot(path=f"assets/img/og-{lang}.png")
        await b.close()

asyncio.run(main())
