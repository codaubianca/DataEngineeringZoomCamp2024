if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    green_taxi_df = pd.DataFrame()
    for month in range(1,13):
        if month < 10:
            month = "0" + str(month)
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month}.parquet"
        print(f"Loading {url}")
        new_df = pd.read_parquet(url)
        green_taxi_df = pd.concat([green_taxi_df, new_df])

    return green_taxi_df
