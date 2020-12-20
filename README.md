# Text Alert Google Cloud Function using Twilio API

[![Build Status](https://travis-ci.org/nslocomotives/csv_clean_woocommerce_functions.svg?branch=main)](https://travis-ci.org/nslocomotives/csv_clean_woocommerce_functionsn)
![GitHub](https://img.shields.io/github/license/nslocomotives/csv_clean_woocommerce_functions)
![code compliance workflow](https://github.com/nslocomotives/csv_clean_woocommerce_functions/workflows/code%20compliance%20workflow/badge.svg?branch=main)

A [Google Cloud Function](https://cloud.google.com/functions/) that takes a csv from New Temptations and format it for import to [WooComerce](https://github.com/woocommerce/woocommerce/wiki/Product-CSV-Import-Schema#csv-columns-and-formatting).

## Example format of how the function is called by the Google cloud message queue

``{"filename":"something.csv","type":["simple","variation","virtual"]}``

## Deploy

### Google Cloud Functions
  * If you've never used gcloud or deployed a Cloud Function before, run through the [Quickstart](https://cloud.google.com/functions/docs/quickstart#functions-update-install-gcloud-python37) to make sure you have a GCP project with the Cloud Functions API enabled before proceeding.


  * Fork/clone this repo
  * Within the repo, deploy this cloud function with:

  ```console
  $ gcloud functions deploy csvCleanWooCommerce \
  --trigger-token=csvCleanWooCommerce \
  --runtime=python37 \
  --source=. \
  --project $(gcloud config list --format 'value(core.project)')
  ```


## Testing

### Prerequisites
* python37
* pytest
* pylint

### Unit tests
```console
$ pip install pytest pylint
$ pytest
$ pylint main.py
```

### Ad-hoc tests

```
To be done..
```

## Contributing
Contributions welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## License
This project is released under the ISC license, which can be found in [LICENSE](LICENSE).

## References
* Google Cloud Functions
  * [Pub\Sub Triggers](https://cloud.google.com/functions/docs/calling/pubsub)
  * [Using Secrets](https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#secretmanager-create-secret-python)
  * [Testing Background Functions](https://cloud.google.com/functions/docs/testing/test-background)
  * [Testing and CI/CD](https://cloud.google.com/functions/docs/bestpractices/testing)
* WooCommerce documentation that appears relevant
  * [CSV import format](https://github.com/woocommerce/woocommerce/wiki/Product-CSV-Import-Schema#csv-columns-and-formatting)
