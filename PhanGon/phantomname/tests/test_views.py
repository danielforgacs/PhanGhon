import pytest
from django import urls
from phantomname import views




@pytest.mark.django_db
def test_index(client):
    url = urls.reverse('index')
    response = client.get(url)
    assert response.status_code == 200
