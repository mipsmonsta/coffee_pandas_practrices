import pandas as pd

data = {
    'Spain': 'Madrid',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy':'Rome',
}

capitals = pd.Series(data)
result = capitals.iloc[-1]
print(capitals)
print(result)

countries_idxs = ['Spain', 'France', 'Germany', 'Italy']
capitals_list = ['Madrid', 'Paris', 'Berlin', 'Rome']

capitals_extra = pd.Series(capitals_list, countries_idxs)

result = capitals_extra.iloc[-1]
print(capitals_extra)
print(result)