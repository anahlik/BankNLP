import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import re
import gensim

# Uncomment if you need to download resources for nltk
# nltk.download('stopwords')
# nltk.download('punkt')


# This tokenizes the responses and takes out stopwords using the natural language toolkit.
def tokenize(corpus: list) -> list:
    text = []
    # This is to get rid of words that will not be useful later
    stop_words = set(nltk.corpus.stopwords.words('english'))
    for i in corpus:
        for j in sent_tokenize(i):
            temp = []
            for k in word_tokenize(j):
                temp.append(k)
            temp = [w for w in temp if not w in stop_words]
            text.append(temp)

    return text


# preprocess the text to only keep letters (will lose numerical info)
def preprocess(x):
    x = re.sub(r'[^a-z\s]', '', x.lower())
    return x


def main():
    qa_df = pd.read_csv("../output/QandA.csv")
    # only take the questions and answers not error values
    goodvals = qa_df[(qa_df.responsetype == 'answer') | (qa_df.responsetype == 'question')]
    text = goodvals['response'].apply(preprocess)
    text2 = tokenize(text)
    modelCBOW = gensim.models.Word2Vec(text2, min_count=5, size=10, window=5)
    modelSGRAM = gensim.models.Word2Vec(text2, min_count=5, size=10, window=5, sg=1)
    modelCBOW.wv.save_word2vec_format('../output/model/CBOW.model')
    modelSGRAM.wv.save_word2vec_format('../output/model/SGRAM.model')
    # Use the following command (while in the correct directory) to generate tensorflow vectors
    # python -m gensim.scripts.word2vec2tensor -i CBOW.model -o BankCBOW
    good_CBOW = modelCBOW.wv.similar_by_word('good', topn=10)
    good_SGRAM = modelSGRAM.wv.similar_by_word('good', topn=10)
    earnings_CBOW = modelCBOW.wv.similar_by_word('earnings', topn=10)
    earnings_SGRAM = modelSGRAM.wv.similar_by_word('earnings', topn=10)
    earnings_rolling_SGRAM = modelSGRAM.wv.similarity('earnings', 'rolling')
    pass


if __name__ == "__main__":
    main()
