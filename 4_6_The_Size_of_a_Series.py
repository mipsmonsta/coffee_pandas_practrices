import pandas as pd

data = [1,2,3,5,7,9,11]
index = [2, 4, 6, 8, 10, 12, 14]

primes = pd.Series(data, index)
result = primes.size

print(result)