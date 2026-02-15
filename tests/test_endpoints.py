from app import app


def test_index():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200


def test_todo_update_requires_auth():
    client = app.test_client()
    res = client.put("/api/v1/todos/000000000000000000000000", json={})
    assert res.status_code in (401, 422, 400)


def test_todo_delete_requires_auth():
    client = app.test_client()
    res = client.delete("/api/v1/todos/000000000000000000000000")
    assert res.status_code in (401, 422, 400)


def test_refresh_requires_auth():
    client = app.test_client()
    res = client.post("/api/v1/auth/refresh")
    assert res.status_code in (401, 422, 400)


def test_logout_requires_auth():
    client = app.test_client()
    res = client.post("/api/v1/auth/logout")
    assert res.status_code in (401, 422, 400)
