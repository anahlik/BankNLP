import cleanText

import pdftotext
# from tika import parser
# import PyPDF2

# Load your PDF


homedir = '../data/'
addondir = 'quarterly/'
# type = 'earningsTran/'
type = 'presentation/'
specificfile = '1Q19.pdf'

fileLoc = homedir + addondir + type+ specificfile

# Used PyPDF2
# pdfFileObj = open(fileLoc, 'rb')
#
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# text = []
# for i in pdf:
#     pageObj = pdfReader.getPage(i)
#     text.append(pageObj.extractText())

# Used pdftotext
with open(fileLoc, "rb") as f:
    pdf = pdftotext.PDF(f)

textpdf = list(pdf)

# used tika
# raw = parser.from_file(fileLoc)
# raw = str(raw)
#
#
# safe_text = raw.encode('utf-8', errors='ignore')
# safe_text = str(safe_text).replace("\\\\n", "")
# safe_text = safe_text.replace("\\\\\\'", "'")
#


commonLong = list(cleanText.findCommon(textpdf))
test2 = cleanText.clean(textpdf, commonLong)

pass