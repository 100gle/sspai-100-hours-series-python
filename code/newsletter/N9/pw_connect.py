import pathlib

import peewee as pw

db_url = pathlib.Path(__file__).parent.joinpath("./mydb.sqlite3")
db = pw.SqliteDatabase(db_url)


# # equivalent to this:
# db_url = pathlib.Path(__file__).parent.joinpath("./mydb.sqlite3")
# db = pw.SqliteDatabase(None)
# db.init(db_url)


db.connect()

stmt = db.execute_sql("SELECT 1 as foo;").fetchall()
print(stmt)


db.close()
