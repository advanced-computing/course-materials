# Lecture 7

**Databases**

---

## [Project](../docs/project.md) evolution

Each Project Part is a baseline; you'll probably need to do more than that to get to the [end result](../docs/project.md#by-the-end).

---

## [Open Data Week](https://opendataweek.nyc/)

- [School of Data](https://schoolofdata.nyc/)
  - Strongly recommend
  - Early-bird ticket sales end today
  - As a sweetener: [I'm showing a policy-related dance-theater piece on the Sunday (UnSchool of Data)](https://nycsodata26.sched.com/event/2I1wy/pre-existing-conditions-performance-and-group-discussion-on-healthcare-in-america) 🕺
- You'll be required to attend at least one event.
  - Doesn't need to be (Un)School of Data.

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

Recommend installing through a [system package manager](../readings/week_04.md#setup). If you have any trouble, the default instructions are fine.

---

## Example

1. Go to this [dataset page](https://databank.worldbank.org/source/sustainable-energy-for-all).
   - Country: Select all (☑️)
   - Series: Access to electricity (% of total population)
   - Time: Select all (☑️)
1. Download and unzip as a CSV.
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

## [Reading response questions](https://edstem.org/us/courses/89925/discussion/7737019)

### Code Quality

- At what point does adding more code quality tools (linters, formatters, type checkers) improve productivity, and when might it slow development?
- At what point does separating code into modules become fragmentation, and how do you decide **where one module ends and another begins**?

---

### Databases

- **When is Pandas used vs SQL used**? What are the advantages/disadvantages of both? I’ve noticed that many dbs use SQL instead of pandas.
- In our quant class, we learn that R is widely used in social science research for statistical analysis. **How do these languages typically work together in real data systems?** Also, if these large data systems combine multiple languages, does relying on multiple languages make such systems harder to maintain?
