import pytest
from app import app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def testid(client):
   response=client.get("/")
   assert b'Hello' in response.data
