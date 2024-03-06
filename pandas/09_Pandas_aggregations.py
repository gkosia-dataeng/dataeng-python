# %% 
import pandas as pd
import numpy as np

df = pd.read_csv('./pokemon_data.csv')
df.head(3)
# %%

# aggregate without rename columns
df.groupby('Type 1',as_index=False).agg({
     'HP': max
    ,'Attack': sum
}).head(10)
# %%
# aggregate with rename 
df.groupby('Type 1',as_index=False).agg(
     max_hp = ('HP', 'max')
    ,sum_attack = ('Attack', 'sum'))
# %%
