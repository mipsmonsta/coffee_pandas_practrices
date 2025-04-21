import pandas as pd

names = ['Alice', 'Bob', 'Clarisse', 'Dagobert']
ages = [20, 53, 42, 23]
data = list(zip(names, ages)) # list of tuples

df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'], columns=['Name', 'Age'])

result = df.loc['C', 'Age']

print(result)
