resource "google_project" "main" {
  name       = var.project_id
  project_id = var.project_id
  folder_id  = var.folder_id
  # deletion_policy = "DELETE"

  lifecycle {
    # we don't control the billing account, so ignore when set by the student
    ignore_changes = [billing_account]
    # safeguard to avoid deleting student work
    prevent_destroy = true
  }
}
