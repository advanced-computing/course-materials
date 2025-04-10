```sh
gcloud functions deploy hello-world \
 --gen2 \
 --region=us-central1 \
 --runtime=python312 \
 --source=. \
 --entry-point=list_datasets \
 --trigger-http \
 --allow-unauthenticated
```

Get a warning:

> The default build service account \[981748110194-compute@developer.gserviceaccount.com\] is missing the \[roles/cloudbuild.builds.builder\] role.

```sh
gcloud projects add-iam-policy-binding sipa-adv-c-aidan-demo-3b12 \
 --member=serviceAccount:981748110194-compute@developer.gserviceaccount.com \
 --role=roles/cloudbuild.builds.builder
```
