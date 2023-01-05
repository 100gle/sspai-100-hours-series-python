import dataclasses

import pytest


@dataclasses.dataclass
class Connection:
    def execute(self, sql: str):
        print(f"execute {sql}...")
        return True

    def close(self):
        print(f"\ndisconnect {repr(self)} object...")


@dataclasses.dataclass
class Database:
    dialect: str = "sqlite"

    def connect(self):
        return Connection()

    def close(self):
        print(f"\ndisconnect {repr(self)} object...")


@pytest.fixture()
def sqlite():
    db = Database()
    conn = db.connect()
    try:
        yield conn
    finally:
        conn.close()
        db.close()


@pytest.fixture()
def mysql():
    db = Database(dialect="mysql")
    conn = db.connect()
    try:
        yield conn
    finally:
        conn.close()
        db.close()


@pytest.fixture(params=["sqlite", "mysql"])
def database(request):
    db = Database(dialect=request.param)
    conn = db.connect()
    try:
        yield conn
    finally:
        conn.close()
        db.close()


@pytest.fixture()
def gender():
    return ["male", "female"]


@pytest.fixture()
def cpu():
    return "cpu"


@pytest.fixture()
def device(cpu):
    return f"the device with {cpu}"


@pytest.fixture(scope="class")
def logger():
    print("\nstart recording...")
    yield
    print("\nend recording...")
