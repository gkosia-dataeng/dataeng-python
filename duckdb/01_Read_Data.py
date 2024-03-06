import duckdb
import pandas

# connect method will create a database in-memory
# if a path exists in parameter duckdb will materialize the data in the file
# if does not provide a path the data will be lost when the connection close
# second parameter is the read_only=True if i want to access the database file from other processes
conn = duckdb.connect()

df = conn.execute("""
        SELECT *
        FROM read_csv_auto('/home/gkosia/my-repos/dataeng-python/data/Sales_Product_Combined.csv', header=True)
        LIMIT 10
""").df()
