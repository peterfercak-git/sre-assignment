def test_incorrect_param(app, client):
    del app
    res = client.get('/health')
    assert res.status_code == 200
