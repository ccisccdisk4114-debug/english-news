from feeds import RSS_FEEDS
from rss_reader import read_feed
from storage import load_sent_news, save_sent_news, is_already_sent

import random


# Carrega notícias já enviadas
sent_news = load_sent_news()


# Busca todas as notícias dos feeds
all_news = []

for source, url in RSS_FEEDS.items():

    news = read_feed(source, url)

    all_news.extend(news)


print(f"Total de notícias encontradas: {len(all_news)}")


# Filtra apenas notícias novas
new_news = []

for article in all_news:

    if not is_already_sent(article["link"], sent_news):
        new_news.append(article)


print(f"Notícias novas: {len(new_news)}")


# Se não houver notícias novas
if len(new_news) == 0:

    print("Nenhuma notícia nova encontrada.")

else:

    # Escolhe uma notícia aleatória
    selected_news = random.choice(new_news)


    print("\nNotícia escolhida:")
    print("=" * 60)

    print("Fonte:", selected_news["source"])
    print("Título:", selected_news["title"])
    print("Resumo:", selected_news["summary"])
    print("Link:", selected_news["link"])


    # Salva como enviada
    sent_news.append(selected_news["link"])

    save_sent_news(sent_news)


    print("\nNotícia salva no histórico.")
