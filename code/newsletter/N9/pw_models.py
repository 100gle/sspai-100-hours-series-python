import pathlib

import peewee as pw

db_url = pathlib.Path(__file__).parent.joinpath("./mydb.sqlite3")
db = pw.SqliteDatabase(db_url)


class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    uid = pw.AutoField()
    username = pw.CharField(max_length=10)


if __name__ == '__main__':
    db.create_tables([User])
