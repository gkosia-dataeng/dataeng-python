import pandas as pd



# drop duplicates
cf_l = cf_l.drop_duplicates(subset=['user'], keep='last')

# partition by user lag profit
df_c["val_prev"] = df_c.groupby("user_id").profit.shift(1)

# partition by user cumm sum
 df_c["cumm_tax"] = df_c.groupby(["user_id"])["taxes"].cumsum()

# n largest,nsmallest
df.nlargest(5, "colname")

# rows between range
df[df["size"].between(10,30,inclusive=True)]