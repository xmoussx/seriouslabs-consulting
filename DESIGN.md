---
name: Serious Labs Consulting
description: Ce marché, vu de l'intérieur.
colors:
  steel: "#1b1e22"
  steel-2: "#23272c"
  steel-0: "#131518"
  rule: "#353b42"
  ink: "#eef0f2"
  ink-2: "#aab2ba"
  brass: "#d4a64a"
  brass-2: "#e7c37a"
  rouge: "#c4382a"
  teal: "#2aa9be"
  s-ps: "#bb8a2e"
  s-po: "#1f9db3"
  s-ph: "#cf4e3c"
  field-edge: "#737b84"
  field-focus: "#202428"
  placeholder: "#8d959d"
  error-text: "#f0a49b"
typography:
  display:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(2.8rem, 6.6vw, 5rem)"
    fontWeight: 900
    lineHeight: 1.02
    letterSpacing: "0"
  heading:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(2.3rem, 5.4vw, 3.9rem)"
    fontWeight: 900
    lineHeight: 0.96
    letterSpacing: "0"
  heading-sm:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(1.9rem, 3.6vw, 2.6rem)"
    fontWeight: 900
    lineHeight: 0.96
    letterSpacing: "0"
  figure:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(2rem, 4.2vw, 3.1rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "0.01em"
    fontFeature: "tnum"
  board-year:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(2rem, 4vw, 2.75rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "0"
    fontFeature: "tnum"
  board-title:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "clamp(1.15rem, 2.2vw, 1.5rem)"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "0.03em"
  entry-date:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "2rem"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "0"
    fontFeature: "tnum"
  entry-title:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "1.6rem"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: "0"
  row-title:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: "0"
  market-name:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "0"
  wordmark:
    fontFamily: "Big Shoulders, Arial Narrow, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "0.04em"
  lede:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  body:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  body-sm:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  readout:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
    fontFeature: "tnum"
  meta:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "normal"
  axis:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "normal"
  label:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 700
    lineHeight: 1.6
    letterSpacing: "normal"
  button:
    fontFamily: "Atkinson Hyperlegible Next, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "normal"
rounded:
  none: "0"
  swatch: "2px"
spacing:
  gutter: "clamp(1rem, 4vw, 2.5rem)"
  band: "clamp(4rem, 9vw, 7rem)"
  band-light: "clamp(3rem, 7vw, 5rem)"
  board-pad: "clamp(1.1rem, 3vw, 2rem)"
  wrap: "78rem"
  target: "2.75rem"
components:
  button-primary:
    backgroundColor: "{colors.brass}"
    textColor: "{colors.steel}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0.75rem 1.4rem"
    height: "3rem"
  button-primary-hover:
    backgroundColor: "{colors.brass-2}"
    textColor: "{colors.steel}"
  button-small:
    backgroundColor: "{colors.brass}"
    textColor: "{colors.steel}"
    rounded: "{rounded.none}"
    padding: "0.55rem 1rem"
    height: "2.75rem"
  board:
    backgroundColor: "{colors.steel-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.board-pad}"
  board-year:
    textColor: "{colors.brass}"
    typography: "{typography.board-year}"
  board-figure:
    textColor: "{colors.ink}"
    typography: "{typography.figure}"
  board-readout:
    textColor: "{colors.ink}"
    typography: "{typography.readout}"
  chart-year-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink}"
    height: "3px"
  chart-year-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink}"
    height: "1px"
  legend-swatch:
    rounded: "{rounded.swatch}"
    size: "0.7rem"
  service-row:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.ink}"
    typography: "{typography.row-title}"
    rounded: "{rounded.none}"
    padding: "1.6rem 0"
  picto:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.brass}"
    rounded: "{rounded.none}"
    padding: "0.5rem"
    size: "3rem"
  entry:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.ink}"
    typography: "{typography.entry-title}"
    rounded: "{rounded.none}"
    padding: "1.5rem 0"
  entry-date:
    textColor: "{colors.brass}"
    typography: "{typography.entry-date}"
    width: "7rem"
  status-regulated:
    textColor: "{colors.brass-2}"
    typography: "{typography.meta}"
    rounded: "{rounded.none}"
    padding: "0.15rem 0.55rem"
  status-emerging:
    textColor: "{colors.teal}"
    typography: "{typography.meta}"
    rounded: "{rounded.none}"
    padding: "0.15rem 0.55rem"
  status-neutral:
    textColor: "{colors.ink}"
    typography: "{typography.meta}"
    rounded: "{rounded.none}"
    padding: "0.15rem 0.55rem"
  input:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.7rem 0.8rem"
    height: "3rem"
  input-focus:
    backgroundColor: "{colors.field-focus}"
    textColor: "{colors.ink}"
  field-error:
    textColor: "{colors.error-text}"
    typography: "{typography.meta}"
  reply:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.9rem 1rem"
