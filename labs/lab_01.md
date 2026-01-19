# Lab 1

## Goals

Students:

- are set up with:
  - Git
  - VSCode
  - Terminal
- understand how to work with Git repositories

---

## Setup

We're going to go through and make sure you have the following installed / set up:

### [Git](https://git-scm.com/downloads)

- On Windows, there are a _lot_ of options in the installer - safe to stick to the defaults.
- Set global [name](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git) and [email](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address#setting-your-commit-email-address-in-git)

```
git config --global user.name "Mona Lisa"
git config --global user.email "ml1234@columbia.edu"
```

---

### [Visual Studio Code (VSCode)](https://code.visualstudio.com/)

- On Windows, in the [integrated terminal](https://code.visualstudio.com/docs/terminal/getting-started), [`Select Default Profile`](https://code.visualstudio.com/docs/terminal/profiles) to be `Git BASH`.

<img src="https://code.visualstudio.com/assets/docs/terminal/basics/terminal-dropdown.png" width="200" height="200" />

If you did all the following:

- took [Computing in Context](https://computing-in-context.afeld.me/)
- have the same computer
- didn't uninstall any of the development tools

…then you should be all set.

---

## Add avatar to bio

1. [Clone](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_clone-a-repository-locally) [the repository](https://github.com/advanced-computing/course-materials).
1. [Create a branch.](https://code.visualstudio.com/docs/sourcecontrol/overview#_branches-and-tags)
1. Add a profile photo / avatar under [`semesters/spring_2026/img/`](../semesters/spring_2026/img/).
   - Keep them around 200px tall, please.
1. [Add the image to your Markdown file.](https://www.markdownguide.org/basic-syntax/#images-1)
   - [Preview](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview)
1. [Commit](https://code.visualstudio.com/docs/sourcecontrol/overview#_commit)
1. Check out the [Source Control Graph](https://code.visualstudio.com/docs/sourcecontrol/overview#_source-control-graph).
1. [Push](https://code.visualstudio.com/docs/sourcecontrol/overview#_remotes)
1. [Create a pull request.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
1. Check out the repository's [network graph](https://github.com/advanced-computing/course-materials/network).
1. Review the pull request of the person next to you.
1. Merge.
1. Submit a link to your pull request in the Assignment.

---

## Sign the Attendance List

1. [Checkout](https://code.visualstudio.com/docs/sourcecontrol/overview#_branches-and-tags) to the default branch
1. [Fetch and Pull](https://code.visualstudio.com/docs/sourcecontrol/overview#_source-control-graph) to retrieve new work done by other people and merge it with your local bracnh
1. View other people's profile pictures
1. Create a branch
1. Add your name to the [attendance list](attendance_example_lab_01.md)
1. Commit, push and create a pull request
1. Review the pull request of the person next to you.
1. Merge

---

## Git concepts/[terms](https://docs.github.com/en/get-started/learning-about-github/github-glossary)/[workflow](https://docs.github.com/en/get-started/using-github/github-flow)

- Repository
- Clone
- Branch
- Commit
- History
- Push
- Review
- Merge
- Fork

[Slides visualizing Git history](https://speakerdeck.com/aidanfeldman/git-graphically)
