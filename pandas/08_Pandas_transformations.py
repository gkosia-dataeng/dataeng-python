# %% 
import pandas as pd
import numpy as np

df = pd.read_csv('./pokemon_data.csv')
df.head(3)

# %% 
# Calculate a new column
df["Total"] = df.iloc[:, 4:10].sum(axis=1)
df.head(3)

# %%
# Filter dataframe

# masking
print(df[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")].head(1)
)

# using query function
# with @var can import in predicate variables
ids_list = ["Grass","Ivysaur"]
print(df.query(" `Type 1` == @ids_list ")[:5])

# using np.where
msk = np.where(df["Type 1"] == "Grass")
print(df.loc[msk][:5])

# %%
# sort dataframe 
df.sort_values(["Type 1", "Type 2"],ascending=[False,False])

# %%
# is not inplace function
df.drop(["Type 1", "Type 2"],axis=1).columns

# %%
# Conditional update
# df.loc[<expression>, columns to assign value] = value
df.loc[df['Type 1']== 'Grass', ['Generation', 'Legendary']] = ['True', 'True']

df.loc[df['Type 1']== 'Grass'].head(10)
# %%
# Find missing values
df.isnull().sum()
df['Type 2'] = df['Type 2'].fillna('Na')
# %%

# Apply a function to a column
def devide_attack(attack):
    return attack / 2
df["half_attack"] = df["Attack"].map(devide_attack)
df[["half_attack", "Attack"]]
# %%

# Apply a function to a row
def process_row(row):
    return row.Attack + row.half_attack

df["attack_plus"] = df.apply(lambda x: process_row(x),axis=1)

df[["Attack", "half_attack", "attack_plus"]]
# %%
