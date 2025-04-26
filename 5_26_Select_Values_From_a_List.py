import pandas as pd

df = pd.read_csv("Cars.csv")

list1 = ["dodge", "audi", "volvo"]
total1 = df[df["make"].isin(list1)]["price"].sum()
total2 = df[~df["make"].isin(list1)]["price"].sum()

print(total2 - total1)