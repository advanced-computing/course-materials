import numpy as np
import pandas as pd
from profiling_helpers import parse_dollars


def test_parse_dollars():
    amounts = pd.Series(
        [
            "$1.00",
            "$55.78",
            None,
        ]
    )

    result = parse_dollars(amounts)
    expected = pd.Series(
        [
            1.00,
            55.78,
            np.nan,
        ]
    )

    # https://pandas.pydata.org/docs/reference/api/pandas.Series.equals.html
    assert result.equals(expected)
