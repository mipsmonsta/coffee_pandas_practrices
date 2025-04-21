import pandas as pd

items = ['apple', 'bread', 'egg']
prices = [1.0, 2.5, 0.25]
data = {'item': items, 'Price':prices}

df = pd.DataFrame(data)
df['Calories'] = [100, 2500, 25]

print(df)