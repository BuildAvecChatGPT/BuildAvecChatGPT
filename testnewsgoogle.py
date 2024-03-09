from googlesearch import search

def get_google_news_urls(query, num_results):
    urls = []
    for url in search(query, tld="com", num=num_results, stop=num_results, pause=2.0):
        urls.append(url)
    return urls

query = "actualité intelligence artificielle"
num_results = 10
urls = get_google_news_urls(query, num_results)
print(urls)
