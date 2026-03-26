-- this script can be run from this directory:
--
--   duckdb -init queries.sql --no-stdin world_bank.db

-- setup

CREATE OR REPLACE TABLE electricity AS
SELECT * FROM read_csv(
   "world_bank_data.csv",
   nullstr=['', '..']
);

SELECT * FROM electricity;

-- cleanup

ALTER TABLE electricity
DROP COLUMN "Time Code";

ALTER TABLE electricity
RENAME COLUMN "Access to electricity (% of total population) [1.1_ACCESS.ELECTRICITY.TOT]" TO "Percent of Pop";

DELETE FROM electricity
WHERE "Country Code" IS NULL;

-- analysis

SELECT
   "Country Name",
   ROUND(MEAN(TRY_CAST("Percent of Pop" AS FLOAT))) AS avg_pct
FROM electricity
GROUP BY "Country Name";

WITH electricity_by_country AS (
   PIVOT electricity
   ON Time
   USING first("Percent of Pop")
)
SELECT
   "Country Name",
   "2016" - "1990" as diff
FROM electricity_by_country
ORDER BY diff DESC;
