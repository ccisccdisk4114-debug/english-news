import re


def clean_html(text):

    if not text:
        return ""

    text = re.sub("<.*?>", "", text)

    text = text.replace("&nbsp;", " ")

    return text.strip()
