# Lecture 3 - the command line

---

## Terminals

- Windows
  - Command Prompt
  - PowerShell
  - Git BASH
  - Windows Subsystem for Linux (WSL)
- macOS/Linux
  - Terminal

---

## Distributions

- UNIX
- UNIX-like
- POSIX standard

---

### Examples

- Darwin (macOS)
- Debian
- Ubuntu
- Mint
- Fedora
- Red Hat Enterprise Linux (RHEL)

---

## Navigation

- `pwd`
- `ls`
  - `ls -al`
- `cd`

---

## Working with files

- Viewing
  - `cat`
  - `less`
- `mv`
- `cp`
- `mkdir`
- `rmdir`
- `find`
- Editing
  - `nano`
  - `vim`

---

## Other shell stuff

- `echo`
- Variables
- `whereis`
  - `whereis jupyter`
  - `whereis -a python3`
- `$PATH`
- Pipes
  - `ls | xargs cat`
- Redirecting output
- `grep`
- `sudo`

---

### Example

Uses a "wildcard":

1. `find . -name 'lecture_*.md'`
1. `find . -name 'lecture_*.md' | sed -E 's/([0-9]{2})/0\1/'`

---

## Shells

- PowerShell
- Bash
- zsh

---

## Dependency/package management

Done through package managers

---

### Python

- [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
- [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/)
  - [PyPI](https://pypi.org/)
- [Virtual environment](https://docs.python.org/3/library/venv.html)

---

#### [VSCode interpreter selection](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters)

---

### Operating system

- Linux: [Aptitude](https://documentation.ubuntu.com/server/how-to/software/package-management/), [Snapcraft](https://snapcraft.io/docs), [others](https://www.linode.com/docs/guides/linux-package-management-overview/)
  - [Debian packages vs. Snaps](https://www.reddit.com/r/Ubuntu/comments/a364ii/proscons_of_snap_vs_apt/)
- Mac: [Homebrew](https://brew.sh/)
- Windows: [Windows Package Manager / WinGet](https://learn.microsoft.com/en-us/windows/package-manager/), [Chocolatey](https://chocolatey.org/)

---

## [Project Part 2](../docs/project.md#part-2)
