# Gcloud configuration serverless with storage

## Bucket configuration
```sh
# Bucket creation
# gsutil mb -p <PROJECT_ID> -c standard -l us-central1 -b on gs://<BUCKET_NAME>
gsutil mb -p miso-cloud-native-414617 -c standard -l us-central1 -b on gs://function-storage-caprilespe

```

## Create a function with a bucket storage environment

```sh
# gcloud functions deploy function-heroes-storage-create --entry-point create_heroe --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --set-env-vars BUCKETNAME=<BUCKET_NAME>
$ gcloud functions deploy function-heroes-storage-create --entry-point create_heroe --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --set-env-vars BUCKETNAME=function-storage-caprilespe
```

gcloud functions deploy function-heroes-storage-details --entry-point heroe_detail --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --set-env-vars BUCKETNAME=function-storage-caprilespe