locals {
  unis = compact([var.group.student_1_uni, var.group.student_2_uni, var.group.student_3_uni])
}

resource "google_project_iam_member" "student" {
  for_each = toset(local.unis)

  project = google_project.main.project_id
  role    = "roles/admin"
  member  = "user:${each.value}@columbia.edu"
}

# creator (user running Terraform) automatically added as an Owner
# https://cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectCreator

# resource "google_project_iam_member" "instructor" {
#   project = google_project.main.project_id
#   role    = "roles/admin"
#   member  = "user:alf2215@columbia.edu"
# }

resource "google_project_iam_member" "ta" {
  project = google_project.main.project_id
  role    = "roles/admin"
  member  = var.ta_member
}

resource "google_project_iam_member" "everyone_data_viewer" {
  project = google_project.main.project_id
  role    = "roles/bigquery.dataViewer"
  member  = "group:advanced-computing-for-policy-all@columbia.edu"
}
