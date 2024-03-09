import requests
from bs4 import BeautifulSoup

def get_techcrunch_urls():
    url = "https://techcrunch.com/category/artificial-intelligence/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []
    for article in soup.find_all('h2', class_='post-block__title'):
        link = article.find('a')['href']
        urls.append(link)
    return urls

if __name__ == "__main__":
    urls = get_techcrunch_urls()
    print("URLs des dernières actualités sur l'IA sur TechCrunch :")
    for url in urls:
        print(url)
