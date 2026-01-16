# Lab 10

**Goals:**

- Think through data loading for different data sources
- Ensure your app is performant

---

Work in your [Project team](../semesters/spring_2026/roster.csv).

---

## All data in BigQuery

Use BigQuery for _all_ your datasets. For each data source:

1. What type of [data loading](lab_08.md#data-loading) will you use? Why? Explain as Markdown in your repository.
1. Repeat the middle steps from [Part 5](../docs/project.md#part-5).

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

### Record

Make a screen recording starting your app locally, then loading each page in real time. Some options for recording:

- [Mac](https://support.apple.com/en-us/102618)
- [Windows](https://www.microsoft.com/en-us/windows/learning-center/how-to-record-screen-windows-11)
- [Zoom](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059856)

---

## Submit

[Submit via CourseWorks:](https://courseworks2.columbia.edu/courses/233896/assignments)

- Links to the pull request(s)
- The screen recording
