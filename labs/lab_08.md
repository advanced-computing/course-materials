# Lab 8

**Goal:** Understand different methods of loading data

---

## Data loading

- Append load
- Trunc(ate) and load
- Incremental load

---

Let's say you were given access to a random table that uses one of the three data loading methods above. How would you tell which it was?

---

### Incremental load

The trick is avoiding duplicates. Your script might then need to say something like:

1. What's the latest timestamp in the database?
1. Pull data from the API that's more recent than that.

---

## Lab work

- You'll write methods to load continuously updated data into a database.
  - You'll set up scripts to perform each of the [methods of data loading](#data-loading) into DuckDB.
- You'll [pair](../docs/pairing.md) in your Lab group.
- Work on branches and submit pull requests for the chunks of work — you decide what the "chunks" are.

---

### Source Data

- We will be using [Consumer Price Index data](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/pcpi) from the Philadelphia Federal Reserve.
- We have monthly observations (rows) and monthly vintages (columns)

| DATE    | PCPI04M1 | PCPI04M2 | PCPI04M3 |
| ------- | -------: | -------: | -------: |
| 2003:09 |    185.0 |    185.1 |    185.1 |
| 2003:10 |    185.0 |    184.9 |    184.9 |
| 2003:11 |    184.6 |    184.6 |    184.6 |
| 2003:12 |    185.0 |    184.9 |    184.9 |
| 2004:01 |     #N/A |    185.8 |    185.8 |
| 2004:02 |     #N/A |     #N/A |    186.3 |

- A revision of past data is released in February of each year.
- A revision released in year `t` can update the values in years `t-5` to `t-1`.

---

### Tasks

Suppose your organization wants to maintain a database of CPI data

- Write a `get_latest_data` function that accepts a `pull_date` and returns the latest data available up to that date
  - For example, if the `pull_date` is 2004-01-15, the function should return the data from vintage `PCPI04M1`
- Write code that pulls the latest data at a given `pull_date` and loads it into a DuckDB database
  - You will implement each of the methods `append`, `trunc`, and `incremental`
- Loop over a range of `pull_dates` to simulate running the scripts on a daily basis
- Compare the performance of each method (consistency and speed)

---

### Steps

1. Write out the usage and manual testing instructions as Markdown.
   - We're doing this as [documentation-driven development](https://gist.github.com/zsup/9434452).
   - What should the user expect to see in the table after running each script?
2. Write the `get_latest_data` function.
   - This function should return only two columns: e.g. `dates` and `cpi`
   - All other code should interact with the source data only through this function
3. Work through [each method of data loading](#data-loading).
   - Include the type in the scripts and table names to keep them separate — something like:
     - `_append`
     - `_trunc`
     - `_inc`
   - Your code should accept a `pull_date` parameter and load the data up to that date
   - The script should be able to run multiple times without duplicating data
   - For incremental: a Python script may be easier than a SQL one
4. On a notebook: simulate your organization running the scripts on a daily basis.
   - Start from empty tables
   - Loop over a range of `pull_dates` (e.g. 2000-01-01 to 2025-02-28) to simulate running the scripts on a daily basis.
   - If the loop takes way too long, use a shorter range
   - Compare the performance of each method (data consistency and speed)
5. [Submit links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)

---

## Simplified version

This is a simpler version of the previous task. You can submit work fullfilling either version of the task.

1. Write out the usage and manual testing instructions as Markdown.
   - We're doing this as [documentation-driven development](https://gist.github.com/zsup/9434452).
   - What should the user expect to see in the table after running each script?
2. Use the data in the file [PCPI24M1.csv](../examples/lab_8/PCPI24M1.csv) to initialize your database. This file contains inflation information as available in January 2024.
   - Create a persistent database containing three tables: `cpi_append`, `cpi_trunc` and `cpi_inc`.
   - For now these three tables look the same.
3. Load additional inflation data contained in the file [PCPI25M2.csv](../examples/lab_8/PCPI25M2.csv) into your database. This file contains inflation data as available in February 2025. It contains additional observations and historical revisions with respect to the previous file.
   - Use [each method of data loading](#data-loading) to update the tables in your database.
   - Now your tables might look different.
4. Discuss how the three methods differ.
5. [Submit links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)
