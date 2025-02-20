import pandas as pd


def parse_dollars(amounts: pd.Series):
    return amounts.str.replace("$", "").str.replace(",", "").astype(float)
