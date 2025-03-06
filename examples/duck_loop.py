"""copied from https://duckdb.org/docs/stable/clients/python/overview#persistent-storage"""

import duckdb

# create a connection to a file called 'file.db'
con = duckdb.connect("file.db")
# create a table and load data into it
# con.sql("CREATE TABLE test (i INTEGER)")
for i in range(0, 10):
    con.sql(f"INSERT INTO test VALUES ({i})")
# query the table
con.table("test").show()
# explicitly close the connection
con.close()
# Note: connections also closed implicitly when they go out of scope
