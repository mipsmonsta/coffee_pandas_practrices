import pandas as pd

df = pd.read_csv("Cars.csv")

df2 = df.pivot_table(index=["fuel"], 
                     values=["make", "price"], 
                     aggfunc={"price": "sum", "make":"count"}, 
                     columns=["aspiration"])
print(df2)
print(df2.shape)

#  The new index is the old fuel column, aggregation columns are
#  make and price, and the columns’ labels come from the values of
#  the column aspiration. In addition, you choose how to aggregate
#  the values—price as sum and make by concatenation