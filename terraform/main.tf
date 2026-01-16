terraform {
  required_version = "~>1.0"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

locals {
  root_project = "sipa-advanced-computing"
  region       = "us-central1"
}

provider "github" {
  owner = "advanced-computing"
}

provider "google" {
  project = local.root_project
  region  = local.region
}

locals {
  everyone_group             = "group:advanced-computing-for-policy-all@columbia.edu"
  roster                     = csvdecode(trimspace(file("${path.module}/../docs/roster.csv")))
  instructor_github_username = "afeld"
  ta_github_username         = "spalle1997"
}
