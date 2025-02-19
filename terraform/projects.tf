locals {
  student_groups = csvdecode(file("${path.module}/../docs/project_teams.csv"))
  # first1-first2-first3
  student_groups_by_id = { for group in local.student_groups : lower(join("-", compact([
    group.student_1_first,
    group.student_2_first,
    group.student_3_first,
  ]))) => group }
}

module "projects" {
  for_each = local.student_groups_by_id

  source     = "./group_project"
  project_id = "adv-comp-${each.key}"
  group      = each.value
}
