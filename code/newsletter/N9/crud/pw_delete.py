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
    user = User.select().where(User.username.startswith("Jay")).get()
    ok = user.delete_instance()
    print(f"delete rows: {ok}")

    stmt = User.delete().where(User.username.in_(["bill gates", "larry page"]))
    ok = stmt.execute()
    print(f"delete rows: {ok}")


if __name__ == '__main__':
    main()
