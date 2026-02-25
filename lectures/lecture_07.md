# Lecture 7

**Databases**

---

## Packages

Whenever documentation says `pip install …`, you probably want to add it to your `requirements.txt`.

---

## SQL

Who has experience with SQL? What have you used it for?

---

## [SQLite](https://www.sqlite.org/)

---

## [DuckDB](https://duckdb.org/)

---

SQL syntax is largely the same across SQL databases:

- SQLite
- DuckDB
- PostgreSQL
- MySQL
- BigQuery
- Oracle
- …

The variations are known as "dialects".

---

### [Install the command-line tool](https://duckdb.org/docs/installation/?version=stable&environment=cli)

- **Mac:** Assuming you have [Homebrew set up](../readings/week_04.md#setup), use the "package manager" option.
- **Windows:** [Not available](https://github.com/chocolatey-community/chocolatey-package-requests/issues/1583) for [Chocolatey](https://chocolatey.org/) yet, so probably easiest to do the "direct download".

---

## Example

1. Download and unzip the [access to electricity dataset](https://databank.worldbank.org/reports.aspx?dsid=2&series=EG.ELC.ACCS.ZS#) as a CSV.
1. Query it.

   ```sql
   SELECT * FROM read_csv('[path].csv');
   ```

---

### [Specify null values](https://duckdb.org/docs/stable/data/csv/overview.html#parameters)

```sql
SELECT * FROM read_csv(
   '[path].csv',
   nullstr=['', '..']
);
```

---

### [Create a table](https://duckdb.org/docs/stable/data/csv/overview.html)

```sql
CREATE TABLE electricity AS SELECT ...;
```

---

What's a question we might want to ask?

---

[Column names with spaces need double quotes.](https://duckdb.org/docs/stable/sql/dialect/keywords_and_identifiers.html#identifiers) Alternatively, [`normalize_names`](https://duckdb.org/docs/stable/data/csv/overview.html#parameters).

---

```sql
SELECT
   "Country name",
   "2022 [YR2022]" - "1990 [YR1990]" AS diff
FROM electricity
ORDER BY diff DESC;
```

---

## SQL similarities to pandas

- Tabular
- DuckDB: `read_csv()`
- Tables are like DataFrames
- Columns have types
- Column-based operations
- `SELECT` is like boolean indexing
- `GROUP BY` is like `groupby()`

---

pandas allows you to build up operations over multiple lines; harder to do that in SQL.

---

## Views

---

## Clients

---

Lots of ways to connect to databases from Python, including:

- [pandas](https://pandas.pydata.org/docs/user_guide/io.html#sql-queries)
- [SQLAlchemy](https://www.sqlalchemy.org/)
  - Object Relational Mapper (ORM)

---

### Drivers

Allow you to use the same Python syntax across databases

---

## Writing data

How would you take data from an API and get it into a database?

---

### [Individual `INSERT`s](https://duckdb.org/docs/stable/clients/python/overview#persistent-storage)

---

#### [Loops](../examples/duck_loop.py)

---

### [Writing from a DataFrame](https://duckdb.org/docs/stable/guides/python/import_pandas.html)

---

## [BigQuery](https://cloud.google.com/bigquery)

---

1. In the [Google Cloud Console](https://console.cloud.google.com/), [make sure your Project is selected](../docs/google_cloud.md#switching-to-your-google-cloud-project).
1. Open [BigQuery](https://console.cloud.google.com/bigquery).
1. [Enable the API.](https://cloud.google.com/apis/docs/getting-started#enabling_apis)
1. [Open a public dataset.](https://cloud.google.com/bigquery/docs/quickstarts/query-public-dataset-console#open_a_public_dataset)
   - Try `Category` of `Economics` and `Price` of `Free`

---

```sql
SELECT company_name, COUNT(*) AS num_complaints
FROM `bigquery-public-data.cfpb_complaints.complaint_database`
GROUP BY company_name
ORDER BY num_complaints DESC;
```

---

## Readings

Coming soon
