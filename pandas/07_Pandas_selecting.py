# %% 
import pandas as pd

df = pd.read_csv('./pokemon_data.csv')
df.head(3)
# %%
# Select columns
df[["Name", "Type 1"]][0:5]

# build list of columns needed
all_cols = list(df.columns.values)
nedded_cols = all_cols[1:4] + all_cols[7:9]
print(df[nedded_cols][:5])

# select based on location
# df[r,c]
df.iloc[:5, :3]

# select based on values
df.loc[1:3, ["Name", "Type 1"]]
# find index values where type is Grass and return the rows
df.loc[df["Type 1"] == "Grass"]


# %%
# Iterate over df
for i,r in df.iterrows():
    print(i, r["Name"])
# %%
