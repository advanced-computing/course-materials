# Lab 4

**Goal:** Better understand APIs by building one

---

## The task

You will build an API using [Flask](https://flask.palletsprojects.com/). Example APIs:

- [OpenFEC](https://api.open.fec.gov/developers/)
- [Socrata Open Data Consumer API (SODA)](https://dev.socrata.com/consumers/getting-started.html)

We will be practicing [pair programming](../docs/pairing.md) and [documentation-driven development](https://gist.github.com/zsup/9434452). You'll get as far as you can during the Lab session, then continue the rest outside.

---

## Steps

### Setup

1. Pair up with someone who isn't on your [project team](../docs/project.md#teams).
   - This will be known as your "Lab group". Subsequent Labs will use the same people, repository, and dataset.
1. Pick a dataset that has unique identifiers for each row.
   - You can use a dataset from one of your [projects](../docs/project.md), or [pick a different one](https://python-public-policy.afeld.me/en/columbia/assignments/open_ended.html#open-data-portals).
   - You'll use a CSV as the data source to power your API.
   - Don't spend too long on this step.
1. [Create a public repository in the `advanced-computing` organization.](https://github.com/new?owner=advanced-computing&visibility=public)
   - Call it something like `[name1]-[name2]-api`.
   - Make sure to grant collaborator access to your partner.
1. Create a README that will describe how to use your forthcoming API.

---

### Build

For each step, you will:

1. Document the functionality. Include:
   - Options, if applicable
   - Sample output
1. Build it.
1. Test it.

The documentation is a starting place; you can add/modify as you go.

For inspiration, check out [the example](examples/lab_04/).

---

_Suggested order_

Allow the user to:

1. List records
   - You can start with CSV or JSON output; you will implement the other later.
   - <details><summary>Hints</summary>
      <ul>
         <li>See <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html"><code>to_csv()</code></a> and <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html"><code>to_json()</code></a>.</li>
         <li>"If [the path is] None, the result is returned as a string."</li>
      <ul>
     </details>
1. Filter the data based on a particular column, such as `age=30`
1. Specify a `limit` and `offset`
1. Retrieve a single record by identifier
1. Specify the output format (CSV or JSON)

[**Submit** via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)
