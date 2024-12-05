import requests
from bs4 import BeautifulSoup

def fetch_from_free_proxy_list():
    url = "https://free-proxy-list.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("table", {"id": "proxylisttable"})
    
    if not table:
        raise ValueError("Table des proxys introuvable sur Free Proxy List")
    
    rows = table.find_all("tr")[1:]  # Ignore l'en-tête
    proxies = []
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 7:
            ip = columns[0].text.strip()
            port = columns[1].text.strip()
            https = columns[6].text.strip()
            protocol = "https" if https.lower() == "yes" else "http"
            proxies.append(f"{protocol}://{ip}:{port}")
    return proxies

if __name__ == "__main__":
    try:
        proxies = fetch_from_free_proxy_list()
        print(f"Proxies récupérés : {len(proxies)}")
        for proxy in proxies[:10]:  # Affiche les 10 premiers proxys
            print(proxy)
    except Exception as e:
        print(f"Erreur : {e}")
