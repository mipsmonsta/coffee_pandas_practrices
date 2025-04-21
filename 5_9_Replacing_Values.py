import pandas as pd

df = pd.read_csv("Cars.csv")

other_df = df.copy()

df["aspiration"] = df["aspiration"].replace("std", "standard")
list1 = df["aspiration"].to_list()

other_df["aspiration"] = other_df["aspiration"].replace("std", "standard")
list2 = other_df["aspiration"].to_list()

result = list1 == list2


print(result)