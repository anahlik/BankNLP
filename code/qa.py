import re
import pandas as pd


def categorize(text: str):
    if re.match(r'^\s*Operator', text):
        return None
    text = re.split(r'\s{20,}', text)
    if len(text) > 2:
        for i in range(2, len(text)):
            temp = re.sub(r'^\d{0,3} ', '', text[i].strip())
            text[1] = text[1] + ' ' + temp
    elif len(text) == 1:
        return {'questiontype': 'error', 'reply': text[0], 'name': None, 'title': None, 'company': None}
    m = re.match(r'^(?P<Name>([A-Z]\.\s)?([A-Z]\.\s)?[A-Z]\w*(\s[A-Z]\.)?\s[A-Z][A-Za-z\'\\]*(,\sJr\.|Sr\.|IV|III|II|)?)\s(?P<Title>.*), (?P<Company>.*)',
                 text[0])
    if m:
        name = m.group('Name')
        title = m.group('Title')
        company = m.group('Company')
        if re.match(r'^\s*A\s?', text[1]):
            qa = 'answer'
            reply = re.sub(r'^\s*A\s?', '', text[1])
        elif re.match(r'^\s*Q\s?', text[1]):
            qa = 'question'
            reply = re.sub(r'^\s*Q\s?', '', text[1])
        else:
            qa = 'unknown'
            reply = text[1]
    else:
        qa = 'unknown'
        reply = ' '.join(text)
        name = None
        title = None
        company = None

    return {'questiontype': qa, 'reply': reply, 'name': name, 'title': title, 'company': company}


def extractQA(text: str) -> pd.DataFrame:
    start = text.find('QUESTION AND ANSWER SECTION')
    questions = []
    text = text[start+28:len(text)]
    # split whenever you see the signifier of many dots
    text = re.split(r'\.{20,}', text)
    for i, j in enumerate(text):
        # trim any white space and page numbers from beginning
        temp = re.sub(r'^\d{0,3} ', '', j.strip())
        temp = categorize(temp)
        if temp:
            questions.append(temp)
        pass
    df = pd.DataFrame(questions)
    return df
