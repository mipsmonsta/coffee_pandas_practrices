import pandas as pd

cars = pd.read_csv('cars.csv')
print(cars)
result = cars['make'].values[-1]
print(result)