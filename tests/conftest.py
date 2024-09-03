import pytest
from glob import glob
import json

from my_app import create_app

@pytest.fixture
def app():
    app = create_app('flask_test.cfg')
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def get_test_data(path='./data/files/data_*.test'):
    for file_name in glob(path):
        with open(file_name, 'r') as file:
            while True:
                query = file.readline()
                if not query:
                    break
                query = query.rstrip()
                output = file.readline()
                if not output:
                    break
                outputJson = json.loads(output.rstrip())
                yield query, outputJson

# Define the pytest_generate_tests hook to generate test cases
def pytest_generate_tests(metafunc):
    files_path = './data/files/data_*.test'
    if all([name in metafunc.fixturenames for name in ['input', 'output']]):
        inputs = [t for t in get_test_data(files_path)]
        metafunc.parametrize('input,output', inputs)
    if all([name in metafunc.fixturenames for name in ['client', 'payload', 'output']]):
        inputs = [({"query": q, "variables": None},o) for q,o in get_test_data(files_path)]
        metafunc.parametrize('payload,output', inputs)


        