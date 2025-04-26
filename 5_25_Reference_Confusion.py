import pandas as pd

df = pd.read_csv("Cars.csv")

second_df = df # using a reference
third_df = df.copy()
df.drop("fuel", axis= 1, inplace=True)
result = second_df.columns[1] == third_df.columns[1]
print(result) # false