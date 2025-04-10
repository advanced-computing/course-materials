import functions_framework


from google.cloud import bigquery


@functions_framework.http
def list_datasets(request):
    # https://cloud.google.com/bigquery/docs/listing-datasets#list_datasets
    client = bigquery.Client()
    datasets = client.list_datasets()
    return [dataset.dataset_id for dataset in datasets]
