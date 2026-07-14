import json
import os


FILE = "sent_news.json"


def load_sent_news():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_sent_news(news):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            news,
            f,
            indent=4,
            ensure_ascii=False
        )



def is_already_sent(link, sent_news):

    for item in sent_news:

        if item["link"] == link:
            return True

    return False
