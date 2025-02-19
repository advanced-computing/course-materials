resource "google_folder" "projects" {
  display_name = "SIPA Advanced Computing"
  parent       = "organizations/378073203623" # afeld.me
}

locals {
  student_groups = csvdecode(file("${path.module}/../docs/project_teams.csv"))
  # first1-first2-first3
  student_group_ids = [for g in local.student_groups : lower(join("-", compact([
    g.student_1_first,
    g.student_2_first,
    g.student_3_first,
  ])))]
}

module "projects" {
  for_each = toset(local.student_group_ids)

  source     = "./group_project"
  folder_id  = google_folder.projects.id
  project_id = each.key
}
