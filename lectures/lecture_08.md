# Lecture 8

**Data warehousing**

---

## [Retro](../docs/project.md#retro)

Anything you'd like to share?

---

## Data loading

- Append load
- Trunc(ate) and load
- Incremental load

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

Let's say you were given access to a random table that uses one of the [three data loading methods above](#data-loading). How would you tell which it was?

---

### Incremental load

The trick is avoiding duplicates. Your script might then need to say something like:

1. What's the latest timestamp in the database?
1. Pull data from the API that's more recent than that.

---

## [Transactions](https://duckdb.org/docs/stable/sql/statements/transactions.html)

```sql
BEGIN TRANSACTION;
INSERT INTO ...;
COMMIT;
```

---

## Revisiting the [Project](../docs/project.md) goals

---

## Why use a database?

---

## Data engineering

---

### [Overview](https://docs.google.com/presentation/d/1Q7Oe3CtLo4NuB4gCHPg4v-okfraLvAeVQWLZPAtejCA/edit)

<!-- using Google Slides because it was easier to do diagrams/transitions there -->

---

### [Example](https://docs.google.com/presentation/d/1-dr8oT9QsjrimhrFPiJQqDI91rMK28HZRsnx9wjGwlw/edit)

---

## [Project arc](../docs/project.md)

---

### [Check-in](../docs/project.md#check-in)

---

## [Project Part 5](../docs/project.md#part-5)

---

### [Example](../examples/bigquery/query.py)
