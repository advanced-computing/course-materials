# Lab 6

You'll work in your [Project teams](../docs/project_teams.csv).

## Objectives

- Get ready to work in Google Cloud
- Set up continuous integration

---

## Google Cloud setup

Everyone go through the [instructions](../docs/google_cloud.md).

---

## Continuous integration

You're going to set up your tests and static analysis to run automatically. We'll be using [ruff](https://docs.astral.sh/ruff/) for the latter.

This is one of those times where you'll follow instructions without necessarily knowing what's going on. You'll learn more about it in [this week's reading](../readings/week_07.md).

---

### Steps

1. Install the [ruff VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).
1. In a branch, add a copy of [`.github/workflows/tests.yml`](../.github/workflows/tests.yml).
1. Create a pull request.
1. [View the results of the Actions run.](https://docs.github.com/en/actions/writing-workflows/quickstart#viewing-your-workflow-results)
1. If the workflow is failing, fix it (by fixing your code).

---

### Submit

[Submit the links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)
