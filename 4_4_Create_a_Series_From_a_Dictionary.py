import pandas as pd

salary = {'Alice':1000, 'Bob':750, 'Carol':1250}
salary_series = pd.Series(salary)
result = salary_series.index[1]

print(result) # 'Bob'
print(salary_series.values[2]) # 1250\
print(salary_series)
print(salary_series.shape)