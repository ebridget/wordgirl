from requests import get
import logic


# umbc api for semantic similarity
sss_url = "http://swoogle.umbc.edu/SimService/GetSimilarity"


#find semantically similar words in text
def similar_words(tgt, txt, type='relation', corpus='webbase'):
    trigs = set([tgt])
    not_trigs = set([])
    ctr = 0
    for s in txt:
        if s.isalpha():
            if s in trigs:
                ctr += 1
            else:
                if s not in not_trigs:
                    response = get(sss_url, params={'operation':'api','phrase1':tgt,'phrase2':s,'type':type,'corpus':corpus})
                    if float(response.text.strip()) > 0.5:
                        trigs.add(s)
                        ctr += 1
                    else:
                        not_trigs.add(s)
    return trigs, ctr


# count keyword and related words
def count_words(txt, trigs):
    ctr = 0
    for t in trigs:
        for s in txt:
            if (s == t):
                ctr = ctr + 1
    return ctr

# instances of keyword and related words as a percentage of the whole text
def word_percent(txt, trigs):
    return count_words(txt, trigs) / len(txt)
