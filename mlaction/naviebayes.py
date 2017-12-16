import numpy as np
import re
from sklearn.cross_validation import  train_test_split
from sklearn.naive_bayes import MultinomialNB
import feedparser
import operator

def textParse(fullText):
    listofTokens = re.split(r'\W*',fullText)
    return [tok.lower() for tok in listofTokens if len(tok) > 2]

def word2vec(vol, line):
    retVec = [0] * len(vol)
    for word in line:
        if word in vol:
            retVec[vol.index(word)] += 1
    return retVec

def genData():
    lines = []
    labes = []
    vol = set([])
    for i in range(1,26):
        line = textParse(open("email/spam/%d.txt" % i).read())
        lines.append(line)
        labes.append(1)
        vol = vol | set(line)
        line = textParse(open("email/ham/%d.txt" % i).read())
        lines.append(line)
        labes.append(0)
        vol = vol | set(line)
    vol = list(vol)
    x = []
    for line in lines:
        ret = word2vec(vol, line)
        x.append(ret)
    return x, labes

def getMostFreq(vol, fullWords):
    freqDict = {}
    for tok in vol:
        freqDict[tok] = fullWords.count(tok)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[0:40]


def localWords(feed1, feed2):
    entries = []
    labels = []
    fullWords = []
    vol = set([])
    minLen = min(len(feed1["entries"]), len(feed2["entries"]))
    for i in range(minLen):
        entry = textParse(feed1["entries"][i]["summary"])
        entries.append(entry)
        vol = vol | set(entry)
        labels.append(1)
        fullWords.extend(entry)
        entry = textParse(feed2["entries"][i]["summary"])
        entries.append(entry)
        vol = vol | set(entry)
        labels.append(0)
        fullWords.extend(entry)
    mostFreqWords = getMostFreq(vol, fullWords)
    for word in mostFreqWords:
        if word[0] in vol:
            vol.remove(word[0])
    vol = list(vol)
    x = []
    for entry in entries:
        ret = word2vec(vol, entry)
        x.append(ret)
    return x, labels


if __name__ == "__main__":
    x, y = genData()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    clf = MultinomialNB()
    clf.fit(x_train, y_train)
    pre = clf.predict(x_test)
    print np.mean(pre != y_test)

    ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
    sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
    x, y = localWords(ny,
                      sf)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    clf = MultinomialNB()
    clf.fit(x_train, y_train)
    pre = clf.predict(x_test)
    print np.mean(pre != y_test)
    print clf.get_params()


