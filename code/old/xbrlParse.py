from xbrl import XBRLParser, GAAP, GAAPSerializer

# https://pypi.org/project/python-xbrl/

homedir = '../data/'
addondir = 'xbrl/'
specificfile = 'rf-20190331.xml'

fileLoc = homedir + addondir + specificfile

xbrl_parser = XBRLParser()
xbrl = xbrl_parser.parse(fileLoc)

gaap_obj = xbrl_parser.parseGAAP(xbrl,
                                 doc_date="20190401",
                                 context="current",
                                 ignore_errors=0)

# Serialize the GAAP data
serializer = GAAPSerializer()
result = serializer.dump(gaap_obj)
pass