# Interview Guide

## Architecture
- Why this architecture? Separate ingestion, validation, transformation, and warehouse layers for maintainability and observability.
- How would you scale it? Partition input, parallelize Spark work, use incremental loads, and optimize warehouse clustering/indexes.

## Reliability
- How are failures handled? Validate before transformation, fail fast on schema violations, use Airflow retries, and make loads idempotent.
- How would you monitor it? Track row counts, null rates, freshness, task duration, and failed records.

## Production extensions
- Store raw data in S3 before transformation.
- Use Snowflake staging and MERGE for incremental loads.
- Add Great Expectations or equivalent data-quality checks.
- Add secrets through environment variables or a cloud secret manager.
