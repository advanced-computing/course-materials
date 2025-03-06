resource "random_id" "demo_project_id" {
  prefix      = "sipa-adv-c-aidan-demo-"
  byte_length = 2
}

resource "google_project" "demo" {
  name       = random_id.demo_project_id.hex
  project_id = random_id.demo_project_id.hex
  folder_id  = google_folder.group_projects.id
  # Billing Account for Education
  billing_account = "012E43-0DE36B-6DD968"
  # deletion_policy = "DELETE"
}
