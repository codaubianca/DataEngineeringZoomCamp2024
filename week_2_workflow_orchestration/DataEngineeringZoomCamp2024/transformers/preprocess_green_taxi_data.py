from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
import pandas as pd
import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def create_date_column(df: DataFrame) -> DataFrame:
    df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime'].dt.date)
    return df

def camel_to_snake(camel_case):
    pattern = re.compile(r'([a-z0-9])([A-Z])')
    snake_case = re.sub(pattern, r'\1_\2', camel_case)
    return snake_case.lower()

def remove_rows(df: DataFrame) -> DataFrame:
    df = df[df['passenger_count'] > 0]
    df = df[df['trip_distance'] > 0]
    return df

@transformer
def transform_df(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Args:
        df (DataFrame): Data frame from parent block.

    Returns:
        DataFrame: Transformed data frame
    """
    df = remove_rows(df)
    print("Number of rows: ", df.shape[0])
    df.columns = [camel_to_snake(col) for col in df.columns]
    df = create_date_column(df)
    print(set(df["vendor_id"].values))

    return df

@test
def test_output_passenger_count(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, "Passenger count is zero"

@test
def test_output_trip_distance(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['trip_distance'].isin([0]).sum() == 0, "Trip distance is zero"

@test
def test_output_snake_case(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert "vendor_id" in output.columns, "Camel case still exisits"

@test
def test_output_not_none(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
