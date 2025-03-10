resource "google_service_account" "streamlit" {
  project      = var.project_id
  account_id   = "streamlit"
  display_name = "Streamlit service account"
}

resource "google_project_iam_member" "streamlit_to_bigquery" {
  project = var.project_id
  # https://cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer
  role   = "roles/bigquery.dataViewer"
  member = google_service_account.streamlit.member
}
