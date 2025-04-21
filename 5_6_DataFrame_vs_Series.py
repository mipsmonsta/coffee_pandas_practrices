import pandas as pd

dict_ = {1: ["a"], 2: ["b"], 3: ["c"]}

result1 = pd.Series(dict_)
result2 = pd.DataFrame(dict_)

print(result1)
print(result2)

print(len(result1) == len(result2))