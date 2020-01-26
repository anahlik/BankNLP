import pandas as pd
import matplotlib.pyplot as plt
from pytablewriter import MarkdownTableWriter

def barchart(df, xlab, savename):
    plt.figure(figsize=(15, 10))
    df.size().sort_values(ascending=False).plot.bar()
    plt.xticks(rotation=50)
    plt.xlabel(xlab)
    # plt.ylabel("Number of Values")
    plt.savefig('../data/images/' + savename + '.png')


def main():
    qa_df = pd.read_csv("../data/QandA.csv")
    df_description = qa_df.describe()
    group_type = qa_df.groupby('questiontype')
    group_type_description = group_type.describe()
    answers = qa_df[qa_df.questiontype == 'answer']
    questions = qa_df[qa_df.questiontype == 'question']

    writer = MarkdownTableWriter()
    writer.from_dataframe(df_description, add_index_column=True)
    writer.write_table()

    barchart(group_type, 'Response Type', 'responses')
    barchart(questions.groupby('name'), 'Who Asked Questions', 'question_names')
    barchart(questions.groupby('company'), 'Which Companies Asked Questions', 'question_companies')
    barchart(questions.groupby('name'), 'Who Gave Answers', 'answer_names')

if __name__ == "__main__":
    main()

pass
