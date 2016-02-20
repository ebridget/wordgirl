import logic

# umbc api for semantic similarity
sss_url = "http://swoogle.umbc.edu/SimService/GetSimilarity"

def sss(s1, s2, type='relation', corpus='webbase'):
    try:
        response = get(sss_url, params={'operation':'api','phrase1':s1,'phrase2':s2,'type':type,'corpus':corpus})
        return float(response.text.strip())
    except:
        print 'Error in getting similarity for %s: %s' % (s1,s2)
        return 0.0

# find semantically similar words in present web text
def trigger(txt, tgt):
    trigs = [tgt]
    for s in txt:
        if s.isalpha() and s in sss.corpus:
            val = sss(tgt, s, type='relation')
            if val > 0.75:
                trigs.add(s)
    return trigs

# count trigger words
def count_trigs(txt, trigs):
    ctr = 0
    for t in trigs:
        for s in txt:
            if (s == t):
                ctr = ctr + 1
    return ctr

# trigger words as a percentage of the whole text
def trig_stats(txt, trigs):
    count_trigs(txt, trigs) / len(txt)
