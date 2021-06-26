# encoding:utf-8
import pandas as pd

f = pd.read_excel("People.xlsx", index='ID')

print(f.head(5))
print(f.columns)
f.to_excel("output.xlsx")
print("done!")
