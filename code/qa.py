import re
import pandas as pd


# all of this function is probably relatively specific to regions but it could be adapted for other banks
def categorize(text: str):
    # Take out anything where the operator talks
    if re.match(r'^\s*Operator', text):
        return None
    # Where there is a lot of space then split it
    text = re.split(r'\s{20,}', text)
    if len(text) > 2:
        # Looks for a page number and takes it out if needed
        for i in range(2, len(text)):
            temp = re.sub(r'^\d{0,3} ', '', text[i].strip())
            text[1] = text[1] + ' ' + temp
    # If it sees something weird it reports what it found but gives question type as an error
    elif len(text) == 1:
        return {'responsetype': 'error', 'response': text[0], 'name': None, 'title': None, 'company': None}

    # This is somewhat complicated but it first finds the question type then tries to find the name, then the title,
    # then the company. Probably specific to what regions looks like unfortunately but can be adapted
    if re.match(r'^\s*A\s?', text[1]):
        qa = 'answer'
        response = re.sub(r'^\s*A\s?', '', text[1])
        m = re.match(r'^(?P<Name>([A-Z]\.\s)?([A-Z]\.\s)?[A-Z]\w*(\s[A-Z]\.)?\s[A-Z][A-Za-z\'\\]*(,\sJr\.|Sr\.|IV|III|II|)?)\s(?P<Title>.*), (?P<Company>.*)',
                 text[0])
    elif re.match(r'^\s*Q\s?', text[1]):
        qa = 'question'
        response = re.sub(r'^\s*Q\s?', '', text[1])
        m = re.match(
            r'^(?P<Name>([A-Z]\.\s)?([A-Z]\.\s)?[A-Z]\w*(\s[A-Z]\.)?(\s[A-Z]\w*)?\s[A-Z][A-Za-z\'\\]*(,\sJr\.|Sr\.|IV|III|II|)?)\s(?P<Title>(Analyst|Portfolio Manager)), (?P<Company>.*)',
            text[0])
    else:
        qa = 'unknown'
        response = text[1]
        m = False

    # if there is a match then write the matches in the appropriate spot
    if m:
        name = m.group('Name')
        title = m.group('Title')
        company = m.group('Company')
    # if no match label it as an error
    else:
        response = ' '.join(text)
        name = 'error'
        title = 'error'
        company = 'error'

    # return the dictionary that will form the dataframe later
    return {'responsetype': qa, 'response': response, 'name': name, 'title': title, 'company': company}


def extractQA(text: str) -> pd.DataFrame:
    # look for the start of the questions and answers
    start = text.find('QUESTION AND ANSWER SECTION')
    questions = []
    text = text[start+28:len(text)]
    # split whenever you see the signifier of many dots
    text = re.split(r'\.{20,}', text)
    for i, j in enumerate(text):
        # trim any white space and page numbers from beginning of text
        temp = re.sub(r'^\d{0,3} ', '', j.strip())
        temp = categorize(temp)
        # if categorize returned something then add to the eventual dataframe
        if temp:
            questions.append(temp)
        pass

    # return a dataframe from the current file
    df = pd.DataFrame(questions)
    return df
