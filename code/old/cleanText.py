import re
from difflib import SequenceMatcher

def findCommon(text):
    pages = len(text)
    sets = []
    for i in range(2, pages):
        # matcha, _, matchsize = SequenceMatcher(None, text[1], text[2]).find_longest_match(0, len(text[1]), 0, len(text[2]))
        # header = text[1][matcha: matcha+matchsize]
        s = set()
        temp = SequenceMatcher(None, text[1], text[i]).get_matching_blocks()
        for j in range(len(temp)):
            if temp[j].size > 30:
                tempStr = text[1][temp[j].a: temp[j].a+temp[j].size]
                s.add(tempStr)
        sets.append(s)

    length = 100
    for i in range(len(sets)):
        if len(sets[i]) < length:
            length = len(sets[i])
            returnSet = sets[i]

    return returnSet

def clean(text, extras):
    output = []
    for i in range(len(text)):
        string = text[i]
        for j in extras:
            string = string.replace(j, ' ') # Take out Extras
        string = string.replace('\r\n', ' ')
        string = string.strip()
        output.append(string)
    return output

def makeCorpus(text):
    pass