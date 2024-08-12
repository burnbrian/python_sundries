import requests
from collections import Counter
from io import StringIO
from html.parser import HTMLParser
import re

def get_page(url):
    """Get the content of a web page"""
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    return r.text

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def main():
    url = "https://www.sans.org"
    page_content = get_page(url)
    if page_content:
        text = strip_tags(page_content)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        words = text.split()
        word_count = Counter(words)
        for word, count in word_count.most_common(100):
            print(f"{word}: {count}")

if __name__ == '__main__':
    main()
