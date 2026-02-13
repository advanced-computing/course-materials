# Create GitHub repository for the project
resource "github_repository" "project" {
  count = var.create_repository ? 1 : 0

  name        = var.team_id
  description = "Group project repository: ${join(", ", [for student in var.students : student.first_name])}"
  visibility  = "public"

  has_issues             = true
  has_projects           = true
  has_wiki               = false
  auto_init              = false
  delete_branch_on_merge = true

  security_and_analysis {
    secret_scanning {
      status = "enabled"
    }
  }

  topics = ["advanced-computing", "group-project"]

  lifecycle {
    prevent_destroy = true
    # allow students to update
    ignore_changes = [description]
  }
}

# Add students as collaborators to the project repository
resource "github_repository_collaborator" "students" {
  for_each = var.create_repository ? {
    for student in var.students : student.github_username => student
    if student.github_username != ""
  } : {}

  repository = github_repository.project[0].name
  username   = each.value.github_username
  permission = "maintain"
}

# Protect main branch - require pull requests
resource "github_branch_protection" "main" {
  count = var.create_repository ? 1 : 0

  repository_id = github_repository.project[0].name
  pattern       = "main"

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
