# get rows with any column null
df.isnull()

# get rows with null on a specific column
df[df["name"].isnull()]

# drop rows with any column null
df.droopna()

# drop rows with at least 3 columns null
df.dropna(thresh=3)

# fill nulls
df.fillna("missing")

# fill specific column nulls
df["name"].fillna("missing")

