import duckdb

con = duckdb.connect(database=':memory:')
con.execute("CREATE TABLE items (name VARCHAR, price DECIMAL);")
con.execute("INSERT INTO items VALUES ('apple', 1.0), ('banana', 2.0), ('cherry', 3.0);")
result = con.execute("SELECT * FROM items;")
print(result.fetchdf())