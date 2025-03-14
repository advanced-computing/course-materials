# Lecture 8

---

## _gestures at everything_

---

## Feedback

- Getting a lot of new information
- Don't understand where we're going

---

Next lecture, we'll zoom out.

---

## Guest speaker

> [John Paul Farmer](https://www.linkedin.com/in/johnpaulfarmer) served as the 3rd Chief Technology Officer of New York City, taking point on everything from broadband to digital services to AI. Prior to that, he spent a handful of years at Microsoft, building connections with cities and the civic tech community. Previously, he was Senior Advisor for Innovation in the White House Office of Science and Technology Policy under President Obama, where he confounded and led the Presidential Innovation Fellows. He has also served as an adjunct associate professor at a Columbia and a Fellow of the University of Pennsylvania’s Institute for Urban Research. Most recently, he served as President of a next-gen broadband technology company and is now the President of Smart City Expo USA.

---

## Intros

- Name
- What you're passionate about

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
