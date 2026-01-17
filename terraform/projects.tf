# Was getting the following error locally:
#
#   Your application is authenticating by using local Application Default Credentials. The orgpolicy.googleapis.com API requires a quota project, which is not set by default. To learn how to set your quota project, see https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds.
#
# Set manually through the Console instead.
# https://cloud.google.com/iam/docs/keys-create-delete#allow-creation
# resource "google_org_policy_policy" "allow_keys" {
#   name   = "${google_folder.course.name}/policies/iam.disableServiceAccountKeyCreation"
#   parent = google_folder.course.name

#   spec {
#     inherit_from_parent = false

#     rules {
#       enforce = "FALSE"
#     }
#   }
# }

locals {
  # Group students by team_id, filtering out those without a team
  students_by_team_id = {
    for team_id, students in merge([
      for student in local.roster :
      student.team_id != "" ? { "${student.team_id}" = [student] } : {}
    ]...) :
    team_id => students
  }

  ta_member = "user:${local.ta_uni}@columbia.edu"
}

module "projects" {
  for_each = local.students_by_team_id

  source         = "./group_project"
  folder_id      = google_folder.spring_2026.id
  team_id        = each.key
  students       = each.value
  everyone_group = local.everyone_group
  ta_member      = local.ta_member
}

module "ta_project" {
  source            = "./group_project"
  folder_id         = google_folder.spring_2026.id
  team_id           = local.ta_uni
  create_repository = false
  students          = []
  everyone_group    = local.everyone_group
  ta_member         = local.ta_member
}

# demo project

resource "random_id" "demo_project_id" {
  byte_length = 2
}

module "demo_project" {
  source            = "./group_project"
  folder_id         = google_folder.spring_2026.id
  team_id           = "aidan-demo-${random_id.demo_project_id.hex}"
  create_repository = false
  allow_destroy     = true
  students          = []
  everyone_group    = local.everyone_group
  ta_member         = local.ta_member
}
