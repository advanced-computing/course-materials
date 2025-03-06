# Lecture 7 - IN PROGRESS

**Databases**

---

### Complexity

_Carry-over from [lecture 6](lecture_06.md)_

- [Types](https://en.wikipedia.org/wiki/Programming_complexity#Types)
- [Cyclomatic measurement](https://en.wikipedia.org/wiki/Cyclomatic_complexity)

---

Who has experience with SQL? What have you used it for?

---

## [SQLite](https://www.sqlite.org/)

---

## [DuckDB](https://duckdb.org/)

---

### [Install the command-line tool](https://duckdb.org/docs/installation/?version=stable&environment=cli)

- **Mac:** Assuming you have [Homebrew set up](../readings/week_04.md#setup), use the "package manager" option.
- **Windows:** [Not available](https://github.com/chocolatey-community/chocolatey-package-requests/issues/1583) for [Chocolatey](https://chocolatey.org/) yet, so probably easiest to do the "direct download".

---

### Example

1. Download the [access to electricity dataset](https://databank.worldbank.org/reports.aspx?dsid=2&series=EG.ELC.ACCS.ZS#) as a CSV.
1. Query it.

   ```sql
   SELECT * FROM read_csv('[path].csv');
   ```

---

#### [Specify null values](https://duckdb.org/docs/stable/data/csv/overview.html#parameters)

```sql
SELECT * FROM read_csv(
   '[path].csv',
   nullstr=['', '..']
);
```

---

### [Create a table](https://duckdb.org/docs/stable/data/csv/overview.html)

```sql
CREATE TABLE electricity AS
SELECT * FROM read_csv(
   '[path].csv',
   nullstr=['', '..']
);
```

---

What's a question we might want to ask?

---

```sql
SELECT
   "Country name",
   "2022 [YR2022]" - "1990 [YR1990]" AS diff
FROM electricity
ORDER BY diff DESC;
```

---

## [BigQuery](https://cloud.google.com/bigquery)
