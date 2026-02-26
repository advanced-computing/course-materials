# Lab 6

[Slides in PDF format](lab_06_slides.pdf)

You'll work in your [Project teams](../docs/project.md#teams).

---

## Goal

Level up your Project repository. This includes:

- Linting
- Continuous integration
- Data validation

---

## Linting

- A type of [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)
- Code quality
- We'll be starting with [ruff](https://docs.astral.sh/ruff/).

---

### Configuration

Add the [ruff configuration](https://docs.astral.sh/ruff/configuration/) from [this repository](../pyproject.toml) to yours.

---

This is a starting place; you're welcome to adapt it as you go.

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

## Data validation

We'll be using [Pandera](https://pandera.readthedocs.io/). **Write data validations for all variables (columns) of interest** across your datasets. (Should probably be fewer than 20.)

- What assumptions are you making about the data that you'd want to validate going forward?

---

## Submit

[Submit links to the pull request(s) via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)
