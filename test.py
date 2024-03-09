import requests
from bs4 import BeautifulSoup

def extract_article(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Vérifier si la balise h1 existe
    title_tag = soup.find('h1')
    if title_tag:
        title = title_tag.get_text()
    else:
        title = "Titre non trouvé"

    paragraphs = soup.find_all('p')
    content = ' '.join([p.get_text() for p in paragraphs])
    return title, content


def generate_html(url_list):
    news_items_html = generate_news_items(url_list)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Dernières News IA</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          margin: 0;
          padding: 0;
          background-color: #f9f9f9;
          color: #333;
        }}

        .container {{
          max-width: 800px;
          margin: 50px auto;
          padding: 20px;
        }}

        h1 {{
          text-align: center;
          color: #007bff;
        }}

        .news-item {{
          background-color: #fff;
          border-radius: 8px;
          box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
          margin-bottom: 30px;
          padding: 20px;
          cursor: pointer;
          transition: transform 0.2s;
        }}

        .news-item:hover {{
          transform: scale(1.03);
        }}

        .news-item h2 {{
          color: #007bff;
        }}

        .news-item p {{
          margin-bottom: 10px;
        }}

        .subscribe {{
          text-align: center;
          margin-top: 50px;
        }}

        .subscribe button {{
          padding: 10px 20px;
          background-color: #007bff;
          color: #fff;
          border: none;
          border-radius: 5px;
          font-size: 16px;
          cursor: pointer;
        }}

        .subscribe button:hover {{
          background-color: #0056b3;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Dernières News IA</h1>
        {news_items_html}
        <div class="subscribe">
          <button onclick="window.location.href='https://buildavecchatgpt.github.io/';">S'abonner pour rester informé</button>
        </div>
      </div>
    </body>
    </html>
    """
    with open('news.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    print("Fichier HTML créé avec succès.")

def generate_news_items(url_list):
    news_items_html = ""
    for url in url_list:
        title, content = extract_article(url)
        summary = generate_summary(content)
        news_item_html = f"""
        <div class="news-item" onclick="window.location.href='{url}';">
          <h2>{title}</h2>
          <p>{summary}</p>
        </div>
        """
        news_items_html += news_item_html
    return news_items_html

def generate_summary(content):
    paragraphs = content.split("\n")
    summary = ""
    sentence_count = 0
    for paragraph in paragraphs:
        sentences = paragraph.split(".")
        for sentence in sentences:
            if sentence.strip() != "":
                summary += sentence.strip() + ". "
                sentence_count += 1
                if sentence_count >= 3:  # Arrête après les 3 premières phrases
                    break
        if sentence_count >= 3:
            break
    return summary.strip()

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
    urls = [
        'https://www.francetvinfo.fr/internet/intelligence-artificielle/intelligence-artificielle-sam-altman-reintegre-le-conseil-d-administration-d-openai_6413401.html',
    ]
    # Ajouter les URLs de TechCrunch aux URLs existantes
    #urls += get_techcrunch_urls()
    generate_html(urls)
