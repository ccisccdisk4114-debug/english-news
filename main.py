from feeds import RSS_FEEDS
from rss_reader import read_feed
from storage import load_sent_news, save_sent_news, is_already_sent
from discord_sender import send_to_discord

import random


# Carrega histórico de notícias enviadas
sent_news = load_sent_news()


# Busca todas as notícias dos feeds RSS
all_news = []

for source, url in RSS_FEEDS.items():

    news = read_feed(source, url)

    all_news.extend(news)


print(f"Total de notícias encontradas: {len(all_news)}")


# Filtra notícias que ainda não foram enviadas
new_news = []

for article in all_news:

    if not is_already_sent(article["link"], sent_news):
        new_news.append(article)


print(f"Notícias novas: {len(new_news)}")


# Caso não existam notícias novas
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


    # Cria mensagem para o Discord
    message = f"""
🇬🇧 **Daily English Reading**

📰 **{selected_news['title']}**

🏢 **Source:**
{selected_news['source']}

📖 **Summary:**
{selected_news['summary']}

🔗 **Read more:**
{selected_news['link']}
"""


    # Envia para o Discord
    send_to_discord(message)


    # Salva a notícia no histórico
    sent_news.append(selected_news["link"])

    save_sent_news(sent_news)


    print("\nNotícia enviada e salva no histórico.")
