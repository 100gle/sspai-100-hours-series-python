from dataclasses import dataclass
from pprint import pprint


@dataclass
class User:
    name: str
    age: int
    email: str
    telephone: str


table = [
    User(
        name="John",
        age=25,
        email="example.john@sspai.com",
        telephone="021-12345678",
    ),
    User(
        name="Steve",
        age=30,
        email="example.steve@sspai.com",
        telephone="000-1111-1111",
    ),
]

pprint(table)
