from feeds import RSS_FEEDS
from rss_reader import read_feed
from storage import load_sent_news, save_sent_news, is_already_sent
from discord_sender import send_to_discord

import os


# Carrega histórico
sent_news = load_sent_news()


# Recebe a fonte definida pelo cron/workflow
selected_source = os.environ.get("NEWS_SOURCE")


all_news = []


# Caso uma fonte específica seja definida
if selected_source:

    if selected_source not in RSS_FEEDS:

        print(f"Fonte inválida: {selected_source}")
        exit()


    print(f"Fonte selecionada: {selected_source}")


    news = read_feed(
        selected_source,
        RSS_FEEDS[selected_source]
    )

    all_news.extend(news)


# Caso nenhuma fonte seja definida
else:

    print("Nenhuma fonte definida. Usando todas.")

    for source, url in RSS_FEEDS.items():

        news = read_feed(
            source,
            url
        )

        all_news.extend(news)



print(
    f"Total de notícias encontradas: {len(all_news)}"
)



# Filtra notícias que ainda não foram enviadas
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



# Caso não tenha notícia nova
if len(new_news) == 0:

    print("Nenhuma notícia nova encontrada.")



else:

    # Ordena pela data e pega a mais recente
    selected_news = sorted(
        new_news,
        key=lambda x: x["published"],
        reverse=True
    )[0]


    print("\nNotícia escolhida:")
    print("=" * 60)

    print("Fonte:", selected_news["source"])
    print("Título:", selected_news["title"])
    print("Data:", selected_news["published"])
    print("Link:", selected_news["link"])



    # Envia para Discord
    send_to_discord(
        selected_news
    )



    # Salva no histórico com data
    sent_news.append(
        {
            "link": selected_news["link"],
            "date": selected_news["published"]
        }
    )


    save_sent_news(
        sent_news
    )


    print("\nNotícia enviada e salva no histórico.")
