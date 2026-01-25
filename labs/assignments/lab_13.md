# Lab 13

**Cloud-based pipelines**

You'll be working with your [Project team](../semesters/spring_2026/people.csv).

---

## Goal

Your regularly-updated data is being pulled in automatically

---

GitHub Actions ➡️ Python ➡️ BigQuery

---

Make a workflow that runs on a [schedule](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule) to run your ETL. Check out [the workflows in this repository](../.github/workflows/) as examples you can start with.

---

## Thinking ahead

- How will you know if it worked?
- If something went wrong, where would you look to find out why?

---

## Hints

<details>
   <summary>There's an extra step</summary>
   GitHub Actions will need credentials + permissions to write to BigQuery.
</details>

<details>
   <summary>How to do it</summary>
   <ol>
      <li><a href="https://cloud.google.com/iam/docs/service-accounts-create">Create a service account in Google Cloud.</a></li>
      <li><a href="https://cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role">Grant</a> it the appropriate <a href="https://cloud.google.com/bigquery/docs/access-control#bigquery">role</a>.</li>
      <li><a href="https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console">Create a key</a> as JSON.</li>
      <li>Add it to GitHub Actions as a <a href="https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions">secret</a>.</li>
   </ol>
</details>

---

## Tips

- To test out the workflow, you can:
  - Make the schedule more frequent
  - Set it to `push`
  - [Run it manually](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow)
  - Advanced: [Run it locally](https://nektosact.com/)
- To protect yourself in case your data gets messed up:
  - Set up [table snapshots](https://cloud.google.com/bigquery/docs/table-snapshots-intro).
  - Make separate test and production datasets/tables in BigQuery.

---

## Optional

---

[Submit via CourseWorks:](https://courseworks2.columbia.edu/courses/233896/assignments)

- Links to your pull request(s)
- A link to your GitHub Actions run history
