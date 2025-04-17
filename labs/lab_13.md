# Lab 13

**Cloud-based pipelines**

You'll be working with your [Project team](../docs/project_teams.csv).

---

## Goal

Your regularly-updated data is being pulled in automatically

---

GitHub Actions ➡️ Python ➡️ BigQuery

---

Back in [Lab 6](lab_06.md#steps), you set up automated testing. Use that as a template to make another workflow that runs on a [schedule](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule) for ETL.

---

How will you know if it worked?

---

## Connection

GitHub Actions will need credentials + permissions to write to BigQuery.

1. [Create a service account in Google Cloud.](https://cloud.google.com/iam/docs/service-accounts-create)
1. [Create a key](https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console) as JSON.
1. Add it to GitHub Actions as a [secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).

---

## Tips

- You can make the schedule more frequent to test it out.
- You might want to set up [table snapshots](https://cloud.google.com/bigquery/docs/table-snapshots-intro) in case anything goes wrong.
- You might want to make separate test and production datasets/tables in BigQuery.

---

## Optional

Get the workflow running locally with [act](https://nektosact.com/)

---

[Submit a link to your GitHub Actions run history via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)
