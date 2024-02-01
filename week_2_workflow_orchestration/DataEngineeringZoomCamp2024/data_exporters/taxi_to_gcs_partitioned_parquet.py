import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/keys/positive-rhino-411414-837fae5602f4.json"
bucket_name = 'mage-ai-ny-tdaxi-bucket'
project_id = 'positive-rhino-411414'
table_name = 'nyc_taxi_data_partitioned'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    print("Exporting data...")
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date
    print("Converting to pandas")
    table = pa.Table.from_pandas(data)
    print("Grab gcs fs")
    gcs = pa.fs.GcsFileSystem()
    print("write to dataset")
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['tpep_pickup_date'],
        filesystem=gcs
    )