---

# Design System: Serious Labs Consulting

Le site de conseil de Serious Labs, `seriouslabs-consulting.com`, en anglais à
`/` et en français à `/fr/`. Il appartient à la famille de `seriouslabs.tech`
(voir le `DESIGN.md` de ce dépôt-là) : même acier, même laiton, mêmes polices
auto-hébergées, mêmes filets de registre. Il n'en reprend ni les étiquettes
ni les plastiques. Sa forme propre, retenue par le client le 29 octobre 2026,
est le tableau du marché.

Fichiers décrits : `index.html`, `fr/index.html`, `404.html`,
`assets/css/conseil.css`, `assets/js/conseil.js`, `assets/img/pictos.svg`,
`outils/marche.py`, `outils/og.py`.

## Overview

**Creative North Star: "Le marché en chiffres"**

La page s'ouvre sur un tableau de bord du marché français des jeux en ligne,
tiré des données ouvertes de l'ANJ. Le visiteur, dirigeant ou responsable
conformité d'un opérateur, voit d'abord le marché : le produit brut des jeux,
les comptes joueurs, les opérateurs, les mises, et quinze ans de barres
empilées qu'il parcourt année par année. Le titre « This market, seen from the
inside. » ne commence qu'en dessous. La preuve vient avant ce qu'on en dit.

Le reste de la page est un registre : les services en lignes à pictogramme,
le parcours d'Antoine Dugast en entrées datées, les marchés dans une vraie
table, les travaux publics, puis la demande. Pas de carte, pas d'ombre, pas
d'image. La tôle (`#23272c`) ne porte que deux choses : le tableau et la
section de demande.

Le monde refuse la page de cabinet à emoji, les chiffres-héros génériques
sans source et la grille de cartes de services.

**Key Characteristics:**

- Acier anthracite et laiton, comme seriouslabs.tech ; pas de plastiques.
- Un panneau de tôle coiffé d'un filet de laiton de 2 px, en tête de page.
- Trois couleurs de segment, validées pour le daltonisme, et nulle part
  ailleurs que dans le graphique.
- Chaque chiffre affiché remonte au fichier de l'ANJ.
- Capitales condensées Big Shoulders 900 pour les titres et les chiffres,
  Atkinson Hyperlegible Next pour tout le reste.
- Des lignes et des filets, jamais des cartes.

## Colors

Contrastes calculés (WCAG 2) sur les valeurs affichées, contre la surface où
chaque couleur est réellement posée.

### Primary

- **Laiton** (`brass`) : l'action (boutons), le filet de 2 px qui coiffe le
  tableau, le registre et la table des marchés, l'année affichée du tableau,
  les dates du registre, le trait des pictogrammes, l'astérisque des champs
  requis, le soulignement des liens, l'anneau de focus. 7,45:1 sur l'acier,
  6,69:1 sur la tôle, 6,96:1 sur un champ au focus. L'acier sur laiton fait
  7,45:1, d'où le texte sombre des boutons.
- **Laiton clair** (`brass-2`) : survol des boutons (acier dessus à 9,94:1) et
  des liens ; texte de l'étiquette « Regulated / Régulé » (9,94:1 sur l'acier).

### Secondary

- **Turquoise** (`teal`) : la seule autre couleur de texte, réservée au statut
  « Emerging / Émergent » de la table des marchés, en texte et en bordure.
  5,99:1 sur l'acier. C'est le turquoise des plastiques de seriouslabs.tech.

### Les trois segments du graphique

| Jeton | Valeur | Segment | Sur la tôle | Sur l'acier |
|---|---|---|---|---|
| `s-ps` | `#bb8a2e` | paris sportifs, en bas de la pile | 4,86:1 | 5,41:1 |
| `s-po` | `#1f9db3` | poker, au milieu | 4,67:1 | 5,20:1 |
| `s-ph` | `#cf4e3c` | paris hippiques, en haut | 3,44:1 | 3,83:1 |

