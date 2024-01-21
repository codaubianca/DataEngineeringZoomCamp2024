terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {
  project = "positive-rhino-411414"
  region  = "europe-west1-b"
}

# creates gcp storage bucket
resource "google_storage_bucket" "demo-bucket" {
  name          = "positive-rhino-411414-demo-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}