resource "github_team" "spring_2026" {
  name        = "spring-2026"
  description = "Spring 2026"
  privacy     = "closed"
}

resource "github_team_members" "spring_2026" {
  team_id = github_team.spring_2026.id

  dynamic "members" {
    for_each = compact(local.roster[*].github_username)
    content {
      username = members.value
      role     = members.value == local.instructor_github_username ? "maintainer" : "member"
    }
  }
}
