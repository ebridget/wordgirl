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
    percentage = round((((ctr*1.0) / len(txt)) * 100), 2)
    return trigs, percentage
