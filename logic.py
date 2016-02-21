from requests import get
import logic

# umbc api for semantic similarity
sss_url = "http://swoogle.umbc.edu/SimService/GetSimilarity"

# delete common words
common_words = ["a", "an", "the", "but", "and", "or"]
def del_words(w):
    if w in common_words:
        return False
    else:
        return True

#find semantically similar words in text
def similar_words(tgt, txt, type='relation', corpus='webbase'):
    trigs = set([tgt])
    txt_smaller = filter(del_words, txt)
    for s in txt_smaller:
        if s.isalpha():
            response = get(sss_url, params={'operation':'api','phrase1':tgt,'phrase2':s,'type':type,'corpus':corpus})
            if float(response.text.strip()) > 0.5:
                trigs.add(s)
    return trigs


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
    count_words(txt, trigs) / len(txt)
