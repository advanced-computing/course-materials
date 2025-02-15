from glob import glob

import pytest

labs = glob("labs/*")


@pytest.mark.parametrize("file", labs)
def test_submit_info(file):
    if "example" in file:
        pytest.skip("Skip examples")
    if file.endswith("/lab_01.md"):
        pytest.skip("Lab 1 doesn't have a separate submission")

    with open(file) as f:
        content = f.read()

    assert "/assignments" in content
