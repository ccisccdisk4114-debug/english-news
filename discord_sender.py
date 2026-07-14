import requests
import os


def send_to_discord(news):

    webhook_url = os.environ["DISCORD_WEBHOOK"]

    embed = {
        "title": f"📰 {news['title']}",
        "url": news["link"],

        "description": news["summary"],

        "fields": [
            {
                "name": "🏢 Source",
                "value": news["source"],
                "inline": True
            },
            {
                "name": "📅 Published",
                "value": news["published"],
                "inline": True
            }
        ],

        "footer": {
            "text": "🇬🇧 Daily English Reading • Improve your English every day"
        },

        "thumbnail": {
            "url": news["image"]
        }
    }


    data = {
        "embeds": [embed]
    }


    response = requests.post(
        webhook_url,
        json=data
    )


    if response.status_code == 204:
        print("Embed enviado ao Discord!")

    else:
        print("Erro ao enviar embed:")
        print(response.text)
