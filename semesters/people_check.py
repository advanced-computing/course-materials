import pandas as pd

INSTRUCTOR_UNIS = set(["alf2215", "sp4434"])

vergil = pd.read_csv("~/Downloads/DSPC7160U001-roster.csv", skiprows=2)
cic_sec_1 = pd.read_csv("~/Downloads/DSPC6000U001-roster.csv", skiprows=2)
cic_sec_2 = pd.read_csv("~/Downloads/DSPC6000U002-roster.csv", skiprows=2)
grouper = pd.read_csv(
    "~/Downloads/groupExportSubjectIds_advanced-computing-for-policy-all.csv"
)
repo = pd.read_csv("semesters/spring_2026/people.csv")

vergil_unis = set(vergil["UNI"])
cic_unis = set(cic_sec_1["UNI"]) | set(cic_sec_2["UNI"])
grouper_unis = set(grouper["entityId"])
repo_unis = set(repo["uni"])

print("Add to Grouper:", vergil_unis - grouper_unis)
print("Remove from Grouper:", grouper_unis - vergil_unis - INSTRUCTOR_UNIS)

print("Add to repo:", vergil_unis - repo_unis)
print("Remove from repo:", repo_unis - vergil_unis - INSTRUCTOR_UNIS)

print("Didn't take Computing in Context last term:", vergil_unis - cic_unis)
