import pandas as pd
import duckdb

conn = duckdb.connect(database=':memory:')

prod_file_path = '../data/2024-07-22_prod.json'
stage_file_path = '../data/2024-07-22_dryrun.json'

transactions_file_path = '../data/tax_on_transactions.json'

conn.execute(f""" 
    CREATE TABLE prod_wht AS
    SELECT 
         json_extract(value, '$.serverId')      as serverId
        ,json_extract(value, '$.login')         as login
        ,json_extract(value, '$.dealPosition')  as dealPosition
        ,json_extract(value, '$.dealId')        as dealId
        ,json_extract(value, '$.taxAmount')     as taxAmount
        ,json_extract(value, '$.executionTime') as executionTime
        ,json_extract(value, '$.profit')        as profit
        ,json_extract(value, '$.commission')    as commission
    FROM read_json_auto('{prod_file_path}')
""")


conn.execute(f""" 
    CREATE TABLE stage_wht AS
    SELECT 
         json_extract(value, '$.serverId')      as serverId
        ,json_extract(value, '$.login')         as login
        ,json_extract(value, '$.dealPosition')  as dealPosition
        ,json_extract(value, '$.dealId')        as dealId
        ,json_extract(value, '$.taxAmount')     as taxAmount
        ,json_extract(value, '$.executionTime') as executionTime
        ,json_extract(value, '$.profit')        as profit
        ,json_extract(value, '$.commission')    as commission
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
'''

conn.execute("""COPY (
                        SELECT 
                                serverId
                                ,login
                                ,dealPosition
                                ,dealId
                                ,profit
                                ,commission
                                ,taxAmount
                        FROM stage_wht
             ) TO 'dry_run.csv' (HEADER, DELIMITER ',') """)


conn.execute("""COPY (
                        SELECT 
                                serverId
                                ,login
                                ,dealPosition
                                ,dealId
                                ,profit
                                ,commission
                                ,taxAmount
                        FROM prod_wht
             )  TO 'prod.csv' (HEADER, DELIMITER ',') """)

'''

'''
    Load transactions topic 
'''
conn.execute(f""" 
    CREATE TABLE dryrun_transactions AS
    SELECT 
         json_extract(value, '$.server')        as serverId
        ,json_extract(value, '$.login')         as login
        ,json_extract(value, '$.dealID')        as dealId
        ,json_extract(value, '$.amount')        as amount
        ,json_extract(value, '$.taxAmount')     as taxAmount
        ,json_extract(value, '$.comment')       as comment
        ,TO_TIMESTAMP(CAST(json_extract(value, '$.executionTimestamp') AS BIGINT) /1000) as executionTimestamp
        
             
    FROM read_json_auto('{transactions_file_path}')
""")



conn.execute("""COPY (
                        SELECT 
                                *
                        FROM dryrun_transactions
             ) TO 'dry_run_transactions.csv' (HEADER, DELIMITER ',') """)