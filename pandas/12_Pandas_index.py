# %% 
import pandas as pd
import numpy as np

df = pd.read_csv('./pokemon_data.csv')
df.head(3)
# %%

# when filtering out rows the index remain the old 
df[df["Type 1"] != "Grass"]

# to reset the index based on new set
# reset_index will place as column the old index
# to drop old index drop=True
df.reset_index(drop=True)

