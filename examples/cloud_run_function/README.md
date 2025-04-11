Deploying from the command line:

```sh
gcloud functions deploy list-datasets \
 --gen2 \
 --region=us-central1 \
 --runtime=python312 \
 --source=. \
 --entry-point=list_datasets \
 --trigger-http \
 --allow-unauthenticated
```
