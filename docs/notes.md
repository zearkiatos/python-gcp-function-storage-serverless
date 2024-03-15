# Gcloud configuration serverless with storage

## Bucket configuration
```sh
# Bucket creation
# gsutil mb -p <PROJECT_ID> -c standard -l us-central1 -b on gs://<BUCKET_NAME>
gsutil mb -p miso-cloud-native-414617 -c standard -l us-central1 -b on gs://function-storage-caprilespe

```