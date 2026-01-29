import pandas as pd

INSTRUCTOR_UNIS = set(["alf2215", "sp4434"])

vergil = pd.read_csv("~/Downloads/DSPC7160U001-roster.csv", skiprows=2)
grouper = pd.read_csv(
    "~/Downloads/groupExportSubjectIds_advanced-computing-for-policy-all.csv"
)
repo = pd.read_csv("semesters/spring_2026/people.csv")

vergil_unis = set(vergil["UNI"])
grouper_unis = set(grouper["entityId"])
repo_unis = set(repo["uni"])

print("Add to Grouper:", vergil_unis - grouper_unis)
print("Remove from Grouper:", grouper_unis - vergil_unis - INSTRUCTOR_UNIS)

print("Add to repo:", vergil_unis - repo_unis)
print("Remove from repo:", repo_unis - vergil_unis - INSTRUCTOR_UNIS)
