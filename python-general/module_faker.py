from faker import Faker


faker = Faker()

for i in range(10):
    print(f"My name is {faker.name()}, my phone is {faker.phone_number()} and i said: {faker.text()}")