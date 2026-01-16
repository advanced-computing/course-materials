resource "github_team" "instructors" {
  name        = "instructors"
  description = "Instructor + TA"
  privacy     = "closed"
}

resource "github_team_members" "instructors" {
  team_id = github_team.instructors.id

  members {
    username = local.instructor_github_username
  }

  members {
    username = local.ta_github_username
  }
}

resource "github_team" "spring_2026" {
  name        = "spring-2026"
  description = "Spring 2026"
  privacy     = "closed"
}

resource "github_team_members" "spring_2026" {
  team_id = github_team.spring_2026.id

  dynamic "members" {
    for_each = compact([for student in local.roster : student["GitHub username"]])
    content {
      username = members.value
    }
  }
}
