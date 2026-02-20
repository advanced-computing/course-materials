# Lab 5

## Goal

Get hands-on experience with:

- Unit testing
- Data profiling
- Data quality checks

---

## Announcements

- [Aidan responded to survey feedback](https://edstem.org/us/courses/89925/discussion/7698376)
- We saw [requests on the GitHub Organization](https://github.com/organizations/advanced-computing/settings/member_feature_requests), but it doesn't say from whom.
  - Custom repository roles: Not sure what this was for. Please post on Ed if you need something about your repositories adjusted.
  - Copilot: [How to get it](https://edstem.org/us/courses/89925/discussion/7702140)

---

## Data cleaning

_All together_

<!-- intentionally vague -->

We're going to be creating a `parse_dollars()` function. It should accept a Series as an argument and return a new Series.

1. Come up with test cases.
   - Example inputs → expected outputs/result
1. Convert those to pytest.
   - Don't write `parse_dollars()` yet!
1. Run the tests, confirm they fail.
1. Write `parse_dollars()`, making tests pass.

---

[Solution](../examples/profiling/)

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
