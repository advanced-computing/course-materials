# Lecture 5

---

## [Project Part 2](../docs/project.md#part-2)

How did it go?

---

## How do you know your code works?

---

## Example

We want to normalize phone numbers. What situations do we need to handle?

---

## [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)

1. Create an empty function
1. Try the different test cases
1. Make them pass
   - Small increments

---

- Working backwards from the expected behavior
- Test cases
  - Edge cases
- The tests become the requirements

---

- `print()`
- `assert`
- Loop

---

## Unit testing

- inputs → function → expected outputs
- Generally testing:
  - Small chunks of code
  - Specific functionality
- Generally should work offline, i.e. not talk to an API or anything
- Generally will use small sets of sample data

---

- **Unit testing:** individual components
- **Integration testing:** multiple components together

---

There are [others](https://www.ssw.com.au/rules/different-types-of-testing/) — it's essentially a spectrum of small to large.

---

When might we want to use unit vs. integration tests? In other words, what are the pros and cons of each?

---

### [pytest](https://docs.pytest.org/)

Structured way of doing what we were already doing

---

#### [Parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html)

---

## Profiling

[Examples](lecture_05_profiling.ipynb)

---

## Data cleaning

1. Add tests for parsing the dollar amount
1. Refactor the code
1. Make them pass

---

Code needs to be testable. This encourages good habits, like:

- Ensuring your code can change without unexpected breakage
- Making small, reusable functions with well-defined behavior
- Organizing code into modules
- Allowing the loading of a module without running all the code

---

## Code organization

Seeing projects with `<name>2.py`. Splitting code up into smaller files will help you work in parallel without stepping on each others' toes.

---

## Data quality checks

- Can be flexible, like checking for standard deviation or X% matching certain criteria
- [Things to check for when cleaning data](https://computing-in-context.afeld.me/lecture_17.html#data-cleaning)
- There are tools that help with this

---

## [Project Part 3](../docs/project.md#part-3---unit-testing)

---

Reminder of the [Project expectations](../docs/project.md#expectations).
