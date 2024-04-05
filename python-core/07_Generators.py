from faker import Faker

def generate_1000customers():
    faker = Faker()

    for c in range(1000):
        yield {"name": faker.name(), "age": faker.random_int(18, 80)}



all_customers =   generate_1000customers()

try:
    print(next(all_customers))
    print(next(all_customers))
    print(next(all_customers))
except StopIteration:
    print("No more customers")

