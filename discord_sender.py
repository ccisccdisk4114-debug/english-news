import requests
import os


def send_to_discord(message):

    webhook_url = os.environ["DISCORD_WEBHOOK"]

    data = {
        "content": message
    }

    response = requests.post(
        webhook_url,
        json=data
    )

    if response.status_code == 204:
        print("Mensagem enviada ao Discord!")

    else:
        print("Erro ao enviar:")
        print(response.text)
