# Lab 12 - IN PROGRESS

## Goal

Get experience configuring a cloud environment

---

You'll be [pairing](../docs/pairing.md) with a new person. You'll be User A and B, to see things from both sides.

When it says `User A:`, use a browser logged in as that person. Ditto for B. May be easiest to switch between laptops.

---

## Steps

Do the following through the [Console](https://console.cloud.google.com/):

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
1. **User A:** Set up a [service account](https://cloud.google.com/iam/docs/service-account-overview).
   1. [Create a service account.](https://cloud.google.com/iam/docs/service-accounts-create#creating) Call it `lab-12-demo`.
   1. Grant [BigQuery Data Viewer](https://cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) to the service account.
   1. [Create a key for the service account.](https://cloud.google.com/iam/docs/keys-create-delete)
1. Try accessing from `gcloud`
1. `gcloud config set project <project>`
1. `gcloud app deploy`
1. [Delete the Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) to avoid charges.

---

Nothing needs to be submitted for this Lab.
