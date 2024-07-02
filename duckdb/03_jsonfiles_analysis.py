import pandas as pd
import duckdb

conn = duckdb.connect(database=':memory:')

prod_file_path = '../data/prod_wht.json'
stage_file_path = '../data/stage_wht.json'

conn.execute(f""" 
    CREATE TABLE prod_wht AS
    SELECT 
         json_extract(value, '$.serverId')      as serverId
        ,json_extract(value, '$.login')         as login
        ,json_extract(value, '$.dealPosition')  as dealPosition
        ,json_extract(value, '$.dealId')        as dealId
        ,json_extract(value, '$.taxAmount')     as taxAmount
        ,json_extract(value, '$.executionTime') as executionTime
    FROM read_json_auto('{prod_file_path}')
""")


conn.execute(f""" 
    CREATE TABLE stage_wht AS
    SELECT 
         json_extract(value, '$.WHTEvent.serverId')      as serverId
        ,json_extract(value, '$.WHTEvent.login')         as login
        ,json_extract(value, '$.WHTEvent.dealPosition')  as dealPosition
        ,json_extract(value, '$.WHTEvent.dealId')        as dealId
        ,json_extract(value, '$.taxAmount')              as taxAmount
        ,json_extract(value, '$.WHTEvent.executionTime') as executionTime
    FROM read_json_auto('{stage_file_path}')
""")

result = conn.execute(""" 
    SELECT * , (CAST(p.taxAmount AS INT) - CAST(s.taxAmount AS INT)) as tax_diff
    FROM prod_wht as p
    FULL JOIN stage_wht AS s
     ON p.login         = s.login
    AND p.dealPosition  = s.dealPosition
    AND p.dealId        = s.dealId    
    ORDER BY  COALESCE(p.serverId, s.serverId), COALESCE(p.executionTime, s.executionTime)               
""").fetchdf()


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


print(result)