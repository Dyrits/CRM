"""Module to generate random users."""
from faker import Faker


class User():
    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    @property
    def full_name(self):
        return f"{self.first_name}, {self.last_name}"

    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"


if __name__ == "__main__":
    fake = Faker(locale="fr_FR")
    for _ in range(10):
        user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        print(user)
        print(repr(user))
        print("-" * 10)
