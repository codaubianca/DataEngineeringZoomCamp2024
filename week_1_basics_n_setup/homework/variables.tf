variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my_creds.json"
}

variable "project" {
  description = "Project Name"
  default     = "positive-rhino-411414"
}

variable "region" {
  description = "Region"
  default     = "europe-west1-b"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "positive-rhino-411414-demo-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}