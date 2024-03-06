import  polars as pl


file  = './data/__mharrison__2020-2021.csv'

df = pl.read_csv(file)

# methods of dataframe
print(dir(df))

# methods of column of dataframe
dir(pl.col('foo'))


#explore data
df.columns
df.shape
df.dtypes # pyarrow types

#get a sample
df.sample(20)
df.estimated_size()

# summary statistics
print(df.describe())