import pathlib
from datetime import datetime

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


class Weibo(BaseModel):
    wid = pw.AutoField()
    content = pw.TextField()
    timestamp = pw.DateTimeField(default=datetime.now)
    user = pw.ForeignKeyField(User, backref="user", field="uid")


class Likes(BaseModel):
    user = pw.ForeignKeyField(User, backref="likes", field="uid")
    weibo = pw.ForeignKeyField(Weibo, backref="likes", field="wid")

    class Meta:
        primary_key = pw.CompositeKey("user", "weibo")


def main():

    # --------------
    # inplace change
    user = User.select().where(User.username.startswith("Steve")).get()
    print(f"before updating: {user}")

    user.username = user.username.lower()
    user.save()
    user = User.select().where(User.username.startswith("Steve")).get()
    print(f"after updating: {user}")

    # -------
    # update
    user = User.select().where(User.username == "100gle").get()
    print(f"before updating: {user}")

    query = User.update(username="100GLE").where(User.username == "100gle")
    query.execute()

    user = User.select().where(User.username.startswith("100")).get()
    print(f"after updating: {user}")

    # --------------------
    # update multiple rows
    users = User.select().where(User.username.in_(["Bill Gates", "Larry Page"]))
    print(f"before updating: {list(users)}")
    u1, u2 = users
    u1.username = u1.username.lower()
    u2.username = u2.username.lower()
    User.bulk_update([u1, u2], fields=[User.username])

    users = user.select().where(User.username.in_(["bill gates", "larry page"]))
    print(f"after updating: {list(users)}")


if __name__ == '__main__':
    main()
