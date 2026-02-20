output "billing_account" {
  value = google_project.main.billing_account
}

output "project_id" {
  value       = google_project.main.project_id
  description = "Derived Google Cloud project ID"
}

output "repository_info" {
  value = var.create_repository ? {
    name         = github_repository.project[0].name
    homepage_url = github_repository.project[0].homepage_url
    html_url     = github_repository.project[0].html_url
  } : null
  description = "Repository information including homepage URL"
}
