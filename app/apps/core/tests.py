
# app/apps/core/tests.py
import pytest
from django.urls import reverse
from django.test import Client
from .models import Item

@pytest.mark.django_db
def test_item_creation():
    """Test item creation"""
    item = Item.objects.create(
        name="Test Item",
        description="This is a test item"
    )
    assert item.name == "Test Item"
    assert item.description == "This is a test item"
    assert item.id is not None

@pytest.mark.django_db
def test_health_check():
    """Test health check endpoint"""
    client = Client()
    response = client.get(reverse('health_check'))
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'
    assert data['database'] == 'connected'
    assert 'item_count' in data