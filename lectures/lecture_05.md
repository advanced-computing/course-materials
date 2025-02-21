# Lecture 5

**Automated testing**

---

## [Survey](https://docs.google.com/forms/d/e/1FAIpQLSdLj1Y6WLyD6bWHmNCV9G47MNZPtHEtjGKaugyE9uahuG81HA/viewform?usp=header)

---

## [Project Part 2](../docs/project.md#part-2)

How did it go?

---

## Questions?

---

## How do you know your code works?

---

## Example

We want to normalize phone numbers. What situations do we need to handle?

---

[Solution](../examples/phone/test_phone.py)

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

### [Running through VSCode](https://code.visualstudio.com/docs/python/testing)

---

#### [Debugging](https://code.visualstudio.com/docs/python/testing#_debug-tests)

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

[Examples](../examples/profiling/profiling.ipynb)

---

## [Project Part 3](../docs/project.md#part-3)

---

Reminder of the [Project expectations](../docs/project.md#expectations).
