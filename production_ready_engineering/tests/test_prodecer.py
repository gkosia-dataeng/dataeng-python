from src.producer import producer 
from src.models.events import Event
from pydantic import ValidationError
from faker import Faker

def test_event_builder():
    fake = Faker()
    json_event_str = producer.event_builder(fake)

    try:
        Event.parse_raw(json_event_str)
    except ValidationError as v:
        raise AssertionError(f"Schema does not match Event obj: {v}")

