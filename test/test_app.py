import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Flask App" in response.data

def test_greet_route_with_name(client):
    response = client.post('/greet', json={'name': 'Shivkumar'})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Shivkumar! Welcome aboard."}

def test_greet_route_without_name(client):
    response = client.post('/greet', json={})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Guest! Welcome aboard."}
