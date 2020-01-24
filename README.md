# BankNLP
In this project, I will be taking publicly available banking data and developing a word embedding model with appropriate weights. Publicly available data include quarterly presentations to investors and sec filings.

## Steps
1) Set up git
2) Set up python environment in anaconda using standard packages like numpy and pandas and also install any non-typical packagaes I might use like\
https://github.com/greedo/python-xbrl for xblr parsing\
pdftotext for taking in PDF files[^1]\
tabula-py for taking in table data
3) Download a selection of data and set up directory structure

[^1]: I tried PyPDF2 but it was inserting odd newline characters, and I tried tika but it relied too much on outside servers before I decided on pdftotext (which took a little extra work installing but seems much better overall)