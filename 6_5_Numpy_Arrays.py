import pandas as pd
import numpy as np

a = pd.array([0,1,2,3])
b = np.array([0, 1, 2, 3])
c = a == b
print(c.all())