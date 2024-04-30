import logging
import pandas as pd

from zenml import step


@step
def clean_df(df: pd.DataFrame) -> None:
    pass


# @zenml.step
# def clean_data(df:pd.DataFrame) -> pd.DataFrame:
