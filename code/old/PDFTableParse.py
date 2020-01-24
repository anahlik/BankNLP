import tabula

# Load your PDF


homedir = '../data/'
addondir = 'quarterly/'
# type = 'earningsTran/'
type = 'earningsPR/'
specificfile = '1Q19.pdf'

fileLoc = homedir + addondir + type + specificfile


dfs = tabula.read_pdf(fileLoc, pages="all")


pass