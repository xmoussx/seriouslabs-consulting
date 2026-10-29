# seriouslabs-consulting.com

Le site du conseil iGaming de Serious Labs. Statique, servi par nginx depuis le
VPS de seriouslabs.tech (et non plus par GitHub Pages depuis la refonte du
29.10.2026). Le formulaire est traité par le script de seriouslabs.tech.

- `index.html` (anglais, langue par défaut) et `fr/index.html`.
- `outils/marche.py` : télécharge les données ouvertes de l'ANJ, écrit
  `assets/data/marche.json` et inscrit le graphique et la table de données dans
  les deux pages. À relancer quand l'ANJ publie une nouvelle année.
- `outils/og.py` : images de partage.
- `deploy.sh` : mise en ligne dans `/var/www/seriouslabs-consulting`.
- `outils/installe-vps.sh prepare|https` : première installation et bascule.
- `nginx/seriouslabs-consulting.com.conf` : configuration définitive.
- `outils/ancien-site.html` : la version précédente, pour mémoire. Non déployée.

Voir `DESIGN.md` pour le système visuel.
