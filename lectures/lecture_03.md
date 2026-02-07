# Lecture 3

**The command line**

---

## Reading responses

They are great! Will talk through some of them at the end, if we have time.

---

## CLI

Command line interface

---

## Terminals

- Windows
  - [Command Prompt](https://www.dell.com/support/kbdoc/en-us/000130703/the-command-prompt-what-it-is-and-how-to-use-it-on-a-dell-system)
  - [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview)
  - [Git BASH](https://gitforwindows.org/)
  - [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about)
- macOS/Linux
  - Terminal

---

We'll be using the following in the [VSCode integrated terminal](https://code.visualstudio.com/docs/terminal/getting-started):

- Windows: Git BASH
- macOS: Bash/zsh

Open it up.

---

## Distributions

- UNIX
- UNIX-like
- [POSIX standard](https://en.wikipedia.org/wiki/POSIX)

---

### Examples

- Darwin (macOS)
- Debian
- Ubuntu
- Mint
- Fedora
- Red Hat Enterprise Linux (RHEL)

---

## Paths

- Separators:
  - Windows (outside of Git BASH): `\`
  - macOS/Linux: `/`
- `.` - current directory
- `..` - parent directory
- Absolute vs. relative

---

## Navigation

- `pwd` - path of working directory
- `ls` - list files
  - `ls -al` - list _all_ files (with dotfiles) with more details
- `cd` - change directory
- Mac:
  1. From Finder, right-click on folder
  1. Click `Services`
  1. Click `New Terminal at Folder`

---

Control-`r` allows you to search your command history

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

If files have spaces or special characters, need to put quotes around them.

- Best to avoid these when naming files, sticking to:
  - Letters
  - Numbers
  - Periods
  - Hyphens
  - Underscores
- For Python files, [snake case](https://en.wikipedia.org/wiki/Snake_case) is most common.

---

## Cases

- `snake_case`
- `TitleCase`
- `camelCase`

---

## Exiting/quitting

- less: `q`
- nano: control-`x`
- vim: escape, then `:q!`
- Other command line tools: control-`c`

Worst case, close your Terminal, and that will kill whatever process was running.

---

## Other shell stuff

- `echo`
  - `echo abc | less`
- Exit codes
  - `echo $?`
- Environment variables
- `which`
  - `which jupyter`
  - `which -a python3`
- `$PATH`
- Pipes
  - `ls | xargs cat`
- Redirecting output
- `grep`
- `sudo`
  - [Important coder cultural reference](https://xkcd.com/149/)
- `man`

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

```sh
echo $SHELL
```

---

### Getting fancy

Optional!

- [Oh My Zsh](https://ohmyz.sh/)
- [Oh My Bash](https://ohmybash.nntoan.com/)

---

## Dependency/package management

Done through package managers

---

### Python

- [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
  - [Anaconda](https://anaconda.org/anaconda/repo) [channel](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html), maintained by the company
  - [conda-forge](https://conda-forge.org/packages/), maintained by the community
- [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/)
  - [PyPI](https://pypi.org/)
- [Virtual environment](https://docs.python.org/3/library/venv.html)

---

### Operating system

- Linux: [Aptitude](https://documentation.ubuntu.com/server/how-to/software/package-management/), [Snapcraft](https://snapcraft.io/docs), [others](https://www.linode.com/docs/guides/linux-package-management-overview/)
  - [Debian packages vs. Snaps](https://www.reddit.com/r/Ubuntu/comments/a364ii/proscons_of_snap_vs_apt/)
- Mac: [Homebrew](https://brew.sh/)
- Windows: [Windows Package Manager / WinGet](https://learn.microsoft.com/en-us/windows/package-manager/), [Chocolatey](https://chocolatey.org/), [Scoop](https://scoop.sh/)

---

## [Project Part 2](../docs/project.md#part-2)

---

## Reading response questions

---

### Week 2

#### Workflow & coordination

- I am curious **if there is a way to sync with the home database without doing it manually** once in a while. It seems a bit annoying to have to deal with it regularly.
- At what point does the proliferation of branches and pull requests begin to **introduce coordination overhead, rather than reducing it**?
- If a team hits a WIP limit in a very specialized area, h**ow can generalist team members realistically help clear that bottleneck** if they lack the specific expertise?

---

#### Planning & merge conflicts

- While the readings emphasize how safe branches are, I'm curious what are the **best practices for the planning phase when multiple branches inevitably need to touch the same files**? I'm interested in how teams avoid messy merge conflicts before they happen.

---

### Week 3

#### Terminology

- What's the difference between **command line interface, terminal, shell, and bash**?

---

#### Design responsibility

- It also raises an important question that the readings only briefly touch on: if users are largely unaware of how files actually work, **who bears responsibility for data loss, privacy breaches, or misuse**---users, designers, or institutions?

---

#### AI & the modern relevance of CLI

- Elements of the command line: the prompt, followed by a command, and an option reminds me of talking to an AI chatbot. **Is this the right way of understanding how it works, or are there differences between the two**? I guess one key difference is perhaps that your computer can't "talk back to you", but instead, runs your command, unlike a chatbot.
- The video mentioned that early interfaces prioritized making things easy for computers, not humans. **Will AI change this?** When we can talk to computers in natural language, will command lines become like Latin---something only specialists need?
- Does the **efficiency of the CLI still hold true for professionals whose main focus is policy analysis** rather than software engineering?

---

_Note to self: Send terminal commands+output._
