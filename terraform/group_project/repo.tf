# Create GitHub repository for the project
resource "github_repository" "project" {
  name        = var.team_id
  description = "Group project repository for ${var.team_id}"
  visibility  = "public"

  has_issues             = true
  has_projects           = true
  has_wiki               = true
  auto_init              = false
  delete_branch_on_merge = true

  topics = ["advanced-computing", "group-project"]

  lifecycle {
    prevent_destroy = true
  }
}

# Add students as collaborators to the project repository
resource "github_repository_collaborator" "students" {
  for_each = {
    for student in var.students : student.github_username => student
  }

  repository = github_repository.project.name
  username   = each.value.github_username
  permission = "maintain"
}
