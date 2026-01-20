# Data Engineer Intern – Website Content Pipeline

## Overview
This project implements an end-to-end data engineering pipeline that crawls company websites, extracts structured content, standardizes the data, and computes analytics metrics. The workflow is orchestrated using Apache Airflow.

## Pipeline Steps
1.Crawling : Fetches raw HTML from company websites and stores it in an S3-like raw zone.
2.Extraction & Tagging: Extracts navbar, homepage, footer, and case study content using heuristic rules.
3.Transformation: Converts extracted data into standardized records.
4.Aggregation: Computes analytics metrics such as content length and website activity.
5.Orchestration: Uses an Airflow DAG to define task dependencies and retries.

## Design Decisions
- Simple requests-based crawling for reliability
- Separation of raw, processed, and aggregated data
- Graceful handling of missing sections
- Idempotent pipeline design

## Failure Handling
- HTTP timeouts during crawling
- Empty sections handled safely
- Airflow retries configured

## Scaling Considerations
- Website list can be dynamically sourced
- Storage can be migrated to S3
- Parallelism can be added using Airflow task mapping

## Tech Stack
- Python
- BeautifulSoup
- Apache Airflow

## Author
Isha
