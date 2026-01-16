# instructors

resource "github_team" "instructors" {
  name        = "instructors"
  description = "Instructor + TA"
  privacy     = "closed"
}

resource "github_team_members" "instructors" {
  team_id = github_team.instructors.id

  members {
    username = local.instructor_github_username
    role     = "maintainer"
  }

  members {
    username = local.ta_github_username
  }
}

data "github_organization_roles" "all" {}

locals {
  # https://github.com/integrations/terraform-provider-github/issues/2981#issuecomment-3650644640
  all_repo_admin_id = one([for x in data.github_organization_roles.all.roles : x.role_id if x.name == "all_repo_admin"])
}

resource "github_organization_role_team" "instructors" {
  role_id   = local.all_repo_admin_id
  team_slug = github_team.instructors.slug
}

# students

resource "github_team" "spring_2026" {
  name        = "spring-2026"
  description = "Spring 2026"
  privacy     = "closed"
}

resource "github_team_members" "spring_2026" {
  team_id = github_team.spring_2026.id

  dynamic "members" {
    for_each = compact(local.roster[*]["GitHub username"])
    content {
      username = members.value
      role     = members.value == local.instructor_github_username ? "maintainer" : "member"
    }
  }
}

# primary repo

resource "github_repository_collaborators" "course_materials_collaborators" {
  repository = "course-materials"

  team {
    team_id    = github_team.instructors.slug
    permission = "admin"
  }

  team {
    team_id = github_team.spring_2026.slug
  }
}
