import pandas as pd

data = {}

idx = range(1, 11)
for i in range(1, 11):
    column = pd.Series(range(i, i*10 + 1, i), index=idx) 
    data[i] = column

mult_table = pd.DataFrame(data, index=range(1, 11)) # multiplication table
result = mult_table.loc[4, 5]

print(result)
print(mult_table)