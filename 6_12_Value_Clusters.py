import pandas as pd
import numpy as np

df = pd.read_csv("Cars.csv")

bins = np.linspace(min(df['price']), max(df['price']), 4)

#  The lowest value of the pair does not belong to the bin;
#  the highest value does. Except for the first bin where both values
#  are included because of the argument include_lowest=True.
df['price-category'] = pd.cut(df['price'], bins, 
                              labels=["Low", "Medium", "High"], 
                              include_lowest=True)
print(df)
print(len(df[df["price-category"] == "Medium"]))