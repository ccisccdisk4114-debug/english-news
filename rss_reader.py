import feedparser


def read_feed(source_name: str, rss_url: str):
    """
    Lê um feed RSS e devolve uma lista padronizada de notícias.

    Retorno:
    [
        {
            "source": "...",
            "title": "...",
            "summary": "...",
            "link": "...",
            "published": "...",
            "image": "..."
        }
    ]
    """

    feed = feedparser.parse(rss_url)

    news_list = []

    for entry in feed.entries:

        # -------------------------
        # Imagem (nem todos possuem)
        # -------------------------

        image = None

        if "media_thumbnail" in entry:
            image = entry.media_thumbnail[0]["url"]

        elif "media_content" in entry:
            image = entry.media_content[0]["url"]

        elif "links" in entry:
            for link in entry.links:
                if link.get("type", "").startswith("image"):
                    image = link.get("href")
                    break

        # -------------------------
        # Monta a notícia
        # -------------------------

        news = {
            "source": source_name,
            "title": entry.get("title", ""),
            "summary": entry.get("description", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "image": image
        }

        news_list.append(news)

    return news_list
