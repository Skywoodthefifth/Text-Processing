import re
import requests

url = "https://www.gutenberg.org/files/2638/2638-0.txt"


def get_book(url):
    raw = requests.get(url).text

    start = re.search(r"START OF THE PROJECT GUTENBERG EBOOK THE IDIOT", raw).end()

    stop = re.search(
        r"it might interest you to see the young fellow, seeing that this is so.", raw
    ).start()

    text = raw[start:stop]

    return text


def preprocess(sentence):
    return re.sub("[^A-Za-z0-9.]+", " ", sentence).lower()


book = get_book(url)
processed_book = preprocess(book)
print(processed_book)
