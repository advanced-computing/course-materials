variable "folder_id" {
  type = string
}

variable "project_id" {
  type = string
}

variable "group" {
  type = object({
    student_1_first = string
    student_1_last  = string
    student_1_uni   = string
    student_2_first = string
    student_2_last  = string
    student_2_uni   = string
    student_3_first = string
    student_3_last  = string
    student_3_uni   = string
  })
}
