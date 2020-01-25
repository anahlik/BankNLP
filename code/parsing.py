import tabula
import pdftotext
import re
from difflib import SequenceMatcher


# The following is for taking out things that are the same on multiple pages (like headers or footers)
def find_common(text: str) -> set:
    pages = len(text)
    sets = []
    # Starts on the second page so that title pages are ignored. Compares everything to this second page
    for i in range(2, pages):
        # old code using longest match instead of all matches
        # matcha, _, matchsize = SequenceMatcher(None, text[1], text[2]).find_longest_match(0, len(text[1]), 0, len(text[2]))
        # header = text[1][matcha: matcha+matchsize]
        s = set()
        temp = SequenceMatcher(None, text[1], text[i]).get_matching_blocks()
        for j in range(len(temp)):
            # only add a match if it has more than 30 characters in common
            if temp[j].size > 30:
                tempStr = text[1][temp[j].a: temp[j].a+temp[j].size]
                s.add(tempStr)
        sets.append(s)

    # take the minimum set so that we reduce the possible overlap from page 2 to only what is necessary
    length = 100
    returnSet = set()
    for i in range(len(sets)):
        if len(sets[i]) < length:
            length = len(sets[i])
            returnSet = sets[i]

    return returnSet


# This takes a string and perhaps some extra values (like a header) and cleans the corpus to make it more
# machine readable. It then returns the cleaned string.
def clean(text: list, extras: list = 0) -> list:
    output = []
    for i in range(len(text)):
        string = text[i]
        for j in extras:
            string = string.replace(j, ' ') # Take out Extras
        string = string.replace('\r\n', ' ')
        string = string.strip()
        output.append(string)
    return output


# This can combine pages if needed
def combine(text: list) -> str:
    separator = ' '
    return separator.join(text)


# This reads in a table using tabula read and returns a list of DataFrames that have the tables included
def table_read(fileLoc: str) -> list:
    dfs = tabula.read_pdf(fileLoc, pages="all")
    return dfs


# This reads in a text pdf and cleans it using functions above
def text_read(fileLoc: str) -> str:
    with open(fileLoc, "rb") as f:
        pdf = pdftotext.PDF(f)

    textpdf = list(pdf)
    commonLong = list(find_common(textpdf))
    cleanedText = clean(textpdf, commonLong)
    return cleanedText


# This is a way to specify where the data is held
homedir = '../data/'
# addondir = 'quarterly/'
addondir = 'other/'
# type = 'earningsTran/'
# type = 'earningsPR/'
type = 'transcript/'
# specificfile = '2Q19.pdf'
specificfile = 'RF 2019 BAAB Transcript.pdf'

fileLoc = homedir + addondir + type + specificfile
andrew = text_read(fileLoc)

import qa
andrew2 = qa.extractQA(combine(andrew))
pass
