from glob import glob

import pytest

readings = glob("readings/*")
lab_assignments = glob("labs/assignments/*")

LABS_WITHOUT_SUBMISSION = [1, 12]


def read_file(path):
    with open(path) as f:
        return f.read()


@pytest.mark.parametrize("file", readings)
def test_readings_boilerplate(file):
    content = read_file(file)
    assert "[General information](../README.md#readings)" in content
    assert "[submit a response](../README.md#responses)" in content


@pytest.mark.parametrize("file", lab_assignments)
def test_lab_submit_info(file):
    if "example" in file:
        pytest.skip("Skip examples")
    for skip_lab in LABS_WITHOUT_SUBMISSION:
        if file.endswith(f"/lab_{skip_lab:02}.md"):
            pytest.skip(f"Lab {skip_lab} doesn't have a separate submission")

    content = read_file(file)
    assert "/assignments" in content or "submit" in content.lower()
