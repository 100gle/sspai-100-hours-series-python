from fastapi import APIRouter, Depends, Form
from popup_api.models import Group, Task, get_db
from popup_api.schema import Response
from sqlalchemy import delete
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get("/tasks")
def query_all_tasks(db=Depends(get_db)):
    data = (
        db.query(Task)
        .with_entities(
            Task.id,
            Task.name,
            Task.priority,
            Task.description,
            Task.is_done,
            Task.group_id,
        )
        .all()
    )

    response = Response(data=data, message="query all tasks successfully.")
    return response


@router.get("/groups")
def query_all_groups(db=Depends(get_db)):
    data = db.query(Group).all()
    response = Response(data=data, message="query all groups successfully.")
    return response


@router.post("/tasks/create")
def create_task(
    name: str = Form(..., alias="taskName", example="测试"),
    priority: int = Form(1, alias="taskPriority", example=1),
    description: str = Form("", alias="taskDescription", example="任务描述测试"),
    group_id: int = Form(1, alias="taskGroup", example=1),
    db=Depends(get_db),
):

    task = Task(
        name=name, priority=priority, description=description, group_id=group_id
    )
    db.add(task)
    db.commit()

    response = RedirectResponse("/")
    return response


@router.put("/tasks/update/{task_id}")
def update_task(task_id: int, db=Depends(get_db)):

    task = db.get(Task, task_id)

    if not task:
        response = Response(
            code=10001, message=f"can't found the task which id is: {task_id}"
        )
    else:
        status = 0 if task.is_done == 1 else 1
        task.is_done = status
        db.commit()

        response = Response(
            data=dict(id=task_id, name=task.name),
            message=f"update #{task_id} task successfully.",
        )

    return response


@router.delete("/tasks/delete/{task_id}")
def delete_task(task_id: int, db=Depends(get_db)):

    task = db.get(Task, task_id)
    if not task:
        response = Response(
            code=10001, message=f"can't found the task which id is: {task_id}"
        )
    else:
        stmt = delete(Task).where(Task.id == task_id)
        db.execute(stmt)
        db.commit()

        response = Response(
            data=dict(id=task_id, name=task.name),
            message=f"delete #{task_id} task successfully.",
        )

    return response
