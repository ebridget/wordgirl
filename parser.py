from requests import get
import urllib2
from bs4 import BeautifulSoup

def visible(element):
    if element.parent.name in ['head', 'title', 'p']:
        return True
    else:
        return False

def extract(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, "xml")
    text = soup.findAll(text = 'true')
    raw = soup.get_text()
    visible_text = filter(visible, text)
    print raw
    print visible_text
    return visible_text

def finder(orig, target):
    orig = orig.strip()
    if len(orig) < 1 or not orig:
        return "failed"
    words = orig.split()
    ctr = 0
    for s in words:
        if (s == target):
            ctr = ctr + 1
    return ctr

web_text = extract("https://en.wikipedia.org/wiki/Fermi_paradox")
print web_text[0:12]

'''

sss_url = "http://swoogle.umbc.edu/SimService/GetSimilarity"

def sss(s1, s2, type='relation', corpus='webbase'):
    try:
        response = get(sss_url, params={'operation':'api','phrase1':s1,'phrase2':s2,'type':type,'corpus':corpus})
        return float(response.text.strip())
    except:
        print 'Error in getting similarity for %s: %s' % ((s1,s2), response)
        return 0.0
'''

'''
def extra():
    triggers = []

    for s in sss.corpus:
        val = sss(target, s)
        if val > 0.75:
            triggers.add(s)

    overall_count = 0
    for s in triggers:
        overall_count = overall_count + finders(s)
'''
