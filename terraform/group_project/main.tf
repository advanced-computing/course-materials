terraform {
  required_providers {
    github = {
      source = "integrations/github"
    }
  }
}

locals {
  project_id = "sipa-adv-c-${var.team_id}"
}

resource "google_project" "main" {
  name       = local.project_id
  project_id = local.project_id
  folder_id  = var.folder_id
  # safeguard to avoid deleting student work
  deletion_policy = var.allow_destroy ? "DELETE" : "PREVENT"

  lifecycle {
    # we don't control the billing account, so ignore when set by the student
    ignore_changes = [billing_account]
    # prevent_destroy = true
  }
}
