-- Connect to a new or existing DuckDB database file
-- This creates the file if it doesn't exist
ATTACH DATABASE 'world_bank.db' AS mydb;

-- Create table in this persistent database
CREATE TABLE mydb.electricity AS SELECT * FROM read_csv("world_bank_data.csv");
