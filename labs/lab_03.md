# Lab 3

---

## Objectives

Students:

- Get the repository that they'll be building their Projects in set up
- Practice working collaboratively in a repository

---

## Terminal in VSCode

- [Using the integrated terminal](https://code.visualstudio.com/docs/terminal/getting-started)
  - [Selecting the shell](https://code.visualstudio.com/docs/terminal/getting-started#_run-commands-in-another-shell)
- [Python interpreter selection](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters)

---

## [Project team](../docs/project.md#teams) repository setup

1. [Create a public repository in the `advanced-computing` organization.](https://github.com/new?owner=advanced-computing&visibility=public)
   - Make the name something distinctive, such as:
     - What your project is focused on
     - Your celebrity couple name
     - A combination of your favorite snacks
     - The name your automation will assume once it becomes sentient
1. In the repository folder, [create a virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments).
1. Add a [`.gitignore`](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-a-single-repository).
   1. Demo
      - Explain what it does and what it's for
   1. [Set one up for Python and Mac (if applicable)](https://www.toptal.com/developers/gitignore?templates=macos,python)
1. Add a `requirements.txt`.
1. [Activate the virtual environment.](https://docs.python.org/3/library/venv.html#how-venvs-work)
1. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

---

## Pull request practice

Have them trade off sending and reviewing pull requests to add:

- The notebook from [Part 1](../docs/project.md#part-1)
  - [Select the Python interpreter under `.venv/` as the kernel.](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
  - Ensure the notebook runs from VSCode.
  - The notebook may not (fully) render on GitHub, due to having interactivity. Try accessing the GitHub URL via [nbviewer](https://nbviewer.org/)/[Colab](https://colab.research.google.com/).
- A README
  - Setup/usage instructions - these will change over time
- An [Open in Colab button](https://openincolab.com/)

---

## TODOs

Have each group [create issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/quickstart) for the things that came up in [the brainstorming](../lectures/lecture_02.md#the-project). They should add objectives / [acceptance criteria](https://www.atlassian.com/work-management/project-management/acceptance-criteria) for each. (These can change later.)
