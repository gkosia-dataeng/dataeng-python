# Event processing Pipeline (Python)

## Producer
Produce fake data to files using Faker, following this structure:

Event schema (JSON):
    ```
        {
            "event_id": "uuid",
            "user_id": 123,
            "event_type": "purchase",
            "amount": 49.99,
            "timestamp": "2025-01-20T10:15:00Z"
        }
    ```

## Data Ingestion
- Idempotent
- Handles bad files / bad records
- Logs counts

## Validation
- Schema validation
- Reject invalid data
- Unit-testable

## Transformation
- Convert timestamps to UTC
- Add event date
- Normalize event types
- Drop invalid business cases (purchase without amount)

## Storage
- Write to database (SQLite)
- Batch inserts
- Retry logic

## Software Engineer Best Practices

### Testing
- Test business logic
- Unit tests for Validation and Transformations

### Logging
- info, warning

### Error Handling
- Custom exceptions
- Dead-letter for bad events

### Configuration Management
- Pydantic settings

### CI
- Run tests
- Run linters
- Enforce formatting

## Tooling
- Data producer: Generate JSON events into /source_data
- Data validation: Pydantic
- Logging: logging
- Testing: pytest
- Lint: ruff
- Config: .env + Pydantic settings