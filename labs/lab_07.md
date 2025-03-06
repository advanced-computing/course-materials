# Lab 7

## Objective

Get experience writing data to and reading data from a database

---

## Database CLI usage

Can use the CLI for DuckDB (and other databases):

- [Interactively](https://duckdb.org/docs/stable/clients/cli/overview#running-sql-statements-in-the-cli)
- By [having it execute a SQL script](https://duckdb.org/docs/stable/clients/cli/overview#non-interactive-usage)

---

You'll [pair](../docs/pairing.md) in your group, repository, and dataset from Labs [4](lab_04.md) and [5](lab_05.md). Work on branches and submit pull requests for the chunks of work — you decide what the "chunks" are.

---

## Steps

You'll be changing your API over to use DuckDB.

1. Install the [Python client](https://duckdb.org/docs/stable/clients/python/overview#installation).
1. Create a SQL script to take data from your CSV file and write it to a [persistent database](https://duckdb.org/docs/stable/clients/python/overview#persistent-storage).
1. Update your API to read from the database.
1. [Submit via CourseWorks](https://courseworks2.columbia.edu/courses/210480/assignments):
   - Links to the pull request(s)
   - A [screenshot](https://www.take-a-screenshot.org/) showing data in your database
