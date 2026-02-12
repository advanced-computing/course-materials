# Lab 13: BigQuery setup for automated data updates

# Service account for GitHub Actions to access BigQuery
resource "google_service_account" "lab_13_github_actions" {
  project      = local.root_project
  account_id   = "lab-13-github-actions"
  display_name = "Lab 13 GitHub Actions service account"
}

# Grant BigQuery job user permission at project level (needed to run queries)
resource "google_project_iam_member" "lab_13_bigquery_job_user" {
  project = local.root_project
  role    = "roles/bigquery.jobUser"
  member  = google_service_account.lab_13_github_actions.member
}

# Grant dataset-level access to stock_data dataset only
resource "google_bigquery_dataset_iam_member" "lab_13_stock_data_editor" {
  dataset_id = "stock_data"
  role       = "roles/bigquery.dataEditor"
  member     = google_service_account.lab_13_github_actions.member
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
