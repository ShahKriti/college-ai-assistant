from bs4 import BeautifulSoup

def read_page(page):

    with open(f"templates/{page}.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style elements
    for tag in soup(["script", "style"]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    # Clean extra spaces
    text = " ".join(text.split())

    # Remove template tags
    text = text.replace("{% extends 'base.html' %}", "")
    text = text.replace("{% block content %}", "")
    text = text.replace("{% endblock %}", "")

    return text