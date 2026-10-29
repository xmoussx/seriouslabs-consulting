#!/usr/bin/env bash
#
# Mise en place de seriouslabs-consulting.com sur le VPS, en deux temps, parce
# que le certificat HTTPS ne peut être délivré qu'une fois les DNS basculés.
#
#   1. bash outils/installe-vps.sh prepare
#        copie le site et installe un bloc nginx HTTP provisoire.
#      Puis, chez OVH, zone DNS de seriouslabs-consulting.com :
#        - remplacer les 4 lignes A 185.199.10x.153 par une seule : A 51.68.227.107
#        - CNAME www : seriouslabs-consulting.com. (au lieu de xmoussx.github.io.)
#        - ne toucher ni aux MX, ni au SPF, ni aux NS, ni à data. et board.
#   2. bash outils/installe-vps.sh https
#        une fois les DNS propagés : certificat Let's Encrypt, configuration
#        définitive (nginx/seriouslabs-consulting.com.conf), rechargement.
#
# Chaque fichier nginx remplacé est d'abord sauvegardé dans /var/backups/.
set -euo pipefail

ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE=/etc/nginx/sites-available/seriouslabs-consulting.com
RACINE=/var/www/seriouslabs-consulting

sauve() {
  [[ -f "$SITE" ]] && sudo cp "$SITE" "/var/backups/seriouslabs-consulting.nginx-$(date +%Y%m%d-%H%M%S)" || true
}

case "${1:-}" in
  prepare)
    "$ICI/deploy.sh"
    sauve
    sudo tee "$SITE" >/dev/null <<CONF
# Provisoire, en attendant le certificat : voir outils/installe-vps.sh https.
server {
    listen 80;
    listen [::]:80;
    server_name seriouslabs-consulting.com www.seriouslabs-consulting.com;
    root $RACINE;
    index index.html;
    server_tokens off;
    location ^~ /.well-known/acme-challenge/ { root $RACINE; }
    location = /api/contact.php {
        root /var/www/seriouslabs;
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
    }
    location ~ \.php\$ { return 404; }
    location ~ /\.(?!well-known) { deny all; }
    location / { try_files \$uri \$uri/ =404; }
}
CONF
    sudo ln -sf "$SITE" /etc/nginx/sites-enabled/seriouslabs-consulting.com
    sudo nginx -t
    sudo systemctl reload nginx
    echo "Prêt. Basculez maintenant les DNS chez OVH, puis lancez : bash outils/installe-vps.sh https"
    ;;
  https)
    ip=$(dig +short A seriouslabs-consulting.com | tr '\n' ' ')
    if [[ "$ip" != "51.68.227.107 " ]]; then
      echo "Les DNS ne pointent pas encore uniquement vers 51.68.227.107 (vu : $ip). Patientez puis relancez." >&2
      exit 1
    fi
    sudo certbot certonly --webroot -w "$RACINE" \
      -d seriouslabs-consulting.com -d www.seriouslabs-consulting.com \
      --non-interactive --agree-tos --keep-until-expiring
    sauve
    sudo cp "$ICI/nginx/seriouslabs-consulting.com.conf" "$SITE"
    sudo nginx -t
    sudo systemctl reload nginx
    echo "En ligne en HTTPS."
    ;;
  *)
    echo "Usage : bash outils/installe-vps.sh prepare|https" >&2
    exit 2
    ;;
esac
