import pytest
from movie_tracker import create_app

# TODO: Add database-related code

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()