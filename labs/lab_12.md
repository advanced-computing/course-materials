# Lab 12

## Goal

Get experience configuring a cloud environment

---

- You'll be [pairing](../docs/pairing.md) with your Lab partner.
- You'll be making setting things up using [Terraform](https://developer.hashicorp.com/terraform) (console), checking them in the [Console](https://console.cloud.google.com/) (pointing and clicking).
- There are a lot of things that can go wrong. No stress, this is a learning experience.
- Take your time. It's preferred that you read outputs carefully, understand what's going on, and explore, rather than rushing through.

---

## Part 1: Terraform

Work through the [Terraform Google Cloud tutorial](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started), [pairing](../docs/pairing.md) in your Lab groups.

- When it asks you to create a Google Cloud Project, do so with the following settings:
  - Project name: Something like `<user1>-<user2>-lab-12`
  - Organization: `afeld.me`
  - Location: `SIPA Advanced Computing` -> `Spring 2026`

---

## Part 2: IAM for services

We're going to deploy a [Cloud Run Function](https://cloud.google.com/functions) that lists our BigQuery datasets. You can do this part through the Console.

---

### BigQuery setup

1. [Switch](../docs/google_cloud.md#switching-to-your-google-cloud-project) to the Project created above.
1. [Create a table in BigQuery](https://cloud.google.com/bigquery/docs/tables#create-table) using [sample data from Lab 8](../examples/lab_8/PCPI24M1.csv) or any other CSV.

---

### Set up the Hello World Cloud Run Function

1. Create a Function using the ["inline editor"](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console). Set the following, leave the other defaults.
   - Service name: `lab-12`
   - Region: `us-central1`
   - Runtime: `Python 3.14`
   - Uncheck `Use Cloud IAM to authenticate incoming requests`.
   - Under `Container(s), Volumes, Networking, Security` -> `Security`, set service account to be [`Default compute service account`](https://cloud.google.com/functions/docs/securing/function-identity#runtime-sa).
1. It will give you some `Hello World` code. Click `Save and redeploy`.
1. Deployment might take a few minutes. When it's done, try visiting the `URL`.
1. [View the Logs.](https://cloud.google.com/run/docs/logging#viewing-logs-cloud-run)
1. Refresh the live `URL` a bunch of times.
1. [View the Metrics.](https://cloud.google.com/run/docs/monitoring)
1. Explain to each other what happened in this section.

---

### Custom Function

1. `Edit source`, and replace the code.
   - [`main.py`](../examples/cloud_run_function/main.py)
   - Function entry point: `list_datasets`
   - [`requirements.txt`](../examples/cloud_run_function/requirements.txt)
1. Click `Save and redeploy`.
1. Deployment might take a minute. When it's done, try visiting the `URL`. It should show an empty list (`[]`), as it doesn't have access to any BigQuery DataSets.
1. [Grant](https://cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role) [BigQuery Data Viewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) to the [default compute service account (`<project-id>-compute@developer.gserviceaccount.com`)](https://cloud.google.com/functions/docs/securing/function-identity#runtime-sa).
1. Refresh the Function URL. You should see your dataset listed.
1. Explain to each other what happened in this section.

---

Unlike when we [set up Streamlit to talk to BigQuery](../docs/project.md#part-5), no key was needed. Things within Google Cloud (Functions, in this case) run as a service account, and roles can be granted to that.

---

### Challenge

If you got done early, repeat the steps above using the [Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) using Terraform.

---

[Delete the Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) to avoid charges.

---

Nothing needs to be submitted for this Lab.
