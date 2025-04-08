# Lab 3

## Goals

Students:

- Get the repository that they'll be building their Projects in set up
- Practice working collaboratively in a repository

---

## Preliminaries: Terminal in VSCode

- Open the [integrated terminal](https://code.visualstudio.com/docs/terminal/getting-started)
  - [Select the shell](https://code.visualstudio.com/docs/terminal/getting-started#_run-commands-in-another-shell) (Git Bash or other)
- [Python interpreter selection](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters)
  - Use the **Python: Select Interpreter** from the **Command Palette** (`Ctrl+Shift+P`)

---

## [Project team](../docs/project_teams.csv) repository setup

- [Create a public repository in the `advanced-computing` organization.](https://github.com/new?owner=advanced-computing&visibility=public)
  - Make the name something distinctive, such as:
    - What your project is focused on
    - Your celebrity couple name
    - A combination of your favorite snacks
    - The name your automation will assume once it becomes sentient
- On your computer choose a directory to locate your local repository
  - Choose a path that will be easy to access:
    - &check; `C:/repos/`
    - &cross; `C:/Users/rbzun/OneDrive/Documents/classes/advanced computing/`
- Using the terminal
  - `cd` to this directory
  - [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) your project repository
    1. Copy the repository URL
    1. In the terminal run `git clone <URL>`
- Open your local repository folder in VSCode

---

## Adding a [`.gitignore`](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-a-single-repository)

- In general, we don't want Git to commit every single file in our local repository
  - Examples: **.DS_Store** files in macOS; **Thumbs.db** files in Windows; python environment files **.env** and **.venv** (more on this below)
- We can tell Git which files and folders to ignore using a .gitignore file
- [Set one up for Python and Mac or Windows](https://www.toptal.com/developers/gitignore?templates=macos,python)
- Save a .gitignore file in your repository's root directory

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

- Check the list of changes in the Source Control panel of VSCode
- Go to the .gitignore file, comment the `.venv/` line and save
- Check the list of changes again. Can you see the problem?
- Uncomment the `.venv/` line and save
- Create a new branch, commit and push
- By group, merge one of the pull requests

---

## Pull request practice

- Make sure your repository is up-to-date: `checkout` to the main branch and `pull`
- Each student will create a new branch to add a new feature:
  - **Student A**: add the notebook from [Part 1](../docs/project.md#part-1)
    - Ensure the notebook runs from VSCode.
    - The notebook may not (fully) render on GitHub, due to having interactivity. Try accessing the GitHub URL via [nbviewer](https://nbviewer.org/)/[Colab](https://colab.research.google.com/).
  - **Student B**: add a README.md
    - Add project title and a short description
    - Setup/usage instructions - these will change over time
  - **Student A or B**: add an [Open in Colab button](https://openincolab.com/)
- Review each other's pull requests

---

## Adding TODOs

Each group [create issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/quickstart) for the things that came up in [the brainstorming](../lectures/lecture_02.md#the-project). Add objectives / [acceptance criteria](https://www.atlassian.com/work-management/project-management/acceptance-criteria) for each. (These can change later.)

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

[**Submit** via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)
