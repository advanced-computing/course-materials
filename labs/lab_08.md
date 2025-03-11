# Lab 8

**Objective:** Understand different methods of loading data

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

- You'll set up scripts to perform each of the [methods of data loading](#data-loading) into DuckDB.
- You'll [pair](../docs/pairing.md) in your Lab group.
- Work on branches and submit pull requests for the chunks of work — you decide what the "chunks" are.

---

### Steps

1. Write out the usage and manual testing instructions as Markdown.
   - We're doing this as [documentation-driven development](https://gist.github.com/zsup/9434452).
   - What should the user expect to see in the table after running each script?
1. Prepare your datasets for [each method of data loading](#data-loading).
1. Work through [each method of data loading](#data-loading).
   - Feel free to manually copy/alter your data file(s) as needed.
   - Include the type in the scripts and table names to keep them separate — something like:
     - `_append`
     - `_trunc`
     - `_inc`
1. [Submit the links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)

---

### Hints

<details>
  <summary>For append and trunc-and-load</summary>
  <ul>
    <li>Make a copy of your data file and adjust the values manually.</li>
    <li>Use dates as part of the filenames to separate them.</li>
    <li>The table should look the same after each time you run the script.</li>
  </ul>
</details>

<details>
  <summary>For incremental</summary>
  <ul>
    <li>You'll want to split your data files into overlapping chunks.</li>
    <li>Your script will need to know what data has been loaded in order to avoid re-inserting existing data.</li>
    <li>A Python script may be easier than a SQL one.</li>
  </ul>
</details>
