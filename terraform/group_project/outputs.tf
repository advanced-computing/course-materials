output "billing_account" {
  value = google_project.main.billing_account
}

output "project_id" {
  value       = local.project_id
  description = "Derived Google Cloud project ID"
}

output "repository" {
  value = {
    name = github_repository.project.name
    url  = github_repository.project.html_url
    # ssh  = github_repository.project.ssh_clone_url
  }
  description = "GitHub repository details"
}
