import pandas as pd

# https://www.istat.it/it/archivio/266993
df = pd.read_excel("ateco.xlsx")
atecos = [value for value in df[df.columns[0]].values if "." in value]
series_ateco = pd.Series(atecos)
series_ateco.to_csv("ateco.csv", index=False)
