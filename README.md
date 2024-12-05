# Proxy Scraper

Un scrappeur de proxys en Python qui collecte des proxys gratuits à partir de sites populaires et les enregistre dans un fichier texte.

## Fonctionnalités
- Récupère des proxys depuis des sites bien connus comme :
  - [Free Proxy List](https://free-proxy-list.net/)
  - [US Proxy](https://www.us-proxy.org/)
  - [ProxyScrape](https://www.proxyscrape.com/)
- Sauvegarde les proxys récupérés dans un fichier `proxies.txt`.
- Gère les erreurs de récupération pour continuer avec les sites fonctionnels.

## Prérequis
- Python 3.8 ou plus récent
- Bibliothèques nécessaires :
  - `requests`
  - `beautifulsoup4`

Installez-les en exécutant la commande suivante :
```bash
pip install requests beautifulsoup4
