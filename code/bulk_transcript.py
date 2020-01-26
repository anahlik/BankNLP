import qa
import parsing
import pandas as pd
import glob

# glob gets all of the files in a directory. We build up a list of all files that we will loop through and add
allfiles = list()
allfiles.append([glob.glob('../data/quarterly/earningsTran/regions_*.pdf'), 'regions', 'qr'])
allfiles.append([glob.glob('../data/other/transcript/regions_*.pdf'), 'regions', 'other'])

df = pd.DataFrame()

# Read all of the files in and build a dataframe
for types in allfiles:
    for fileLoc in types[0]:
        text = parsing.text_read(fileLoc)
        df_temp = qa.extractQA(parsing.combine(text))
        df_temp['bank'] = types[1]
        df_temp['doctype'] = types[2]
        df_temp['filename'] = fileLoc
        df = pd.concat([df, df_temp])
    pass

# Save to csv for later
df.to_csv("../data/QandA.csv", index=False)
pass
