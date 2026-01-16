# Was getting the following error locally:
#
#   Your application is authenticating by using local Application Default Credentials. The orgpolicy.googleapis.com API requires a quota project, which is not set by default. To learn how to set your quota project, see https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds.
#
# Set manually through the Console instead.
# https://cloud.google.com/iam/docs/keys-create-delete#allow-creation
# resource "google_org_policy_policy" "allow_keys" {
#   name   = "${google_folder.group_projects.name}/policies/iam.disableServiceAccountKeyCreation"
#   parent = google_folder.group_projects.name

#   spec {
#     inherit_from_parent = false

#     rules {
#       enforce = "FALSE"
#     }
#   }
# }

locals {
  student_groups = csvdecode(trimspace(file("${path.module}/../docs/project_teams.csv")))
  # first1-first2-first3
  student_groups_by_id = { for group in local.student_groups : lower(join("-", compact([
    group.student_1_first,
    group.student_2_first,
    group.student_3_first,
  ]))) => group }

  ta_member = "user:sp4434@columbia.edu"
}

locals {
  no_students = {
    student_1_first = null
    student_1_last  = null
    student_1_uni   = null
    student_2_first = null
    student_2_last  = null
    student_2_uni   = null
    student_3_first = null
    student_3_last  = null
    student_3_uni   = null
  }
}

module "projects" {
  for_each = local.student_groups_by_id

  source         = "./group_project"
  folder_id      = google_folder.group_projects.id
  project_id     = each.value.google_cloud_project_id
  group          = each.value
  everyone_group = local.everyone_group
  ta_member      = local.ta_member
}

# module "ta_project" {
#   for_each = toset(["sneha"])

#   source         = "./group_project"
#   folder_id      = google_folder.group_projects.id
#   project_id     = "sipa-adv-c-${each.value}"
#   group          = local.no_students
#   everyone_group = local.everyone_group
#   ta_member      = local.ta_member
# }

# demo project

# resource "random_id" "demo_project_id" {
#   prefix      = "sipa-adv-c-aidan-demo-"
#   byte_length = 2
# }

# module "demo_project" {
#   source         = "./group_project"
#   folder_id      = google_folder.group_projects.id
#   project_id     = random_id.demo_project_id.hex
#   allow_destroy  = true
#   group          = local.no_students
#   everyone_group = local.everyone_group
#   ta_member      = local.ta_member
# }
