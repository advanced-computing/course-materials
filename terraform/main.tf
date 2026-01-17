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
  everyone_group = "group:advanced-computing-for-policy-all@columbia.edu"
  roster         = csvdecode(trimspace(file("${path.module}/../semesters/spring_2026/people.csv")))

  instructor_uni             = "alf2215"
  ta_uni                     = "sp4434"
  instructor_github_username = one([for user in local.roster : user.github_username if user.uni == local.instructor_uni])
  ta_github_username         = one([for user in local.roster : user.github_username if user.uni == local.ta_uni])
}