Validés avec le validateur de palette du skill dataviz, en mode sombre, sur
`#1b1e22` et sur la tôle `#23272c` où le graphique est réellement posé :
toutes les vérifications passent sur les deux surfaces. Luminosité OKLCH dans
la bande sombre (0,48 à 0,67), chroma au-dessus de 0,10, écart daltonien le
plus faible entre voisins ΔE 16,4 (poker et hippique, en deutéranopie), écart
le plus faible en vision normale ΔE 21,0 (sport et poker), chaque segment à
plus de 3:1 sur la surface. Au survol, une barre est éclaircie de 15 % ; le
segment hippique passe alors à 4,42:1.

Entre eux, les segments n'ont qu'un contraste de luminance de 1,04 à 1,41:1 :
ils se distinguent par la teinte, et par un jour de 2 unités (sur 220) entre
deux segments d'une même barre. La légende, la ligne de lecture et la table de
données donnent les valeurs en toutes lettres.

### Neutral

- **Acier** (`steel`) : le fond de page et le fond des champs. Encre à
  14,64:1, encre secondaire à 7,80:1.
- **Tôle** (`steel-2`) : le panneau du tableau et la section de demande. Encre
  à 13,15:1, encre secondaire à 7,00:1.
- **Ombre** (`steel-0`) : le pied de page. Encre secondaire à 8,52:1.
- **Filet** (`rule`) : séparations, bordure du tableau, cadre des
  pictogrammes, bordure des statuts neutres. 1,48:1 sur l'acier, 1,33:1 sur
  la tôle : il sépare, il ne porte jamais d'information seul.
- **Encre** (`ink`) et **encre secondaire** (`ink-2`) : texte courant et
  texte d'appoint (chapeaux, libellés des chiffres, descriptions, graduations).

### Couleurs du formulaire

- **Bord de champ** (`field-edge`) : le bas de 2 px de chaque champ. 3,50:1
  contre la tôle qui l'entoure, 3,90:1 contre le fond acier du champ : la
  limite du champ se voit (WCAG 1.4.11). Le commentaire de la feuille de style
  annonce 3,3:1 ; le calcul donne 3,50:1.
- **Champ au focus** (`field-focus`) : le fond du champ actif. Encre à
  13,67:1.
- **Indication** (`placeholder`) : le texte d'exemple. 5,51:1 sur le champ,
  5,15:1 au focus.
- **Texte d'erreur** (`error-text`) : le message sous un champ invalide, en
  gras. 7,50:1 sur la tôle.
- **Rouge** (`rouge`) : le bas pointillé d'un champ invalide et le filet du
  message d'échec. 3,14:1 contre le champ, 2,82:1 contre la tôle : il n'est
  jamais seul, le texte d'erreur et le pointillé disent la même chose.

### Named Rules

**La règle de l'encre pour le choix.** L'année choisie est marquée en encre,
jamais en laiton. Le laiton et le segment des paris sportifs sont de la même
famille (1,38:1 entre eux) : un repère de laiton sous une barre se
confondrait avec elle.

**La règle de l'ordre des segments.** De bas en haut : paris sportifs, poker,
paris hippiques. Sport et hippique ne se touchent jamais : comparés entre eux,
ils tombent à ΔE 14,4 en vision normale, sous le plancher de 15, et à 7,0 en
deutéranopie. Le poker les sépare.

**La règle des segments au graphique.** Les trois couleurs de segment
n'existent que dans le graphique et sa légende. Ailleurs, l'acier, le laiton
et un turquoise de statut suffisent.

**La règle du filet ouvert.** Un filet de laiton de 2 px coiffe ce qui ouvre
une liste ou un panneau : le tableau, le registre des missions, l'entête de la
table des marchés. Un filet d'acier de 1 px sépare les lignes.

## Typography

**Display Font:** Big Shoulders (avec Arial Narrow)
**Body Font:** Atkinson Hyperlegible Next (avec system-ui)

**Character:** Les capitales condensées frappées de seriouslabs.tech pour les
titres, les noms et les chiffres ; une sans-serif de lecture, choisie pour un
public non technique sur téléphone, pour la prose et les libellés.

