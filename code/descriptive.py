import pandas as pd
import matplotlib.pyplot as plt
from pytablewriter import MarkdownTableWriter


# This is to do descriptive barcharts and save them with correct xlabels
def barchart(df, xlab, savename, rotatation=50):
    plt.figure(figsize=(15, 10))
    df.size().sort_values(ascending=False).plot.bar()
    plt.xticks(rotation=rotatation)
    plt.xlabel(xlab)
    # plt.ylabel("Number of Values")
    plt.tight_layout()
    plt.savefig('../data/images/' + savename + '.png')


def main():
    # Split the data in various ways
    qa_df = pd.read_csv("../data/QandA.csv")
    df_description = qa_df.describe()
    group_type = qa_df.groupby('questiontype')
    group_type_description = group_type.describe()
    answers = qa_df[qa_df.questiontype == 'answer']
    questions = qa_df[qa_df.questiontype == 'question']

    # Make a table for putting in the github markdown
    writer = MarkdownTableWriter()
    writer.from_dataframe(df_description, add_index_column=True)
    writer.write_table()

    # Generate the different bar charts
    barchart(group_type, 'Response Type', 'responses')
    barchart(questions.groupby('name'), 'Who Asked Questions', 'question_names', rotatation=90)
    barchart(questions.groupby('company'), 'Which Companies Asked Questions', 'question_companies', rotatation=90)
    barchart(answers.groupby('name'), 'Who Gave Answers', 'answer_names')


if __name__ == "__main__":
    main()

pass
