# Lecture 11

**Data engineering, continued**

---

We're going to revisit a number of concepts from earlier.

---

What can go wrong in data loading/manipulation? What errors/bugs have you hit?

---

What would you want to happen?

---

## Process mapping

---

### DAGs

**Directed acyclic graphs**

What does that mean?

---

## Online vs. offline data processing

- Batch jobs
- [Online analytical processing (OLAP)](https://en.wikipedia.org/wiki/Online_analytical_processing)
- [Online transaction processing (OLTP)](https://en.wikipedia.org/wiki/Online_transaction_processing)

---

## Pipelines

[From Arshiya](https://edstem.org/us/courses/73208/discussion/6434817?comment=14941963):

> Why is DAG different from setting workflows in Github?

---

- Useful for complex [ETL](lecture_10.md#overview)
- Dependencies
- Assets
- Data
- Code (continuous integration/deployment)

---

## Persistence

Why store the data?

---

## Data lake/warehouse

<!-- https://lucid.app/lucidchart/3a04cf05-06b1-4a79-a2f5-b72314f0d46e/edit --->

![Warehouse layers](../img/warehouse_layers.svg)

---

## [Airflow](https://airflow.apache.org/)

---

[From Angel](https://edstem.org/us/courses/73208/discussion/6434817?comment=14975715):

> this method [DAGs?] increases data pipeline transparency but simultaneously increases reliance on developer discipline. Code flexibility might just as easily turn into production instability.

---

There are _many_ [alternative data integration / workflow orchestration tools](https://www.pracdata.io/p/open-source-data-engineering-landscape-2025).

---

## [Project Part 6](../docs/project.md#part-6)

---

## [Readings](../readings/week_12.md)

They're heavy this week, don't wait!
