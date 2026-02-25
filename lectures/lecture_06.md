# Lecture 6

**Organizing code**

---

## [Survey responses](https://edstem.org/us/courses/89925/discussion/7698376)

---

How have you been organizing code (in this course and before)?

---

…within files?

---

…between files?

---

## Modules

_Files! Things you `import`!_

---

### Search path

1. Show [Python's module search path](https://docs.python.org/3/library/sys_path_init.html).

   ```python
   import sys
   sys.path
   ```

1. Look in those directories.
1. Look at `csv.py`.
1. Make a `csv.py` file the current directory.

   ```python
   print("Aidan csv")
   ```

1. Try `import csv`.

---

## Refactoring

Let's refactor [phone code](../examples/phone/) from [last lecture](lecture_05.md#example).

---

Simulate an API call:

```python
from time import sleep

sleep(5)
```

How do we keep the tests from being slow?

---

## Packages

_Folders!_

---

How have you been organizing data?

---

## Data structures

> a _data structure_ is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data

[Encyclopedia of Computer Science, 2003](https://dl.acm.org/doi/epdf/10.5555/1074100.1074312)

---

What data structures exist in Python?

---

## Abstraction

---

## Object-Oriented Programming (OOP)

[Intro from Python course](https://python-public-policy.afeld.me/en/columbia/lecture_0.html#fundamental-programming-concepts)

---

## Code/test coverage

[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html)

---

```sh
pytest --cov --cov-report html
open htmlcov/index.html
```

---

### Branching

Not the Git kind

---

## [Project Part 4](../docs/project.md#part-4)

---

### Revisit [expectations](../docs/project.md#expectations)
