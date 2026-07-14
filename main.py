from feeds import RSS_FEEDS
from rss_reader import read_feed
from storage import load_sent_news, save_sent_news, is_already_sent
from discord_sender import send_to_discord

import random
import os


sent_news = load_sent_news()


selected_source = os.environ.get("NEWS_SOURCE")


all_news = []


if selected_source:

    if selected_source not in RSS_FEEDS:

        print(
            f"Fonte inválida: {selected_source}"
        )

        exit()


    print(
        f"Fonte selecionada: {selected_source}"
    )


    news = read_feed(
        selected_source,
        RSS_FEEDS[selected_source]
    )


    all_news.extend(news)



else:

    print(
        "Nenhuma fonte definida. Usando todas."
    )


    for source, url in RSS_FEEDS.items():

        news = read_feed(
            source,
            url
        )

        all_news.extend(news)



print(
    f"Total de notícias encontradas: {len(all_news)}"
)



new_news = []


for article in all_news:

    if not is_already_sent(
        article["link"],
        sent_news
    ):

        new_news.append(article)



print(
    f"Notícias novas: {len(new_news)}"
)



if len(new_news) == 0:

    print(
        "Nenhuma notícia nova."
    )


else:

    selected_news = random.choice(
        new_news
    )


    print(
        selected_news["title"]
    )


    send_to_discord(
        selected_news
    )


    sent_news.append(
        selected_news["link"]
    )


    save_sent_news(
        sent_news
    )


    print(
        "Finalizado."
    )
