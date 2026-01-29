# Lab 2

---

## Goals

Students:

- refresh their memories on working with Jupyter and pandas
- get practice with pagination and concatenation of datasets

---

## Steps

We'll be doing this lab as pair programming, with the TA floating around to help.

---

### Full class together

1. Go over [pair programming](../docs/pairing.md).
1. Talk through the steps below.
1. Set up groups with different people than the [project teams](../semesters/spring_2026/people.csv).

---

### In groups

Students can look back at the [Computing in Context slides](https://computing-in-context.afeld.me/#schedule) if needed.

1. One person in each group, create a new notebook in [Google Colab](https://colab.research.google.com/).
   1. Add everyone's name.
   1. Share it with your teammate(s).
1. [Load](https://python-public-policy.afeld.me/en/columbia/assignments/open_ended.html#storing-data) the [NYPD Hate Crime data](https://data.cityofnewyork.us/Public-Safety/NYPD-Hate-Crimes/bqiq-cu78/about_data) into pandas.
1. Confirm how many records have been loaded.
1. Compute an aggregate statistic (mean, median, sum, whatever).
1. Create a visualization.
   - Keep it simple.
1. Switch to getting the data from the API.
1. Check how many records the API is returning.
1. Get the full dataset using pagination.
   - Useful resources:
     - [Socrata API: Paging through Data](https://dev.socrata.com/docs/queries/page.html)
     - [Requests package: Passing Parameters In URLs](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls)
     - [pandas: `concat()`](https://pandas.pydata.org/docs/user_guide/merging.html#concat)
   - Restriction for this lab: Page size shouldn't be set greater than `1000`.
1. Check how many results you get total, confirm it matches what's in the data portal.
1. Do the aggregate statistic and visualization using the expanded dataset and note how they've changed.
1. [Submit via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)
