# Lab 13: BigQuery setup for automated data updates

# Service account for GitHub Actions to access BigQuery
resource "google_service_account" "lab_13_github_actions" {
  project      = local.root_project
  account_id   = "lab-13-github-actions"
  display_name = "Lab 13 GitHub Actions service account"
}

# Grant BigQuery permissions to the service account
resource "google_project_iam_member" "lab_13_bigquery_permissions" {
  for_each = toset([
    "roles/bigquery.dataEditor",
    "roles/bigquery.jobUser",
  ])

  project = local.root_project
  role    = each.value
  member  = google_service_account.lab_13_github_actions.member
}

# Create a service account key
resource "google_service_account_key" "lab_13_github_actions_key" {
  service_account_id = google_service_account.lab_13_github_actions.name
}

# Store the service account key as a GitHub secret
resource "github_actions_secret" "lab_13_bq_credentials" {
  repository      = "course-materials"
  secret_name     = "BQ_LAB13"
  plaintext_value = base64decode(google_service_account_key.lab_13_github_actions_key.private_key)
}
