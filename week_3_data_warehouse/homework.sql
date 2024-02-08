-- Setup

CREATE OR REPLACE EXTERNAL TABLE `positive-rhino-411414.ny_taxi.external_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://week_3_data_warehouse/green_taxi_2022_data.parquet']
);

CREATE OR REPLACE TABLE `positive-rhino-411414.ny_taxi.green_tripdata_non_partitioned` AS
SELECT * FROM `positive-rhino-411414.ny_taxi.external_green_tripdata`;

-- Question 1
SELECT count(*)
FROM `positive-rhino-411414.ny_taxi.green_tripdata_non_partitioned`;

-- Question 2
SELECT count(distinct(PULocationID))
FROM `positive-rhino-411414.ny_taxi.green_tripdata_non_partitioned`;


SELECT count(distinct(PULocationID))
FROM `positive-rhino-411414.ny_taxi.external_green_tripdata`;


-- Question 3
SELECT count(*)
FROM `positive-rhino-411414.ny_taxi.green_tripdata_non_partitioned`
WHERE fare_amount = 0;

-- Question 4
CREATE OR REPLACE TABLE `positive-rhino-411414.ny_taxi.green_tripdata_partitoned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `positive-rhino-411414.ny_taxi.green_tripdata_non_partitioned`;

-- Question 5
SELECT count(distinct(PULocationID))
FROM `positive-rhino-411414.ny_taxi.green_tripdata_non_partitioned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

SELECT count(distinct(PULocationID))
FROM `positive-rhino-411414.ny_taxi.green_tripdata_partitoned_clustered`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- Bonus Question
SELECT count(*)
FROM `positive-rhino-411414.ny_taxi.green_tripdata_non_partitioned`;