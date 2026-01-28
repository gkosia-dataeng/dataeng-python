from faker import Faker
import json

def event_builder(fake: Faker) -> str:

    return json.dumps({
            "event_id": fake.uuid4(),
            "user_id": fake.random_int(min=1, max=50),
            "event_type": fake.random_element(["purchase", "invalid", "order", "deletion"]),
            "amount": fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            "timestamp": fake.date_time().isoformat()
        })
    

def produce_data(events_file_path: str, num_of_events: int) -> None:

    fake = Faker()
    
    with open(events_file_path, "w") as f:
         for _ in range(num_of_events):
            f.write(event_builder(fake) + "\n")