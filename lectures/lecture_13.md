# Lecture 13

**Big data; algorithms**

---

## [Lab 12](../labs/lab_12.md) issue

Redo tomorrow

---

## [Schedule](../README.md#schedule)

---

## Big-O notation

---

## Exercise

Write out five two-digit numbers.

---

1. When I say "go", add them up.
   - This is not a race.
   - [Stopwatch](https://www.google.com/search?q=stopwatch)
1. Record the time.
   - [Results](https://docs.google.com/spreadsheets/d/1YY757UIDWnJ3OowZXqoFcQl3_F_nLBrxqY_x7EEZGuw/edit)

---

For this exercise, don’t care if the answer's right or not.

---

Repeat with 10 numbers.

---

Repeat with 20 numbers.

---

1. Split into groups of roughly even size (3-5).
1. Someone be the reducer, others will be the workers.
1. Workers, write out 10 two-digit numbers, split up roughly evenly (i.e. 3-3-4).

---

When I say "go":

1. Workers:
   1. Add your numbers.
   1. Tell the reducer your sum.
1. Reducer:
   1. Add them up.
   1. Record the time.

---

How many [compute cycles](https://en.wikipedia.org/wiki/Instruction_cycle) did each take?

---

## Back to Big-O

_Draw chart of times on chalkboard, individual and team_

How long would we expect each to take for 100 (10x) numbers?

---

## Parallelization

- Threads
- Distributed workloads
- MapReduce

---

What are real-world examples?

- Serial vs. parallel
- Sync vs. async

---

## [Project Parts 7 and 8](../docs/project.md#part-7)

---

## [Lab 14](../labs/lab_14.md) DMs

Need 1/4 or 1/5 of the class as volunteers.

- You'll be the [Dungeon Master (DM)](https://en.wikipedia.org/wiki/Dungeon_Master), for folks familiar with D&D
- Should be a good storyteller / comfortable thinking on your feet
- 15-30 minutes of prep required
  - A doc will be shared with you

---

## [Reading response questions](https://edstem.org/us/courses/89925/discussion/7941726)

### Algorithms & Efficiency

- While I did find that sorting was the easiest for my brain to understand, I'm still a bit confused why the other examples were more efficient. Were there just less steps involved whereas sorting would have to go through each value one by one?
- Is there still a practical reason for someone who is not a CS student to learn bubble sort or selection sort, or are they really just teaching tools at this point?
- Could we go over Big O/ an example together :D

---

### Algorithms & AI

- If AI is fundamentally built on algorithms though, why does policy discourse treat AI governance as its own distinct conversation? Are black box algorithms really so vague and complex that we cannot understand their decisions?
