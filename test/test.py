import sys
import os

# Add the directory containing app.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask App!" in response.data