Les polices sont auto-hébergées (`assets/css/fonts.css`, latin et latin
étendu) ; seule Big Shoulders latin est préchargée. Big Shoulders Stencil est
déclarée par la famille, mais la page ne l'emploie pas : au pochoir, le « € »
se lisait « E ». Les chiffres et les dates sont en Big Shoulders pleine.

### Hierarchy

- **Titre d'ouverture** (900, `clamp(2.8rem, 6.6vw, 5rem)`, 1,02) : le h1,
  sous le tableau, en capitales, équilibré (`text-wrap: balance`).
- **Titre de section** (900, `clamp(2.3rem, 5.4vw, 3.9rem)`, 0,96) ; en petit,
  `clamp(1.9rem, 3.6vw, 2.6rem)` pour les travaux publics.
- **Chiffre du tableau** (900, `clamp(2rem, 4.2vw, 3.1rem)`, 1, +0,01em,
  chiffres tabulaires).
- **Année du tableau** (900, `clamp(2rem, 4vw, 2.75rem)`, laiton, tabulaire).
- **Titre du tableau** (900, `clamp(1.15rem, 2.2vw, 1.5rem)`, +0,03em).
- **Date d'une mission** (900, 2rem, laiton, tabulaire).
- **Nom d'une mission** (900, 1,6rem, 1,05) ; **nom d'un service** (900,
  1,5rem, 1,05) ; **nom d'un marché** (900, 1,35rem, 1,1, sans césure).
- **Mot-symbole** (900, 1,35rem, +0,04em ; 1,1rem sous 26rem).
- **Chapeau** (1,125rem, 1,6) : sous chaque titre de section, 60ch au plus ;
  sous le h1, la largeur de sa colonne.
- **Corps** (1,0625rem, 1,6) ; **petit corps** (0,9375rem) : descriptions,
  navigation, pied de page, libellés de champ en gras.
- **Ligne de lecture** (0,875rem, tabulaire) : les trois segments de l'année.
- **Mention** (0,8125rem, 1,3) : libellés des chiffres, légende, nature d'une
  mission, étiquettes de statut, mots-clés des services, source, messages
  d'erreur (en gras).
- **Graduation** (0,75rem, 1) : axes et millésimes du graphique ; 0,6875rem
  sous 40rem pour les millésimes non choisis.
- **Bouton** (700, 1rem, 1,2) ; petit bouton de l'entête 0,9375rem.

### Named Rules

**La règle du texte en HTML.** Aucun texte dans le SVG du graphique. Le SVG
s'étire en hauteur (`preserveAspectRatio="none"`) ; les graduations et les
millésimes sont du HTML posé par-dessus, à taille fixe, lisibles à toutes les
largeurs.

**Pas de sur-titre.** Comme sur seriouslabs.tech, aucun libellé au-dessus d'un
titre.

## Layout

Largeur utile `min(100% - 2 × gouttière, 78rem)`. Les sections sont séparées
par un filet de 1 px et un rythme de `clamp(4rem, 9vw, 7rem)` ; les travaux
publics, plus courts, prennent `clamp(3rem, 7vw, 5rem)`. L'ouverture n'a pas
de filet et commence à `clamp(1.5rem, 4vw, 2.75rem)` sous l'entête, pour que
le tableau tienne dans le premier écran.

- **Le tableau** : une colonne ; à partir de 64rem, deux (`5fr` les chiffres,
  `7fr` le graphique), le titre et la source sur toute la largeur. Les quatre
  chiffres sont toujours sur deux colonnes.
- **L'ouverture** : sous le tableau, le h1 et le chapeau ; à partir de 64rem,
  côte à côte (`6fr` et `5fr`).
- **Les services** : une colonne ; deux à partir de 52rem, 3rem d'écart.
- **Les travaux publics** : une colonne ; trois à partir de 52rem.
- **La demande** : une colonne ; à partir de 64rem, le texte (`5fr`) et le
  formulaire (`7fr`). Le formulaire est sur deux colonnes, une sous 30rem.

Seuils en usage : 26rem (le mot-symbole rétrécit), 30rem (formulaire en une
colonne), 40rem (missions et marchés se replient, millésimes réduits), 52rem
(services et travaux publics en colonnes), 64rem (tableau, ouverture et
demande en deux colonnes), 760px (la navigation ne garde que la langue et
« Contact »).

Toutes les cibles font au moins 2,75rem de haut : liens de navigation, liens
du pied de page, curseur d'année, « Show the data ».

