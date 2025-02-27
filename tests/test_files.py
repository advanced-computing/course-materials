from glob import glob

import pytest

readings = glob("readings/*")
labs = glob("labs/*")


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
    for skip_lab in [1]:
        if file.endswith(f"/lab_{skip_lab:02}.md"):
            pytest.skip(f"Lab {skip_lab} doesn't have a separate submission")

    content = read_file(file)
    assert "/assignments" in content
