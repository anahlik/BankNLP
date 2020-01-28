# Setup Instructions
1) Clone this file to an appropriate location and setup a python environment using [environment.yml](environment.yml) in anaconda. Note that pdftotext has some extra dependencies to install.
2) Put any relevant data files into the data folder categorized by type of report (quarterly or otherwise) and then explicit type of document.
3) Choose a .py file for a specific task
    1) [bulk_transcript.py](code/bulk_transcript.py) goes through all transcript data and makes a csv of parsed questions and answers.
    2) [descriptive.py](/code/descriptive.py) takes the csv question and answer file from bulk_transcript and outputs some descriptive tables and graphs.
    3) [word2vec.py](/code/word2vec.py) takes the csv question and answer file from bulk_transcript and compiles a word2vec model using the corpus of replies. Note there are commands within the document that allow you to generate tensors for visualization as well.
    4) [xbrl_parse.py](code/xbrl_parse.py) takes a downloaded xbrl file within the file structre and shows how it would parse files.
    5) [xbrl_web_reader.py](/code/xbrl_web_reader.py) will download xbrl 10-Q files from the SEC directly and can be improved to read tags.
    6) _Helper files_ [parsing.py](/code/parsing.py) has functions to read in various pdfs and output relevant data. [question_answer.py](/code/question_answer.py) takes in regions bank transcripts and outputs a dataframe using regex to categorize the data. Could be adapted to other banks formatting as well.