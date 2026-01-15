# CUIT doesn't want the projects to exist under the columbia.edu Google Cloud organization, which they manage. Also, don't seem to be able to create in No Organization, due to:
# https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations
# Therefore, create under a different domain.

data "google_organization" "org" {
  domain = "afeld.me"
}

resource "google_organization_iam_member" "org_viewer" {
  org_id = data.google_organization.org.org_id
  role   = "roles/resourcemanager.organizationViewer"
  member = local.everyone_group
}

resource "google_folder" "group_projects" {
  display_name = "SIPA Advanced Computing"
  parent       = data.google_organization.org.name
}

resource "google_folder_iam_member" "project_creator" {
  folder = google_folder.group_projects.name
  role   = "roles/resourcemanager.projectCreator"
  member = local.everyone_group
}
