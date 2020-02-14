from pathlib import Path

import pandas as pd
#%%
df = pd.read_csv(Path().joinpath('transactions.csv'))
#%%
# path = '/home/ubuntu/Downloads/Data_analytics/assaignment_01/transactions.csv'
# df = pd.read_csv(path)
# df.head(10)
#%%
df.info()

#%%
df.head(10)
#%%
df.isnull().sum()
#%%
print('hey') #whatsup
