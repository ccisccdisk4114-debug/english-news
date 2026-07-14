import requests
import os
from formatter import clean_html


def send_to_discord(news):

    webhook_url = os.environ["DISCORD_WEBHOOK"]


    embed = {

        "title": f"📰 {news['title']}",

        "url": news["link"],


        "description": clean_html(news["summary"])[:4000],


        "fields": [

            {
                "name": "🏢 Source",
                "value": news["source"],
                "inline": True
            },

            {
                "name": "📅 Published",
                "value": news.get("published", "Unknown"),
                "inline": True
            }

        ],


        "footer": {

            "text":
            "🇬🇧 Daily English Reading • Improve your English every day"

        }

    }


    # adiciona imagem somente se existir
    if news.get("image"):

        embed["image"] = {
            "url": news["image"]
        }


    data = {

        "embeds": [
            embed
        ]

    }


    response = requests.post(
        webhook_url,
        json=data
    )


    if response.status_code == 204:

        print("Mensagem enviada ao Discord!")

    else:

        print("Erro no Discord:")
        print(response.text)
