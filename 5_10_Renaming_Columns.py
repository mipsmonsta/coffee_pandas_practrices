import pandas as pd

df = pd.read_csv("Cars.csv")

second_df = df.copy()

df.rename(columns={"aspiration": "body_style", "body_style":"aspiration"}, inplace=True)

second_df.rename(columns={"aspiration": "body-style"}, inplace=True)
second_df.rename(columns={"body-style": "aspiration"}, inplace=True)


list1 = df.columns.to_list()
list2 = second_df.columns.to_list()

print(list1, list2)

result = list1 == list2

print(result)