import re
import string

class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self) -> str:
        return f"User('{self.first_name}', '{self.last_name}')"

    def __str__(self) -> str:
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", '', self.phone_number)
        if len(phone_number) < 10 and phone_number.isdigit():
            raise ValueError(f"Phone number {self.phone_number} is not valid")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError(f"firstname & lastname can't be empty")

        special_characters = string.punctuation + string.digits
        if any(char in special_characters for char in (self.first_name+self.last_name)):
            raise ValueError(f"{self.full_name} is not valid")

    def _checks(self):
        self._check_names()
        self._check_phone_number()

if __name__ == "__main__":
    from faker import Faker
    fake = Faker(locale='fr_FR')
    for _ in range(25):
        # user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        user._checks()
        print(user)
        # print(repr(user))
        print("-" * 10)
        