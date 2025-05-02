import pytest
from app import app
from unittest.mock import Mock, patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_visit_counter(client):
    # Create a mock Redis instance
    mock_redis = Mock()
    mock_redis.incr.return_value = 1  # First visit
    
    # Patch the Redis connection in your app
    with patch('app.cache', mock_redis):
        response = client.get('/visits')
        assert response.json['visits'] == 1
        mock_redis.incr.assert_called_once_with('visits')
