from pathlib import Path
import pandas as pd
#%%
# fancy way to load data
df = pd.read_csv(Path().joinpath('transactions.csv'))
#%%
# another way to load data
# path = '/home/ubuntu/Downloads/Data_analytics/assaignment_01/transactions.csv'
# df = pd.read_csv(path)
# df.head(10)
#%%
# to look into the data
df.info()
#%%
df.head(10)
#%%
df.isnull().sum()
#%%
df.tail(10)
