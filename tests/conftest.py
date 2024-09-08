import pytest
from glob import glob
import json
from os import path

from my_app import create_app


@pytest.fixture
def app():
    app = create_app('flask_test.cfg')
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def get_test_data(file_path='./data/files', file_pattern = 'data_*_test.json'):
    for file_name in glob(path.join(file_path, file_pattern)):
        with open(file_name, 'r') as file:
            data = json.load(file)
            for d in data:
                qv = (d['query'], d['variables'] if 'variables' in d else None)
                expected_output = d['expected_output']
                yield qv, expected_output


# Define the pytest_generate_tests hook to generate test cases
def pytest_generate_tests(metafunc):
    if all([name in metafunc.fixturenames for name in ['input', 'output']]):
        inputs = [t for t in get_test_data()]
        metafunc.parametrize('input,output', inputs)
    if all([name in metafunc.fixturenames for name in ['client', 'payload', 'output']]):
        inputs = [({"query": q, "variables": v},o) for (q, v),o in get_test_data()]
        metafunc.parametrize('payload,output', inputs)


        