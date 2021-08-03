"""Module to generate random users."""
from faker import Faker
import re


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

    def checks(self):
        self._check_phone_number()
        self._check_names()

    def _check_phone_number(self):
        phone_digits = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_digits) < 10 or not phone_digits.isdigit():
            raise ValueError(f"Le numéro de téléphone {self.phone_number} est invalide.")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError(f"Le prénom et/ou le nom de famille ne peuvent pas être vides.")
        if not (self.first_name + self.last_name).isalpha():
            raise ValueError(f"Le nom {self.full_name} est invalide.")


if __name__ == "__main__":
    fake = Faker(locale="fr_FR")
    for _ in range(10):
        user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        user.checks()
        print(user)
        print(repr(user))
        print("-" * 10)
