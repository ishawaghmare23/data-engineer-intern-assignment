from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.crawler import crawl_website
from src.extractor import extract_sections
from src.transformer import transform_to_records, save_processed_data
from src.aggregator import aggregate_metrics

import os


WEBSITES = [
    "https://example.com",
    "https://stripe.com",
    "https://slack.com"
]


def crawl_task():
    for site in WEBSITES:
        crawl_website(site)


def process_task():
    for site in WEBSITES:
        domain = site.replace("https://", "").replace("/", "")

        raw_file = f"data/raw/{domain}/homepage.html"
        if not os.path.exists(raw_file):
            continue

        with open(raw_file, "r", encoding="utf-8") as f:
            html = f.read()

        sections = extract_sections(html)
        records = transform_to_records(site, sections)
        save_processed_data(domain, records)


with DAG(
    dag_id="website_data_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    retries=2
) as dag:

    crawl = PythonOperator(
        task_id="crawl_websites",
        python_callable=crawl_task
    )

    process = PythonOperator(
        task_id="extract_transform",
        python_callable=process_task
    )

    aggregate = PythonOperator(
        task_id="aggregate_metrics",
        python_callable=aggregate_metrics
    )

    crawl >> process >> aggregate
