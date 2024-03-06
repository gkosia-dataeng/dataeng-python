# %% 
import pandas as pd

df = pd.read_csv('./pokemon_data.csv')
# %%
# rows, cols
print(df.shape)
# column, #values, dtype
print(df.info())
# get columns
print(df.columns)
# get datatypes of columns
print(df.dtypes)

# get number of rows
df.index.size
df.head(3)
# %%

# 'all'
# include=[np.number] => include numeric column
# include=[object] => include only string columns
# include=['category'] => include only categorical columns
print(df.describe(include='all'))

# %%
