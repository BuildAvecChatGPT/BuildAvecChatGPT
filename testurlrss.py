import feedparser
from datetime import datetime, timedelta

def get_news_urls_from_rss(rss_urls, max_articles_per_source):
    all_urls = []
    current_time = datetime.utcnow()
    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:max_articles_per_source]:
            pub_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
            if current_time - pub_date <= timedelta(days=2):
                all_urls.append(entry.link)
    return all_urls

rss_urls = [
    'https://openai.com/blog/rss',
    'opera://news/?preview_title=AI&preview_url=https%3A%2F%2Fblog.google%2Ftechnology%2Fai%2Frss%2F',
    # Ajoutez d'autres sources RSS ici
]

max_articles_per_source = 10
urls = get_news_urls_from_rss(rss_urls, max_articles_per_source)
print(urls)
