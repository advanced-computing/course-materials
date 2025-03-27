# Lab 10

**Objectives:**

- Think through data loading for different data sources
- Ensure your app is performant

---

Work in your [Project team](../docs/project_teams.csv).

---

## All data in BigQuery

Use BigQuery for _all_ your datasets. For each data source:

1. What type of [data loading](lab_08.md#data-loading) will you use? Why? Explain as Markdown in your repository.
1. Repeat the middle steps from [Part 5](../docs/project.md#part-5).
   - Doesn't necessarily need to be [incremental](lab_08.md#incremental-load).

---

## Performance

Ensure each page of your app (if there are multiple) fully loads within two seconds.

- You can use [caching in Streamlit](https://docs.streamlit.io/develop/concepts/architecture/caching), but don't rely on that exclusively.
- [Timing Function[s] in Python](https://builtin.com/articles/timing-functions-python) can help you identify where the slowdown(s) are.

<details>
   <summary>Hint</summary>
   You may need to push logic/filtering from pandas to SQL to reduce the number of records that need to be loaded from the database by your app.
</details>

---

[Submit links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)
