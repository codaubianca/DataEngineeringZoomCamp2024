# Data Warehouse and BigQuery

- [Slides](https://docs.google.com/presentation/d/1a3ZoBAXFk8-EhUsd7rAZd-5p_HpltkzSeujjRGB2TAI/edit?usp=sharing)  
- [Big Query basic SQL](big_query.sql)

# Videos

## Data Warehouse

- Data Warehouse and BigQuery

[![](https://markdown-videos-api.jorgenkh.no/youtube/jrHljAoD6nM)](https://youtu.be/jrHljAoD6nM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=34)

- Data Warehouse: OLAP solution for reporting and data analysis
#### BigQuery 
- has open data   
    -- Query public available table  
        SELECT station_id, name  
        FROM bigquery-public-data.new_york_citibike.citibike_stations  
        LIMIT 100;  

- can access google storage buckets:  
    -- Creating external table referring to gcs path  
        CREATE OR REPLACE EXTERNAL TABLE `taxi-rides-ny.nytaxi.external_yellow_tripdata`  
        OPTIONS (  
            format = 'CSV',  
            uris = ['gs://nyc-tl-data/trip data/yellow_tripdata_2019-*.csv', 'gs://nyc-tl-data/trip data/yellow_tripdata_2020-*.csv']  
        );  
        
- can partition and cluster tables  
    -- Creating a partition and cluster table  
        CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered  
        PARTITION BY DATE(tpep_pickup_datetime)  
        CLUSTER BY VendorID AS  
        SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;  

## :movie_camera: Partitoning and clustering

- Partioning and Clustering

[![](https://markdown-videos-api.jorgenkh.no/youtube/-CqXf7vhhDs)](https://youtu.be/-CqXf7vhhDs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=35)

- Partioning vs Clustering

[![](https://markdown-videos-api.jorgenkh.no/youtube/-CqXf7vhhDs)](https://youtu.be/-CqXf7vhhDs?si=p1sYQCAs8dAa7jIm&t=193&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=35)

## :movie_camera: Best practices

[![](https://markdown-videos-api.jorgenkh.no/youtube/k81mLJVX08w)](https://youtu.be/k81mLJVX08w&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=36)

## :movie_camera: Internals of BigQuery

[![](https://markdown-videos-api.jorgenkh.no/youtube/eduHi1inM4s)](https://youtu.be/eduHi1inM4s&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=37)

## Advanced topics

### :movie_camera: Machine Learning in Big Query

[![](https://markdown-videos-api.jorgenkh.no/youtube/B-WtpB0PuG4)](https://youtu.be/B-WtpB0PuG4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=34)

* [SQL for ML in BigQuery](big_query_ml.sql)

**Important links**

- [BigQuery ML Tutorials](https://cloud.google.com/bigquery-ml/docs/tutorials)
- [BigQuery ML Reference Parameter](https://cloud.google.com/bigquery-ml/docs/analytics-reference-patterns)
- [Hyper Parameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-glm)
- [Feature preprocessing](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-preprocess-overview)

### :movie_camera: Deploying Machine Learning model from BigQuery

[![](https://markdown-videos-api.jorgenkh.no/youtube/BjARzEWaznU)](https://youtu.be/BjARzEWaznU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=39)

- [Steps to extract and deploy model with docker](extract_model.md)  



# Homework

* [2024 Homework](../cohorts/2024/03-data-warehouse/homework.md)


# Community notes

Did you take notes? You can share them here.

* [Notes by Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/3_data_warehouse.md)
* [Isaac Kargar's blog post](https://kargarisaac.github.io/blog/data%20engineering/jupyter/2022/01/30/data-engineering-w3.html)
* [Marcos Torregrosa's blog post](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-3/) 
* [Notes by Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week3)
* [Notes from Xia He-Bleinagel](https://xiahe-bleinagel.com/2023/02/week-3-data-engineering-zoomcamp-notes-data-warehouse-and-bigquery/)
* [Bigger picture summary on Data Lakes, Data Warehouses, and tooling](https://medium.com/@verazabeida/zoomcamp-week-4-b8bde661bf98), by Vera
* [Notes by froukje](https://github.com/froukje/de-zoomcamp/blob/main/week_3_data_warehouse/notes/notes_week_03.md)
* [Notes by Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week3.md)
* [Notes from Vincenzo Galante](https://binchentso.notion.site/Data-Talks-Club-Data-Engineering-Zoomcamp-8699af8e7ff94ec49e6f9bdec8eb69fd)
* [2024 videos transcript week3](https://drive.google.com/drive/folders/1quIiwWO-tJCruqvtlqe_Olw8nvYSmmDJ?usp=sharing) by Maria Fisher 
* [Notes by Linda](https://github.com/inner-outer-space/de-zoomcamp-2024/blob/main/3-data-warehouse/readme.md)
* Add your notes here (above this line)