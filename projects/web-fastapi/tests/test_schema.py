from popup_api.schema import Response


def test_Response():

    resp1 = Response(code=200, message="success", data=[{"foo": 1}])
    assert resp1.dict() == dict(code=200, message="success", data=[{"foo": 1}])
    assert resp1.json() == '{"code": 200, "message": "success", "data": [{"foo": 1}]}'

    resp2 = Response(code=200, message="success", data=[])
    assert resp2.dict() == dict(code=200, message="success", data=[])
    assert resp2.json() == '{"code": 200, "message": "success", "data": []}'

    resp3 = Response(code=200, message="success", data="foo")
    assert resp3.dict() == dict(code=200, message="success", data="foo")
    assert resp3.json() == '{"code": 200, "message": "success", "data": "foo"}'

    resp4 = Response(code=400, message="failed")
    assert resp4.dict() == dict(code=400, message="failed", data=None)
    assert resp4.json() == '{"code": 400, "message": "failed", "data": null}'
