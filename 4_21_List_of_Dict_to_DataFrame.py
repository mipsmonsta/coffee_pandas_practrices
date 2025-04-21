import pandas as pd

data = [
    {'Car':'Mercedes', 'Driver':'Hamilton, Lewis'},
    {'Car': 'Ferrari', 'Driver':'Schumacher, Michael'},
    {'Car': 'Lamborghini'}
]

df = pd.DataFrame(data, index=['Rank 2', 'Rank 1', 'Rank 3'])
df.sort_index(inplace=True)
result = df['Car'].iloc[0]

print(result)