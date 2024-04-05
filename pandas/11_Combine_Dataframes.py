import pandas as pd


# combine columns
pd.concat([df1,df2],axis=1)

# combine rows, colunms that does not exists in one df will be null 
pd.concat([df1,df2],axis=0)

# join two dataframes
df_merge = pd.merge(
            df_c, df_l, how="left", left_on="user_id", right_on="user_id"
        )