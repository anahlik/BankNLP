# BankNLP
In this project, I will be taking publicly available banking data, parsing it to get it into a useable format, showing some descriptive statistics, and finally developing a word embedding model. Publicly available data include quarterly presentations to investors and sec filings. Specifically, I will be focusing on publicly available Regions bank information over the past two years.

## Steps
1) Set up git
2) Set up python environment in anaconda using standard packages like numpy, matplotlib, and pandas and also install any non-typical packages I might use like\
https://github.com/greedo/python-xbrl for xblr parsing\
pdftotext for taking in PDF files<sup>1</sup>\
tabula-py for taking in table data\
pytablewriter for writing markdown tables (for this document)\
nltk and gensim for Word2Vec modeling
3) Download a selection of data and set up directory structure
4) Started coding data ingestion starting with different .py files and then unifying some of the files into a helper .py file using variouis functions (putting the original files in an folder labeled old). Make sure to do effective commenting of what each function performs and other comments along the way where there could be confusion.
5) Set up automated bulk ingestion of the pdfs and automated descriptive statistics to take a first look at the data and see any glaring errors.

[1]: I tried PyPDF2 but it was inserting odd newline characters, and I tried tika but it relied too much on outside servers before I decided on pdftotext (which took a little extra work installing but seems much better overall)

For my process, I focused first on reading in the pdf files and making sure I was getting text and tables that were usable. Next, I focused in on the transcripts for Regions banks both quarterly report calls and other events. I wanted to have a good source of textual data that also had labels that I could parse. This allows me to show some descriptive stats and do simple NLP. I worked to get the transcripts into a generic dataframe structure that would be usable for any bank. The end goal would be to ingest transcript information for any publicly traded banks and use the same functions to immediately be able to ingest that information and draw conclusions.



## Some Results
I took transcripts (and other published data) from Regions Bank over the period from January 1 2018 to January 20th 2020 and pulled relevant information using string and regex functions. The parsing I did unfortunately is relatively specific to how regions formatted its pdf. However, the broad intuition would be the same to read in other transcripts. I developed a dataframe of results that included the person who gave the response, their title, their company, the type of response, the response itself, the type of document, the bank in question, and the filename of the file it was pulled from. It also perserved data that was not ingested correctly and noted it. This ensures that if when running the script, there were systematic errors showing up you could see which files were giving the errors by matching it to the filename.<sup>2</sup> A csv of the dataframe is given in [QandA.csv](output/QandA.csv)

[2] For example in this process it turns out some of the transcripts from specific events were encoded slightly differently and thus gave errors that could be corrected in a finalized product.

#### Tables
The following provides descriptive statistics for the entire dataframe

|      |responsetype| response |       name        | title |        company        | bank  |doctype|                            filename                             |
|------|------------|----------|-------------------|-------|-----------------------|-------|-------|-----------------------------------------------------------------|
|count |1305        |1305      |1146               |1146   |1146                   |1305   |1305   |1305                                                             |
|unique|           4|      1161|                 49|     35|                     32|      1|      2|                                                               19|
|top   |answer      |Thank you.|John M. Turner, Jr.|Analyst|Regions Financial Corp.|regions|qr     |../data/other/transcript\regions_Investor-Day-2019-Transcript.pdf|
|freq  |675         |21        |258                |434    |666                    |1305   |744    |129                                                              |

Note that this shows us there are some replies that aren't very helpful like "Thank you" and some columns are not helpful at all (for the moment) due to the lack of variation in the current dataset. For example, the bank column is completely unnecessary at the moment, though it would be key as more banks are loaded into the database.

#### Figures
These figures quickly visualize the data by what types of questions are in the dataset, who is answering the questions, who is asking the questions, and what companies are asking questions.

![Types](output/images/responses.png)
![Answers](output/images/answer_names.png)
![QuestionNames](output/images/question_names.png)
![QuestionNames](output/images/question_companies.png)

Note this quickly shows us things like relative frequency of names and companies that show up. It also shows that some names are probably the same person but the transcript has coded them differently. For example, Matthew O'Conner shows up 3 different ways. It is important to decide if this matters. We also see the companies graph is very similar to the names graph suggesting that generally there is only one analyst asking questions for each company and perhaps companies is a better way to slice the data.

In general, without getting good data to start we will have bad conclusions at the end. Garbage in Garbage out. Ingesting the data aka [data munging](https://en.wikipedia.org/wiki/Data_wrangling) into a consistent format will allow the downstream analysis to proceed seamlessly if done well.