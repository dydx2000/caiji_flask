import pandas as pd
df = pd.read_excel("output.xlsx",index_col="ID")
df.to_excel("output2.xlsx")
print(df.head())