import pathlib
import typing as t
from datetime import datetime

import peewee as pw
from fastapi import FastAPI
from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel, Field

db_url = pathlib.Path(__file__).parent.joinpath("web.sqlite3")
db = pw.SqliteDatabase(db_url)

app = FastAPI()

T = t.TypeVar("T")


class NoteORM(pw.Model):
    id = pw.AutoField()
    title = pw.CharField()
    content = pw.TextField()
    tags = pw.CharField()
    create_at = pw.DateTimeField(default=datetime.now())

    class Meta:
        database = db


class GenericResponse(BaseModel):
    code: int = 0
    msg: t.Optional[str]
    data: t.Optional[t.List[T]]


class NoteModel(BaseModel):
    id: t.Optional[int] = Field(example="null")
    title: str
    content: str
    tags: t.Optional[t.List[str]] = Field(example="null")


@app.on_event("startup")
def connect():
    db.create_tables([NoteORM])
    db.connect(reuse_if_open=True)


@app.on_event("shutdown")
def disconnect():
    if not db.is_closed():
        db.close()


@app.get("/")
def index():
    data = NoteORM.select()
    return GenericResponse(
        code=200, msg="success", data=[model_to_dict(orm) for orm in data]
    )


@app.get("/note/{id}", response_model=GenericResponse)
def query_note_by_id(id: int):
    result = NoteORM.get_or_none(NoteORM.id == id)

    if not result:
        response = GenericResponse(
            code=404, msg=f"can't get the note which id is: `{id}`."
        )
    else:
        response = GenericResponse(
            code=200,
            msg="success",
            data=[model_to_dict(result)],
        )
    return response


@app.post("/note", response_model=GenericResponse)
def add_note(payload: NoteModel):
    tags = "" if not payload.tags else ",".join(payload.tags)

    note = NoteORM.create(
        title=payload.title,
        content=payload.content,
        tags=tags,
    )

    return GenericResponse(
        code=200,
        msg="success",
        data=[model_to_dict(note)],
    )


@app.put("/note", response_model=GenericResponse)
def update_note(payload: NoteModel):
    data = payload.dict()
    id = data.pop("id")
    if not id:
        return GenericResponse(code=400, msg="`id` is invalid value.")

    result: t.Optional[NoteORM] = NoteORM.get_or_none(NoteORM.id == id)

    if not result:
        return GenericResponse(
            code=404, msg=f"can't update the note which id is: `{id}`."
        )

    result.update(**data)
    result.save()

    return GenericResponse(code=200, msg="success", data=[model_to_dict(result)])


@app.delete("/note/{id}", response_model=GenericResponse)
def delete_note_by_id(id: int):
    data: t.Optional[NoteORM] = NoteORM.get_or_none(NoteORM.id == id)
    if not data:
        return GenericResponse(
            code=404, msg=f"can't update the note which id is: `{id}`."
        )

    id = data.id
    ok = data.delete_instance()
    if ok >= 1:
        return GenericResponse(code=200, msg="success", data=[{"id": id}])

    return GenericResponse(
        code=500,
        msg=f"something wrong when delete note which id is: {id}.",
        data=[{"id": id}],
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", reload=True)
