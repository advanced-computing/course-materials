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

---

## [Reading response questions](https://edstem.org/us/courses/89925/discussion/7680568)

### Testing Strategy & Workflow

- "The materials explain how to write unit tests, but I am curious about **practical guidelines for deciding what to test and how much coverage is sufficient**. When working with limited time, how do experienced **developers prioritize which tests to write first**?"
- "I am also wondering **how often we are expected to do unit testing**? Or is this more like an effective way when debugging to find where the problem/bug exactly lies?"
- "As for the "Pytest" part, I find it to be a very strong tool to run automatic testing and give multiple possible results, but I'm still not sure **how to apply that to the group project**. What is the best way to integrate automated testing (e.g., Pytest) with version control workflows so that collaboration remains efficient rather than restrictive?"

---

### PyUnit vs. Pytest

- "I also wonder **why python still includes pyunit if pytest is more modern** and simpler?"
- "While the reading introduced two types of test method; Pyunit and Pytest, I am still **unclear about the pros and cons** of pyUnit versus Pytest."

---

### Post-Launch Bugs & Types of Testing

- "I just wonder if they have already done sufficient testing but the error still occurs after the app is launched, what is the general rule for companies to do? **Some errors still occur in many big apps in the world**. Also, is **stress testing** a part of software testing?"
