# Lab 10

**Goals:**

- Think through data loading for different data sources
- Ensure your app is performant

---

Work in your [Project team](../docs/project.md#teams).

---

## All data in BigQuery

Use BigQuery for _all_ your datasets. For each data source:

1. What type of [data loading](../lectures/lecture_08.md#data-loading) will you use? Why? Explain as Markdown in your repository.
1. Repeat the middle steps from [Part 5](../docs/project.md#part-5).

---

## Performance

Ensure each page of your app (if there are multiple) fully loads within two seconds.

- Display the overall page load time using a [custom context manager](https://www.pythonmorsels.com/creating-a-context-manager/):

  ```python
  import time
  import streamlit as st

  @contextmanager
  def display_load_time():
      start_time = time.time()

      try:
          yield
      finally:
          elapsed = time.time() - start_time
          st.caption(f"Page loaded in {elapsed:.2f} seconds")

  with display_load_time():
      # --- your page code here ---

  ```

- [Dig into the timing even further using profiling.](https://github.com/wyattscarpenter/wfork-streamlit-profiler).
  - [How to read the results.](https://calmcode.io/course/pyinstrument/scripts)
  - Note that the `Profiler` adds overhead, so you probably don't want to leave it in your app indefinitely.
- You can use [caching in Streamlit](https://docs.streamlit.io/develop/concepts/architecture/caching).
  - Don't rely on that exclusively.
  - That won't help with initial/uncached page load.

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

- Links to the pull requests
  - Documentation updates from [Lecture 10](../lectures/lecture_10.md)
  - Code changes from above
- The screen recording
