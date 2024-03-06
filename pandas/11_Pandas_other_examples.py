import pandas as pd

# join two dataframes
df_merge = pd.merge(
            df_c, df_l, how="left", left_on="user_id", right_on="user_id"
        )

# drop duplicates
cf_l = cf_l.drop_duplicates(subset=['user'], keep='last')

# partition by user lag profit
df_c["val_prev"] = df_c.groupby("user_id").profit.shift(1)

# partition by user cumm sum
 df_c["cumm_tax"] = df_c.groupby(["user_id"])["taxes"].cumsum()

