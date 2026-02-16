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
    secret_scanning_push_protection {
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
  permission = "admin"
}

# Protect main branch using repository ruleset
resource "github_repository_ruleset" "main" {
  count = var.create_repository ? 1 : 0

  name        = "Protect main branch"
  repository  = github_repository.project[0].name
  target      = "branch"
  enforcement = "active"

  conditions {
    ref_name {
      include = ["~DEFAULT_BRANCH"]
      exclude = []
    }
  }

  bypass_actors {
    actor_id    = var.instructors_team_id
    actor_type  = "Team"
    bypass_mode = "always"
  }

  rules {
    # Require pull requests with review from another collaborator
    pull_request {
      required_approving_review_count = 1
      dismiss_stale_reviews_on_push   = false
      require_code_owner_review       = false
      require_last_push_approval      = false
    }

    # Prevent force pushes
    non_fast_forward = true

    # Prevent branch deletion
    deletion = true
  }
}
