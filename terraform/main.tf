terraform {
  required_version = "~>1.0"
}

locals {
  root_project = "sipa-advanced-computing"
  region       = "us-central1"
}

provider "google" {
  project = local.root_project
  region  = local.region
}