## Elevation & Depth

Aucune ombre. La profondeur tient à trois tons d'acier : la tôle du tableau et
de la demande posée sur l'acier de la page, l'ombre du pied de page. L'entête
collant est un acier translucide (`rgb(27 30 34 / .82)`, flou de 10px,
saturation 1,2 ; `.94` opaque sans `backdrop-filter`).

### Named Rules

**La règle du plat.** Rien ne flotte. Une barre survolée s'éclaircit, elle ne
se soulève pas.

## Shapes

Tout est d'équerre : le tableau, les champs (`border-radius: 0` explicite),
les boutons, le cadre des pictogrammes, les étiquettes de statut. Le seul
arrondi est celui des pastilles de légende (2px), et dans le dessin, le
rectangle de la carte d'identité du pictogramme KYC.

## Components

### Buttons

Aplat de laiton, texte acier en gras, sans rayon, 3rem de haut au moins.
Survol en laiton clair, en 0,2 s sur la courbe `cubic-bezier(.16, 1, .3, 1)`.
Dans l'entête, une version de 2,75rem, « Contact ». Pendant l'envoi, le bouton
est désactivé (opacité 0,6, texte à 3,55:1) et dit « Sending… » ; après un
envoi réussi, il disparaît.

### Le tableau du marché (composant signature)

Un `<figure>` de tôle, bordé d'un filet de 1 px et coiffé d'un filet de
laiton de 2 px, `clamp(1.1rem, 3vw, 2rem)` de marge intérieure.

