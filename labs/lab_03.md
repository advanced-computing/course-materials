# Lab 3

## Goals

Students:

- Get their Project repository set up
- Practice working collaboratively in a repository

---

## Preliminaries: Terminal in VSCode

- Open the [integrated terminal](https://code.visualstudio.com/docs/terminal/getting-started)
  - [Select the shell](https://code.visualstudio.com/docs/terminal/getting-started#_run-commands-in-another-shell) (Git Bash or other)
- [Python interpreter selection](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters)
  - Use the **Python: Select Interpreter** from the **Command Palette** (`Ctrl+Shift+P`)

---

## [Project team](../docs/project.md#teams) repository setup

1. [Create a public repository in the `advanced-computing` organization.](https://github.com/new?owner=advanced-computing&visibility=public)
   - Make the name something distinctive, such as:
     - What your project is focused on
     - Your celebrity couple name
     - A combination of your favorite snacks
     - The name your automation will assume once it becomes sentient
1. Using the terminal
   1. `cd` to this directory
   1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) your project repository
      1. Copy the repository URL
      1. In the terminal run `git clone <URL>`
1. Open your local repository folder in VSCode

---

## Adding a [`.gitignore`](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-a-single-repository)

- In general, we don't want Git to commit every single file in our local repository. Examples:
  - **.DS_Store** files in macOS
  - **Thumbs.db** files in Windows
  - Python environment files **.env** and **.venv** (more on this below)
- We can tell Git which files and folders to ignore using a `.gitignore` file
- [Set one up for Python and Mac or Windows](https://www.toptal.com/developers/gitignore?templates=macos,python)
- Save a `.gitignore` file in your repository's root directory

---

## Setting up a Virtual Environment

- In the repository folder, [create a virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) running the command `python -m venv .venv`
- Add a `requirements.txt` listing the packages that you expect to use in your project. Write each package on its own line, for example:

  ```
  pandas
  jupyter==1.*
  plotly
  ```

- [Activate the virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work)
- Install the dependencies:

  ```sh
  pip install -r requirements.txt
  ```

- [Select the Python interpreter under `.venv/` as the kernel.](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)

---

## Checking that .gitignore works

1. Check the list of changes in the Source Control panel of VSCode.
1. Go to the `.gitignore` file, comment the `.venv/` line and save.
1. Check the list of changes again. Can you see the problem?
1. Uncomment the `.venv/` line and save.
1. Create a new branch, commit and push.
1. By group, merge one of the pull requests.

---

## Pull request practice

1. Make sure your repository is up-to-date: `checkout` to the `main` branch and `pull`
1. Each student will create a new branch to add a new feature:
   1. **Student A**: add the notebook from [Part 1](../docs/project.md#part-1)
      - Ensure the notebook runs from VSCode.
      - The notebook may not (fully) render on GitHub, due to having interactivity. Try accessing the GitHub URL via [nbviewer](https://nbviewer.org/)/[Colab](https://colab.research.google.com/).
   1. **Student B**: add a `README.md`.
      - Add project title and a short description
      - Setup/usage instructions - these will change over time
   1. **Student A or B**: add an [Open in Colab button](https://openincolab.com/)
1. Review each other's pull requests

---

## Adding TODOs

Each Project team will:

1. Re-review the [Project goals](../docs/project.md#goals) and think back to [the brainstorming](../lectures/lecture_02.md#the-project).
1. Think through what it will take to achieve that.
   - What are the [known unknowns](https://en.wikipedia.org/wiki/There_are_unknown_unknowns)?
1. Create at least eight [issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/quickstart).
   - Add objectives / [acceptance criteria](https://www.atlassian.com/work-management/project-management/acceptance-criteria) for each.
   - These can change later.

---

### Examples

```markdown
Get data

- [ ] The get data function should collect all data from source XX
- [ ] The data should be stored as a DataFrame with columns X, Y, Z,...
- [ ] The get data function should print the number of rows
```

```markdown
Make Visualization X

- [ ] Add a visualize button
- [ ] Produce an interactive graph showing X vs Y
- [ ] Add a filter by YY option
- [ ] Add a group by ZZ option
```

---

[**Submit** via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)
