from requests import get
import urllib
from bs4 import BeautifulSoup

# extract visible text from url
def extract(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "xml")
    for script in soup(["script", "style"]):
        script.extract()
    text = ''.join(soup.findAll(text=True))
    raw = soup.get_text()
    return text.split()
