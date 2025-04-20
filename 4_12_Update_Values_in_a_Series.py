import pandas as pd

cities = {1111: 'New York', 2222:'Marseille', 3333:'Warsaw'}
zips = pd.Series(data=cities)
zips = zips.apply(lambda x: x.upper()) # update the values of series but not in placed.

result = zips.loc[2222]
print(result)

print(zips)
result2 = zips.iloc[2]
print(result2)

cities2 = pd.Series(data=cities.values(), index=cities.keys())
print(cities2)
result3 = cities2.iloc[0]
print(result3)
result4 = cities2.loc[[True, False, True]]
print(result4)