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


def main():
    User.create(username="Steve Jobs")

    user = User(username="Bill Gates")
    user.save()

    User.insert(username="Larry Page").execute()

    rows = [
        dict(username="100gle"),
        dict(username="Jay Chou"),
    ]
    User.insert_many(rows).execute()


if __name__ == '__main__':
    main()
