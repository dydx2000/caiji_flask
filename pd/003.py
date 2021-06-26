import pandas as pd

d = {"x": 100, "y": 200, "z": 300}
'''s1 = pd.Series(d)
print(s1.index)
print(s1)'''

s1 = pd.Series([100, 200, 300], index=["a", "b", "c"])
print(s1)