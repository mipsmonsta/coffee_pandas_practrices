import pandas as pd

snakes= ['Python', 'Cobra', 'Anaconda', 'Viper']
snakes_series = pd.Series(snakes)
result = snakes_series.values[2]

print(snakes_series)
print(result)