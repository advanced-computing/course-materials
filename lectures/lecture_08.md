# Lecture 8

---

## Guest speaker

[John Paul Farmer](https://www.linkedin.com/in/johnpaulfarmer)

---

## [Retro](../docs/project.md#retro)

Anything you'd like to share?

---

## Data warehousing

---

## Tracking loads

It can be helpful to track the load information for each row. These might be things like:

- `_LOADED_FROM`: filename, if applicable
- `_LOADED_AT`: timestamp

---

"Give me the data from the most recent load"

---

### DuckDB example

#### Create

```sql
CREATE TABLE my_table AS
SELECT
   *,
   current_localtimestamp() AS _LOADED_AT,
   filename AS _LOADED_FROM
FROM read_csv('[path]', filename=true);
```

---

#### Subsequent loads

```sql
INSERT INTO my_table
SELECT
   *,
   current_localtimestamp() AS _LOADED_AT,
   filename AS _LOADED_FROM
FROM read_csv('[path]', filename=true);
```

---

You can imagine the equivalent in a DataFrame.

---

### Retrieving the latest load

```sql
SELECT *
FROM my_table
WHERE _LOADED_AT = (SELECT MAX(_LOADED_AT) FROM my_table);
```

---

## [Transactions](https://duckdb.org/docs/stable/sql/statements/transactions.html)

```sql
BEGIN TRANSACTION;
INSERT INTO ...;
COMMIT;
```

---

## [Project Part 5](../docs/project.md#part-5)

---

### [Example](../examples/bigquery/query.py)
