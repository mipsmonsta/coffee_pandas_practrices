import pandas as pd

data = [
    ['apple', 1.0],
    ['bread', 2.5],
    ['egg', 0.25],
]

df = pd.DataFrame(data, columns=['Item','Price'])
shopping_list = pd.Series([5, 1, 4])
result = (df['Price'] * shopping_list).sum()

print(result)