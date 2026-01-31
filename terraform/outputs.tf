output "students_without_github_username" {
  description = "List of students who don't have a GitHub username"
  value = [
    for student in local.roster : student
    if student.github_username == ""
  ]
}
