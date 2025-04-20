import pandas as pd
import numpy as np

data = pd.Series([0, np.nan, 2]) # np.NaN was deprecated, use np.nan
result = data.hasnans

print(result)