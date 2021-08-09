"""Module to generate random users."""
from typing import List

from faker import Faker
import re
from tinydb import TinyDB, where
from pathlib import Path


class User:
    DB = TinyDB(Path(__file__).resolve().parent / "db.json", indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    @property
    def full_name(self):
        return f"{self.first_name}, {self.last_name}"

    @property
    def get(self):
        User.DB.get((where("first_name") == self.first_name) and (where("last_name") == self.last_name))
        return User.DB.get((where("first_name") == self.first_name) and (where("last_name") == self.last_name))

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

    def save(self, validate_data=False):
        if self.exists():
            return -1
        if validate_data:
            self.checks()
        return User.DB.insert(self.__dict__)

    def exists(self):
        return bool(self.get)

    def delete(self) -> List[int]:
        return User.DB.remove(doc_ids=[self.get.doc_id]) if self.exists() else []

    @classmethod
    def get_all_users(cls):
        return [User(**user) for user in cls.DB.all()]


if __name__ == "__main__":
    fake = Faker(locale="fr_FR")
    users = User.get_all_users()
    print(users)
