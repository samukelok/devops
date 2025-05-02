import pytest
from app import app
import redis

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_visit_counter(client, monkeypatch):
    # Mock Redis
    mock_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
    mock_redis.flushall()  # Clear before test
    monkeypatch.setattr('app.cache', mock_redis)

    # First request
    response = client.get('/visits')
    assert response.json['visits'] == 1

    # Second request
    response = client.get('/visits')
    assert response.json['visits'] == 2