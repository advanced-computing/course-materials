variable "folder_id" {
  type = string
}

variable "project_id" {
  type = string
}

variable "allow_destroy" {
  default = false
}

variable "everyone_group" {
  type = string
}

variable "ta_member" {
  type = string
}

variable "students" {
  type = list(object({
    first_name      = string
    last_name       = string
    uni             = string
    github_username = string
  }))
}
