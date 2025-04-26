import pandas as pd

df = pd.read_csv("Cars.csv")

df2 = df.groupby("fuel").agg(list)
result = df2.index.to_list()
print(df2) 
#                           make  ...      engine-size
# fuel                            ...
# diesel          [mazda, volvo]  ...       [nan, 2.0]
# gas     [audi, dodge, porsche]  ...  [2.0, 1.8, 6.0]

print(result)

