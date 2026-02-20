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

Install the [Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) VSCode extension.

---

### Data quality checks

- Unit tests for data
- [Things to check for when cleaning data](https://computing-in-context.afeld.me/lecture-18/#data-cleaning)
- Can be flexible, like checking for:
  - Standard deviation being in a certain range
  - X% of values matching certain criteria
- There are commercial tools that help with this - we're going to write the code ourselves.

---

Look around your data profiling report. **Write takeaways of five findings** that seem relevant to your analysis. This can be done in a Markdown file or a Jupyter notebook in your repository.

---

Using the profile information, **write data quality checks for three of the [things to check for](https://computing-in-context.afeld.me/lecture-18/#things-to-check-for)** with pytest. The pandas documentation around [comparing if objects are equivalent](https://pandas.pydata.org/docs/user_guide/basics.html#comparing-if-objects-are-equivalent) will be helpful.

---

## Submit

[Submit the links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)
