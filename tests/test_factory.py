from movie_tracker import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'href="/"' in response.data
    assert b'Welcome to the Movie Tracker!' in response.data