- **La tête** : « The French online gambling market » à gauche, l'année
  affichée à droite en grand laiton (« Year shown » pour les lecteurs d'écran).
- **Les quatre chiffres** (`<dl>`, chacun sous un filet de 1 px) : produit
  brut des jeux (2,59 Md€ en 2024) ; comptes joueurs actifs (5,70 M), avec les
  joueurs uniques en dessous (3,87 millions, « non publiés » avant 2018) ;
  opérateurs agréés (17), avec les agréments (29) ; mises des paris sportifs
  et hippiques (11,85 Md€). En grand, « M » ; en appoint, « millions » en
  toutes lettres.
- **Le graphique** : titre en mention, légende à pastilles, puis quinze
  barres empilées de 2010 à 2024. Le SVG (viewBox 600 × 220, barres de 28 sur
  un pas de 40) s'étire à `clamp(10rem, 24vw, 15rem)` de haut ; les filets de
  graduation gardent 1 px (`vector-effect: non-scaling-stroke`). Échelle de 0
  à 3 Md€, graduée à 1, 2 et 3. Les millésimes pairs sont affichés ; le
  premier s'aligne à gauche, le dernier à droite, pour ne pas déborder.
- **La sélection** : l'année choisie prend un trait d'encre de 3 px sous sa
  barre et son millésime passe en encre grasse ; l'année survolée, un trait de
  1 px. Les millésimes voisins s'effacent pour ne pas chevaucher. Aucune barre
  n'est atténuée : l'historique reste lisible.
- **La ligne de lecture**, sous le graphique : « 2024: sports betting €1.76bn
  · poker €493m · horse racing €339m ».
- **L'interaction** : à la souris, survoler une barre affiche son année,
  quitter le graphique revient à l'année choisie ; un clic ou un toucher
  choisit l'année ; le curseur d'année (laiton, 2,75rem) choisit aussi.
- **La région vivante** n'annonce que les choix (curseur, clic), jamais un
  survol, et rien au chargement.
- **La table de données**, dans un `<details>` « Show the data » : les quatre
  colonnes en millions d'euros, chiffres tabulaires, légendée « Gross gaming
  revenue, € million, ANJ ».
- **La source**, en pied : « Source: ANJ open data, 2010 to 2024, published on
  data.gouv.fr », le lien vers le tableau de bord complet, et la note
  « *2010: the regulated market opened in June, so the year covers seven
  months. » L'astérisque suit 2010 partout : millésime, tête, lecture, table.
- **Sans script** : le tableau montre 2024, le graphique et la table sont
  écrits dans la page ; le curseur reste caché (il n'apparaît qu'avec la
  classe `is-live`).

### Le pipeline des chiffres

`outils/marche.py` télécharge le fichier CSV de l'ANJ publié sur data.gouv.fr
(ressource du 8 décembre 2025, `open-data-donnees-marche-des-jah-en-ligne-2024.csv`,
encodé cp1252, séparé par des points-virgules), en extrait neuf séries par
leur libellé exact, et écrit :

- `assets/data/marche.json`, lu par la page pour changer d'année, avec
  l'adresse de la page et du fichier source ;
- le SVG du graphique et la table de données, injectés entre les balises
  `<!-- marche:graphique -->` et `<!-- marche:tableau -->` des deux pages.

Les couleurs ne sont pas dans le script : il pose les classes `s-ps`, `s-po`,
`s-ph`, la feuille de style les colore.

`outils/og.py` rend les images de partage (`og-en.png`, `og-fr.png`,
1200 × 630) depuis `outils/og.html`, qui charge la feuille du site. Ses
chiffres (2,59 Md€, 5,70 millions, 17) sont écrits en dur : à reprendre à
chaque mise à jour des données.

### Les services

Six lignes à pictogramme, sur deux colonnes à partir de 52rem, chacune sous un
filet de 1 px, 1,6rem de marge verticale.

- **Le pictogramme** : carré de 3rem, filet de 1 px, 0,5rem de marge
  intérieure, trait de laiton, à gauche sur toute la hauteur de la ligne.
- **À droite** : le nom en capitales (1,5rem), la phrase en encre secondaire,
  puis trois mots-clés en encre, en mention, séparés par « · ».
- Les lignes ne sont pas des liens et n'ont pas d'état de survol.

### Les pictogrammes

`assets/img/pictos.svg`, une planche de symboles appelée par `<use>` :
`licence`, `integrite`, `strategie`, `kyc`, `jeu-responsable`, `monetisation`,
et la flèche de sortie `sortie`, qui suit chaque lien externe (1em, 0,3em
d'écart). Même grammaire que les poinçons de seriouslabs.tech : grille de 48,
trait de 2,4 en couleur courante, bouts et angles ronds, aucun remplissage hors
les points pleins de rayon 2,6. Chaque tracé porte ses attributs de
présentation : la politique de sécurité refuse tout `<style>` en ligne.

### Le registre des missions

Une liste ordonnée sous un filet de laiton de 2 px, dans l'ordre
chronologique (2010, 2013, 2024, 2025), chaque entrée close par un filet de
1 px, 1,5rem de marge verticale.

- **Au-delà de 40rem**, trois colonnes : la date en laiton (7rem), le nom et
  la phrase (64ch au plus), la nature de la mission alignée à droite (12rem,
  mention).
- **Jusqu'à 40rem**, la date et la nature sur une ligne, le nom et la phrase
  dessous, sur toute la largeur.
- Le chapeau situe le parcours : « Antoine Dugast's work, before and since
  Serious Labs. » Les entrées ne sont pas des liens.

### La table des marchés

Une vraie `<table>` à trois colonnes : marché, statut, apport. L'entête est en
mention grasse sur un filet de laiton de 2 px ; le nom du marché en capitales
(1,35rem), sans césure ; l'apport en encre secondaire.

**Les étiquettes de statut** sont des cadres de 1 px, sans rayon, en mention :

- « Regulated / Régulé » : bordure laiton, texte laiton clair ;
- « Emerging / Émergent » : bordure et texte turquoise ;
- « In transition / En transition » : bordure en pointillé, couleur du filet,
  texte encre ;
- « All types / Tous types » : bordure du filet, texte encre.

Le mot dit le statut ; la couleur et le pointillé ne font que le redoubler.
Jusqu'à 40rem, l'entête est masquée visuellement (gardée pour les lecteurs
d'écran) et chaque rangée devient une grille : le nom et le statut sur une
ligne, l'apport dessous.

### Inputs / Fields

- **Champ** : fond acier sur la tôle, filet de 1 px, bas de 2 px en bord de
  champ, sans rayon, 3rem de haut, `0.7rem 0.8rem` de marge. La zone de
  message fait 9rem, redimensionnable en hauteur.
- **Libellé** : petit corps en gras au-dessus ; un astérisque de laiton
  (masqué aux lecteurs d'écran) pour les champs requis.
- **Focus** : pas d'anneau ; le bas passe au laiton et le fond au champ au
  focus.
- **Erreur** : le formulaire valide lui-même à l'envoi. Sous chaque champ
  invalide, un message en texte d'erreur gras, préfixé « ! » (muet pour les
  lecteurs d'écran), relié par `aria-describedby` ; le champ prend
  `aria-invalid` et un bas rouge en pointillé ; le premier champ invalide
  reçoit le focus. Le message s'efface dès que le champ est corrigé.
- **Message d'état** (`role="status"`) : un bloc acier coiffé d'un filet de
  2 px, laiton pour « envoi en cours » et « reçu », rouge pour un échec.
- **Case de consentement** : 1,25rem, couleur d'accent laiton, texte en encre
  secondaire.
- **Sans script**, le formulaire reste caché (`hidden`) et un `<noscript>`
  renvoie vers LinkedIn : le serveur écarte tout envoi sans l'horodatage que
  pose le script. Un champ piège invisible et le refus des liens complètent la
  protection.

### Navigation

L'entête est collant, 4rem de haut, en acier translucide, sous un filet de
1 px. À gauche, le logo inversé en blanc et le mot-symbole « Serious Labs
Consulting », « Consulting » en laiton : c'est lui qui distingue le site de
seriouslabs.tech, il reste même sur petit téléphone. À droite, les sections
(encre secondaire, encre au survol), la langue et le petit bouton « Contact ».
Sous 760px, les sections disparaissent.

Le focus clavier est partout un anneau de laiton de 3px, décalé de 3px. Le
lien d'évitement apparaît en aplat de laiton.

### Le pied de page

Fond d'ombre, encre secondaire, le mot-symbole et trois liens (Serious Labs,
mentions légales, l'autre langue), puis sous un filet : la raison sociale, le
SIRET en chiffres tabulaires et « No cookies, no trackers. »

### La page absente

`404.html` sert les deux langues. Pas d'entête, pas de pied, pas de script :
le mot-symbole en lien vers l'accueil, puis « Page not found. » en titre
d'ouverture réduit (`clamp(2.8rem, 8vw, 5rem)`, interligne 1, 3rem sous le
mot-symbole), et deux chapeaux, l'anglais vers `/`, le français
(`lang="fr"`) vers `/fr/`. Non indexée.

### Mouvement

Peu de mouvement, et rien à l'arrivée : le survol des boutons en 0,2 s, le
défilement doux vers les ancres (5rem de marge sous l'entête), l'éclaircissement
instantané d'une barre survolée. En mouvement réduit, le défilement redevient
immédiat et toute transition tombe à 0,01 ms.

## Do's and Don'ts

### Do:

- **Do** ouvrir sur les données : le tableau du marché passe avant le titre et
  avant toute affirmation.
- **Do** faire remonter chaque chiffre au fichier de l'ANJ par
  `outils/marche.py`, et relancer `outils/og.py` après chaque mise à jour des
  données, dont il répète les valeurs en dur.
- **Do** marquer la sélection en encre (`#eef0f2`), et garder l'ordre des
  segments : sport, poker, hippique, de bas en haut.
- **Do** garder les textes du graphique en HTML et le SVG étirable, sans texte.
- **Do** attribuer l'expérience à Antoine Dugast, qui a participé aux
  lancements : « Antoine Dugast was part of the PokerStars launches… »,
  « Antoine Dugast a participé… ».
- **Do** garder une table de données sous le graphique, et la note de 2010
  partout où 2010 apparaît.
- **Do** dessiner tout nouveau pictogramme dans la grammaire de la planche :
  grille de 48, trait de 2,4, bouts ronds.
- **Do** vérifier à 3:1 au moins toute limite de champ et tout segment de
  graphique contre la surface où il est posé, et le calculer.

### Don't:

- **Don't** prêter l'expérience à la société : pas de « Serious Labs depuis
  2010 », pas de « nous avons lancé » ; la société n'a pas quinze ans.
- **Don't** afficher un chiffre sans source, ni de montant de gain chez un
  client : les gains Betclic restent qualitatifs.
- **Don't** marquer l'année choisie en laiton, ni poser sport et hippique l'un
  contre l'autre.
- **Don't** annoncer un survol à la région vivante, ni l'année au chargement.
- **Don't** faire de cartes, d'ombres, de dégradés ou d'emoji.
- **Don't** employer les trois couleurs de segment hors du graphique, ni les
  plastiques de seriouslabs.tech sur ce site.
- **Don't** afficher le formulaire sans script, ni une adresse de courriel en
  clair.
