import pytest
from fastapi.testclient import TestClient
from popup_api.models import Task


def test_query_all_tasks(client: TestClient):
    resp = client.get("/api/tasks")
    assert resp.status_code == 200

    data = resp.json()
    assert data["code"] == 0
    assert data["message"] == "query all tasks successfully."
    assert len(data["data"]) > 0


def test_query_all_groups(client: TestClient):
    resp = client.get("/api/groups")
    assert resp.status_code == 200

    data = resp.json()
    assert data["code"] == 0
    assert data["message"] == "query all groups successfully."
    assert len(data["data"]) > 0


@pytest.mark.parametrize(
    "data",
    [
        dict(
            taskName="测试 1",
            taskPriority=1,
            taskDescription="测试描述",
            taskGroup=0,
        ),
        dict(
            taskName="测试 2",
            taskPriority=2,
            taskDescription="测试一下最长的情况如何" * 100,
            taskGroup=1,
        ),
        dict(
            taskName="测试 3",
            taskPriority=1,
            taskDescription="测试描述",
            taskGroup=-1,
        ),
    ],
)
def test_create_task(client: TestClient, db, data):
    resp = client.post("/api/tasks/create", data=data)
    assert resp.status_code == 307

    tasks = db.query(Task).filter(Task.name.like("%测试%")).all()
    assert len(tasks) > 0


def test_update_task(client: TestClient, db):
    pre_resp = client.get("/api/tasks")
    pre_json = pre_resp.json()["data"]
    task_id = pre_json[0]["id"]
    is_done = pre_json[0]["is_done"]

    resp = client.put(f"/api/tasks/update/{task_id}")
    json = resp.json()
    assert json["data"]["id"] == task_id
    assert json["message"] == f"update #{task_id} task successfully."

    task = db.get(Task, task_id)
    assert task.is_done == (not is_done)


@pytest.mark.parametrize("invalid_id", [-1, -10])
def test_update_task_with_invalid_task_id(client: TestClient, invalid_id: int):
    resp = client.put(f"/api/tasks/update/{invalid_id}")
    assert resp.status_code == 200

    json = resp.json()
    assert json["code"] == 10001
    assert json["message"] == f"can't found the task which id is: {invalid_id}"


def test_delete_task(client: TestClient, db):
    pre_resp = client.get("/api/tasks")
    pre_json = pre_resp.json()["data"]
    task_id = pre_json[0]["id"]
    resp = client.delete(f"/api/tasks/delete/{task_id}")

    json = resp.json()
    assert json["data"]["id"] == task_id
    assert json["message"] == f"delete #{task_id} task successfully."

    task = db.get(Task, task_id)
    assert not task


@pytest.mark.parametrize("invalid_id", [-1, -10])
def test_delete_task_With_invalid_task_id(client: TestClient, invalid_id):
    resp = client.delete(f"/api/tasks/delete/{invalid_id}")
    assert resp.status_code == 200

    json = resp.json()
    assert json["code"] == 10001
    assert json["message"] == f"can't found the task which id is: {invalid_id}"
