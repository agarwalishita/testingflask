import pytest
from app import app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_hello(client):
   response=client.get("/")
   assert b'Hello' in response.data
