# Architecture

```mermaid
flowchart LR
  A[CSV / API Sources] --> B[Landing / S3]
  B --> C[Airflow DAG]
  C --> D[Python Validation]
  D --> E[PySpark Transformations]
  E --> F[Warehouse Fact / Dimensions]
  F --> G[SQL Analytics]
  G --> H[BI / Reporting]
```

## Reliability
- Idempotent order processing using `order_id` as the business key.
- Schema validation before transformation.
- Invalid timestamps are quarantined by the transformation layer.
- CI executes automated tests on every push.
