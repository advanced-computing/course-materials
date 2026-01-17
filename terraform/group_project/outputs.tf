output "billing_account" {
  value = google_project.main.billing_account
}

output "project_id" {
  value       = local.project_id
  description = "Derived Google Cloud project ID"
}
