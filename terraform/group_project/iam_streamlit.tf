resource "google_service_account" "streamlit" {
  project      = var.project_id
  account_id   = "streamlit"
  display_name = "Streamlit service account"
}

resource "google_project_iam_member" "streamlit_to_bigquery" {
  # https://cloud.google.com/bigquery/docs/access-control
  for_each = toset([
    "roles/bigquery.dataViewer",
    "roles/bigquery.jobUser",
  ])

  project = var.project_id
  role    = each.value
  member  = google_service_account.streamlit.member
}
