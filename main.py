import pandas as pd

# https://www.istat.it/it/archivio/266993
df = pd.read_excel("ateco.xlsx")
cols = df.columns
df["ok"] = df[cols[0]].apply(lambda x: "." in x)
df = df[df["ok"]==True][cols].rename(columns={cols[0]: "codice_ateco", cols[1]: "descrizione_ateco"})
df.to_csv("ateco.csv", index=False)
