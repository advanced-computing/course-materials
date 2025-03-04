import pandas as pd


def parse_dollar(amounts: pd.Series):
    return amounts.str.replace('$',"").str.replace(",","").astype(float)

