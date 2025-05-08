def test_register(client):
    response = client.get('/auth/register')

    assert response.status_code == 200
    assert b'Register here!' in response.data