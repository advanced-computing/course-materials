## Setup

[ydata-profiling requires Python 3.13 or below.](https://github.com/ydataai/ydata-profiling/pull/1804)

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Viewing slides

They are built in [Remark](https://github.com/gnab/remark).

1. From the repository root, start the server.

   ```sh
   python3 -m http.server
   ```

1. Open http://localhost:8000/slides.html?file=lectures/lecture_01.md, replacing the file path as needed.

## Google Cloud setup

This only needs to be done once per semester.

1. If the number of students+instructors is larger than 20, [request a Project Quota increase](https://support.google.com/code/contact/project_quota_increase).
1. [Install Terraform](https://developer.hashicorp.com/terraform/install).
1. [Install `gcloud`](https://cloud.google.com/sdk/docs/install).
1. Set up `gcloud`:

   ```sh
   gcloud config configurations activate columbia
   gcloud auth application-default login
   ```

1. Ensure the [roster/project list](../semesters/spring_2026/) is up to date.
1. Run `terraform apply`.

As students go through the setup (below), you can re-run the `apply` to get a report of who is missing billing.
