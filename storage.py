import json
import os


FILE_NAME = "sent_news.json"


def load_sent_news():
    """
    Carrega os links das notícias já enviadas.
    """

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)



def save_sent_news(sent_news):
    """
    Salva os links das notícias enviadas.
    """

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(
            sent_news,
            file,
            indent=4,
            ensure_ascii=False
        )



def is_already_sent(link, sent_news):
    """
    Verifica se uma notícia já foi enviada.
    """

    return link in sent_news
