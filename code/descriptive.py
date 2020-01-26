import pandas as pd
import matplotlib.pyplot as plt

qa_df = pd.read_csv("../data/QandA.csv")
df_description = qa_df.describe()
group_type = qa_df.groupby('questiontype')
group_type_description = group_type.describe()
answers = qa_df[qa_df.questiontype == 'answer']
questions = qa_df[qa_df.questiontype == 'question']

plt.figure(figsize=(15, 10))
group_type.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Response Type")
# plt.ylabel("Number of Values")
plt.savefig('../data/images/responses.png')

plt.figure(figsize=(15, 10))
questions.groupby('name').size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=90)
plt.xlabel("Who Asked Questions")
# plt.ylabel("Number of Values")
plt.tight_layout()
plt.savefig('../data/images/questionnames.png')

plt.figure(figsize=(15, 10))
questions.groupby('company').size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=90)
plt.xlabel("Which Companies Asked Questions")
# plt.ylabel("Number of Values")
plt.tight_layout()
plt.savefig('../data/images/questioncompanies.png')

plt.figure(figsize=(15, 10))
answers.groupby('name').size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=45)
plt.xlabel("Who Gave Answers")
# plt.ylabel("Number of Values")
plt.tight_layout()
plt.savefig('../data/images/answernames.png')

pass
