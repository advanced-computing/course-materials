from glob import glob

import pandas as pd
import pytest

readings = glob("readings/*")
labs = glob("labs/*")
rosters = glob("semesters/**/people.csv")


LABS_WITHOUT_SUBMISSION = [1, 12]

# sanity check
for files in [readings, labs, rosters]:
    assert len(files) > 0


def read_file(path):
    with open(path) as f:
        return f.read()


@pytest.mark.parametrize("file", readings)
def test_readings_boilerplate(file):
    content = read_file(file)
    assert "[General information](../README.md#readings)" in content
    assert "[submit a response](../README.md#responses)" in content


@pytest.mark.parametrize("file", labs)
def test_lab_submit_info(file):
    if "example" in file:
        pytest.skip("Skip examples")
    if "slides" in file:
        pytest.skip("Skip slides")
    for skip_lab in LABS_WITHOUT_SUBMISSION:
        if file.endswith(f"/lab_{skip_lab:02}.md"):
            pytest.skip(f"Lab {skip_lab} doesn't have a separate submission")

    content = read_file(file)
    assert "/assignments" in content or "submit" in content.lower()


@pytest.mark.parametrize("file", rosters)
def test_roster_is_valid_csv(file):
    pd.read_csv(file)
