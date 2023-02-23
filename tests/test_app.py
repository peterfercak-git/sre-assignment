def test_incorrect_param(app, client):
    del app
    res = client.get('/error')
    assert res.status_code == 200
