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
    #visible_text = filter(visible, raw)
    return text.split()

web_text = extract("https://en.wikipedia.org/wiki/Fermi_paradox")
print web_text
