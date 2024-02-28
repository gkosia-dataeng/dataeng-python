import  polars as pl

# %%
file  = './data/__mharrison__2020-2021.csv'

df = pl.read_csv(file)

# methods of dataframe
print(dir(df))

# methods of column of dataframe
print(dir(df.col('foo')))


#explore data
