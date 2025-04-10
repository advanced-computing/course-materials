# Lab 12

## Goal

Get experience configuring a cloud environment

---

- You'll be [pairing](../docs/pairing.md) with a new person.
- You'll work in the [Console](https://console.cloud.google.com/).
- Take your time. It's preferred that you read outputs carefully, understand what's going on, and explore, rather than rushing through.

---

## Steps

### Part 1: IAM for users

You'll be User A and B, to see things from both sides. When it says `User A:`, use a browser logged in as that person. Ditto for B. May be easiest to switch between laptops.

1. **User A:** Project setup
   1. [Create a new Project.](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)
      - Name it something like `<user1>-<user2>-lab-12`.
   1. [Change the Billing Account](https://cloud.google.com/billing/docs/how-to/modify-project#how-to-change-ba) to that person's `Billing Account for Education`.
   1. [Grant](https://cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role) User B [BigQuery Admin](https://cloud.google.com/bigquery/docs/access-control#bigquery.admin) at the Project level.
1. **User B:** BigQuery setup
   1. [Switch](../docs/google_cloud.md#switching-to-your-google-cloud-project) to the Project created above.
   1. [Create a table in BigQuery](https://cloud.google.com/bigquery/docs/tables#create-table) using [sample data from Lab 8](../examples/lab_8/PCPI24M1.csv) or any other CSV.
1. **User A:** [Revoke access.](https://cloud.google.com/docs/security/data-loss-prevention/revoking-user-access#remove-account)
1. **User B:** Refresh the page. You should get an access error.
1. Explain to each other what's been done so far.

---

### Part 2: IAM for services

We're going to deploy a [Cloud Run Function](https://cloud.google.com/functions) that lists our BigQuery datasets.

1. Create a Function using the ["inline editor"](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console). Set the following, leave the other defaults.
   - Service name: `lab-12`
   - Region: `us-central-1`
   - Runtime: `Python 3.12`
   - Uncheck `Use Cloud IAM to authenticate incoming requests`.
   - Under `Container(s), Volumes, Networking, Security` -> `Security`, set service account to be [`Default compute service account`](https://cloud.google.com/functions/docs/securing/function-identity#runtime-sa).
1. Click `Save and redeploy`.
1. Deployment might take a few minutes. When it's done, try visiting the `URL`.
1. `Edit source`, and replace the code.
   - [`main.py`](../examples/cloud_run_function/main.py)
   - Function entry point: `list_datasets`
   - [`requirements.txt`](../examples/cloud_run_function/requirements.txt)
1. Click `Save and redeploy`.
1. Deployment might take a minute. When it's done, try visiting the `URL`. It should show an empty list (`[]`), as it doesn't have access to any BigQuery DataSets.
1. [Grant](https://cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role) [BigQuery Data Viewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) to the [default compute service account (`<project-id>-compute@developer.gserviceaccount.com`)](https://cloud.google.com/functions/docs/securing/function-identity#runtime-sa).
1. Refresh the Function URL. You should see your dataset listed.
1. Explain to each other what you did.
1. [Delete the Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) to avoid charges.

---

Unlike when we [set up Streamlit to talk to BigQuery](../docs/project.md#part-5), no key was needed — things within Google Cloud (Functions, in this case) run as a service account.

---

Nothing needs to be submitted for this Lab.
