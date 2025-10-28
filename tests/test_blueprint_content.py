"""This is a test script to test flask application"""

import pytest              # third-party import first
from application.app import app  # first-party import second




@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_main_page_content(client):
    """flask unit testing for content in default page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Blueprint' in response.data

def test_about_page_content(client):
    """flask unit testing for content in about page"""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Blueprint' in response.data
