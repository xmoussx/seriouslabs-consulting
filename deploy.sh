#!/usr/bin/env bash
#
# Déploiement de seriouslabs-consulting.com vers /var/www/seriouslabs-consulting.
# Liste explicite de ce qui part en ligne : ni outils/, ni nginx/, ni l'ancien
# site, ni les notes de conception.
#
# Usage : ./deploy.sh

set -euo pipefail

SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="/var/www/seriouslabs-consulting"
CONTENU=(index.html 404.html fr assets robots.txt sitemap.xml)

for item in "${CONTENU[@]}"; do
  [[ -e "$SOURCE/$item" ]] || { echo "Manquant : $item — déploiement interrompu." >&2; exit 1; }
done

if [[ -d "$TARGET" ]]; then
  SAUVE="/var/backups/seriouslabs-consulting"
  sudo mkdir -p "$SAUVE"
  HORO="$(date +%Y%m%d-%H%M%S)"
  sudo tar czf "$SAUVE/site-$HORO.tar.gz" -C "$TARGET" . 2>/dev/null && echo "Sauvegarde : $SAUVE/site-$HORO.tar.gz"
  sudo sh -c "ls -1t '$SAUVE'/site-*.tar.gz 2>/dev/null | tail -n +11 | xargs -r rm -f"
fi

STAGING="$(mktemp -d)"
trap 'rm -rf "$STAGING"' EXIT
for item in "${CONTENU[@]}"; do cp -a "$SOURCE/$item" "$STAGING/"; done

sudo mkdir -p "$TARGET"
sudo rsync -a --delete "$STAGING/" "$TARGET/"
sudo chown -R www-data:www-data "$TARGET"
sudo find "$TARGET" -type d -exec chmod 755 {} +
sudo find "$TARGET" -type f -exec chmod 644 {} +
echo "Déployé dans $TARGET."
