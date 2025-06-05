import numpy as np 
import pandas as pd
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df['W'])
print(type(df['W']))
df['New'] =df['W'] + df['Y']
print(df)
print(df[['W','Y']])
df.loc['A']
print(df.loc['A'])
df.iloc[2]
print(df.iloc[2])

print(df.iloc[['A','B'],['W','Y']])
print(df.loc['A':'C','W':'Y'])