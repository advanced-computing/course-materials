output "students_without_github_username" {
  description = "List of students who don't have a GitHub username"
  value = [
    for student in local.roster : student
    if student.github_username == ""
  ]
}

output "repos_without_homepage" {
  description = "List of repositories without homepage URLs"
  value = [
    for team_id, project in module.projects : {
      team_id  = team_id
      name     = project.repository_info.name
      html_url = project.repository_info.html_url
    }
    if project.repository_info != null && (project.repository_info.homepage_url == null || project.repository_info.homepage_url == "")
  ]
}
