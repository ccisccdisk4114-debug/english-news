from feeds import RSS_FEEDS
from rss_reader import read_feed

all_news = []

for source, url in RSS_FEEDS.items():
    news = read_feed(source, url)
    all_news.extend(news)

print(f"Foram encontradas {len(all_news)} notícias.\n")

for article in all_news:

    print("=" * 60)

    print("Fonte:", article["source"])
    print("Título:", article["title"])
    print("Resumo:", article["summary"])
    print("Data:", article["published"])
    print("Imagem:", article["image"])
    print("Link:", article["link"])

    print()
