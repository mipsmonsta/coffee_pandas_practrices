import pandas as pd

df = pd.read_csv("Cars.csv")
temp = pd.get_dummies(df["aspiration"])
temp.rename(columns= {"std": "aspiration-std", "turbo": "aspiration-turbo"}, inplace=True)
df = pd.concat([df, temp], axis=1)

print(df["aspiration-std"].sum(), df["aspiration-turbo"].sum())