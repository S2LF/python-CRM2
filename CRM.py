import re
import string
from pathlib import Path
from regex import F

from tinydb import TinyDB, where

class User:

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

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

    @property
    def db_instance(self):
       return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))

    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        print(phone_number)
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

    def exists(self) -> bool:
        return bool(self.db_instance)

    def delete(self) -> list[int]:
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

    def save(self, validate_data=False) -> int:
        if validate_data:
            self._checks()
        if self.exists():
            return -1
        else:
            return User.DB.insert(self.__dict__)


def get_all_users():
    return [User(**user) for user in User.DB.all()]
    for user in User.DB.all():
        each_user = User(**user)
        print(each_user.full_name)
    return True

if __name__ == "__main__":
    # from faker import Faker
    # fake = Faker(locale='fr_FR')
    # for _ in range(25):
        # user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        # user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
        # user._check_phone_number()
        # user._checks()
        # print(user)
        # print(repr(user))
        # print(user.__dict__)
        # print("-" * 10)
        # print(user.save(True))
        # print(get_all_users())
    vincent = User("Vincent", "Martinez")
    # print(vincent.db_instance)
    # print(vincent.exists())
    # print(vincent.delete())
    print(true + false)