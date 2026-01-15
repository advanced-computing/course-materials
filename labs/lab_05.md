# Lab 5

## Goal

Get hands-on experience with:

- Unit testing
- Data profiling
- Data quality checks

---

## Data cleaning

_All together_

1. Add tests for parsing the dollar amount
1. Refactor the code
   - Modules and `import`
1. Make them pass

---

Code needs to be testable. This encourages good habits, like:

- Ensuring your code can change without unexpected breakage
- Making small, reusable functions with well-defined behavior
- Organizing code into modules
- Allowing the loading of a module without running all the code

---

## Code organization

Seeing projects with `<name>2.py`. Splitting code up into smaller files will help you work in parallel without stepping on each others' toes.

---

## Steps

You'll [pair](../docs/pairing.md) in your Lab group. Work on branches and submit pull requests for the chunks of work — you decide what the "chunks" are.

---

### Data profiling

[**Set up YData Profiling**](../examples/profiling/profiling.ipynb#ydata-profiling) for your dataset. If it's slow, see [their documentation on profiling large datasets](https://docs.profiling.ydata.ai/latest/features/big_data/).

---

At time of writing, [YData Profiling is only compatible with Python 3.13 and below](https://github.com/ydataai/ydata-profiling/pull/1804). If you're on Python 3.14+, the easiest thing will be to run the profiling in [Colab](https://colab.research.google.com/) and include a link to that notebook. Install the package there with:

```sh
!pip install ydata-profiling
```

---

### Data quality checks

- Unit tests for data
- [Things to check for when cleaning data](https://computing-in-context.afeld.me/lecture_17.html#data-cleaning)
- Can be flexible, like checking for:
  - Standard deviation being in a certain range
  - X% of values matching certain criteria
- There are commercial tools that help with this - we're going to write the code ourselves.

---

Look around your data profiling report. Using that information, **write data quality checks for three of the [things to check for](https://computing-in-context.afeld.me/lecture_17.html#things-to-check-for)** with pytest. The pandas documentation around [comparing if objects are equivalent](https://pandas.pydata.org/docs/user_guide/basics.html#comparing-if-objects-are-equivalent) will be helpful.

---

## Submit

[Submit the links to the pull requests via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)
