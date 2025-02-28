# Lab 6

You'll work in your [Project teams](../docs/project_teams.csv).

## Objectives

- Get ready to work in Google Cloud
- Set up continuous integration

---

## Finishing [Lab 5](lab_05.md)

- Profiling
  - Find anything surprising/interesting/useful?
- Data quality checks

---

## Linting

- A type of [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)
- Code quality
- We'll be starting with [ruff](https://docs.astral.sh/ruff/).

---

1. Install the [ruff VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).
1. Open up your Python files, you'll likely see some warnings.
   - Don't do anything with them yet.

---

## Continuous integration

You're going to set up your tests and linting to run automatically.

This is one of those times where you'll follow instructions without necessarily knowing what's going on. You'll learn more about it in [this week's reading](../readings/week_07.md#readings).

---

### Steps

1. In a branch, add a copy of [`.github/workflows/tests.yml`](../.github/workflows/tests.yml).
1. Create a pull request.
1. [View the results of the Actions run.](https://docs.github.com/en/actions/writing-workflows/quickstart#viewing-your-workflow-results)
1. If the workflow is failing, review the errors and address them.

---

### Submit

[Submit the links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)
