import pathlib

import peewee as pw

db_url = pathlib.Path(__file__).parents[1].joinpath("./mydb.sqlite3")
db = pw.SqliteDatabase(db_url)


class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    uid = pw.AutoField()
    username = pw.CharField(max_length=10)

    def __repr__(self) -> str:
        return f"User<uid={self.uid}, username={self.username}>"

    __str__ = __repr__


def main():
    # get*
    User.get(User.uid == 1)
    User.get_by_id(2)
    User.get_or_none(User.uid == 3)
    User[1]

    # select
    users = User.select()
    print(list(users))

    users = User.select().limit(3)
    print(list(users))

    users = User.select().limit(100).iterator()
    print(list(users))

    # select with condition
    users = User.select().where(User.uid.in_([1, 3]))
    print(list(users))

    users = User.select().where((User.uid == 1) | (User.uid == 4))
    print(list(users))

    users = User.select().where(
        (User.username.startswith("Steve")) & (User.username.endswith("Jobs"))
    )
    print(list(users))


if __name__ == '__main__':
    main()
