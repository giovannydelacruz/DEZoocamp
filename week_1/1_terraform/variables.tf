variable "credentials" {
  description = "The path to the service account key file"
  default     = "./keys/my-creds.json"
}

variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset"
  default     = "demo_dataset"
}

variable "gcs_storage_class" {
  description = "The storage class of the GCS bucket"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  default     = "terraform-demo-449117-terra-bucket"
}

variable "location" {
  description = "The location of the GCS bucket"
  default     = "EU"
}

variable "project" {
  description = "The GCP project ID"
  default     = "terraform-demo-449117"
}

variable "region" {
  description = "The region of the GCS bucket"
  default     = "europe-west1"
}