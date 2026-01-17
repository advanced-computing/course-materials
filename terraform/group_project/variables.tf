variable "folder_id" {
  type = string
}

variable "team_id" {
  type = string
}

variable "create_repository" {
  type    = bool
  default = true
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
