import requests
from bs4 import BeautifulSoup

def fetch_items(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    items = []
    for item in soup.find_all("div", class_="catalog-item"):
        title = item.find("h3", class_="title").text.strip()
        price = item.find("div", class_="price").text.strip()
        link = item.find("a")["href"]
        items.append({
            "title": title,
            "price": price,
            "link": f"https://www.vinted.pt{link}"
        })
    return items

# Links das marcas (adicione outros conforme necessário)
links = {
    "Zara": "https://www.vinted.pt/catalog?time=1731694909&catalog[]=2050&catalog[]=4&currency=EUR&brand_ids[]=12&status_ids[]=6&status_ids[]=1&status_ids[]=2&page=1&search_id=18662263633",
    "Nike": "https://www.vinted.pt/catalog?time=1731694840&catalog[]=2050&catalog[]=4&currency=EUR&brand_ids[]=88&status_ids[]=6&status_ids[]=1&status_ids[]=2&page=1&search_id=18662263633",
    "Ralph Lauren": "https://www.vinted.pt/catalog?time=1731694840&catalog[]=2050&catalog[]=4&currency=EUR&brand_ids[]=88&status_ids[]=6&status_ids[]=1&status_ids[]=2&page=1&search_id=18662263633",
    "Adidas": "https://www.vinted.pt/catalog?time=1731694832&catalog[]=2050&catalog[]=4&currency=EUR&brand_ids[]=14&status_ids[]=6&status_ids[]=1&status_ids[]=2&page=1&search_id=18662263633"
}

def fetch_all_items():
    all_items = {}
    for brand, url in links.items():
        all_items[brand] = fetch_items(url)
    return all_items
