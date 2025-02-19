# Google Cloud

## Course setup

This only needs to be done once per semester.

1. If the number of students+instructors is larger than 20, [request a Project Quota increase](https://support.google.com/code/contact/project_quota_increase).
1. [Install Terraform](https://developer.hashicorp.com/terraform/install).
1. [Install `gcloud`](https://cloud.google.com/sdk/docs/install).
1. Set up `gcloud`:

   ```sh
   gcloud config configurations activate columbia
   gcloud auth application-default login
   ```

1. Ensure the [teams list](project_teams.csv) is up to date.
1. Run `terraform apply`.

As students go through the setup (below), you can re-run the `apply` to get a report of who is missing billing.
