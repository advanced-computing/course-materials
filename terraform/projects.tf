# CUIT doesn't want the projects to exist under the columbia.edu Google Cloud organization, which they manage. Also, don't seem to be able to create in No Organization, due to:
# https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations
# Therefore, create under a different domain.

data "google_organization" "org" {
  domain = "afeld.me"
}

resource "google_folder" "group_projects" {
  display_name = "SIPA Advanced Computing"
  parent       = data.google_organization.org.name
}

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
  folder_id  = google_folder.group_projects.id
  project_id = "sipa-adv-c-${each.key}"
  group      = each.value
}
