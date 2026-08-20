# Enterprise Data Pipeline

Production-style batch ETL pipeline demonstrating ingestion, validation, transformation, dimensional modeling, and orchestration.

## Stack
- Python / Pandas
- SQL
- PySpark
- Apache Airflow
- AWS S3 concepts
- Snowflake-ready warehouse model
- Docker
- GitHub Actions

## Architecture
Source files/API → ingestion → validation → PySpark transformation → warehouse tables → data quality checks → reporting.

## Project Goals
- Build reusable ETL components
- Support incremental processing
- Apply schema and data-quality validation
- Create analytics-ready dimensional models
- Add automated testing and CI

## Structure
```text
src/        pipeline modules
sql/        warehouse schemas and transformations
tests/      unit tests
airflow/    DAGs
docker/     container configuration
```
