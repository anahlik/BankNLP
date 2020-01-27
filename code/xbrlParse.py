from bs4 import BeautifulSoup

# https://pypi.org/project/python-xbrl/

homedir = '../data/'
addondir = 'xbrl/'
specificfile = 'regions_rf-2019630x10xq_htm.xml'

fileLoc = homedir + addondir + specificfile

# Find and print stockholder's equity
xmlFile = open(fileLoc)
soup = BeautifulSoup(xmlFile, 'lxml')
tag_list = soup.find_all()
for tag in tag_list:
    if tag.name == 'us-gaap:stockholdersequity':
        print("Stockholder's equity: " + tag.text)
pass