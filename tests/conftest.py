import pytest

from my_app import create_app

@pytest.fixture
def app():
    app = create_app('flask_test.cfg')
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()