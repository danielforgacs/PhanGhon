import re
import pytest
from django import urls
from phantomname import views
from phantomname import models


TEST_GHOST_NAME_COUNT = 5
TEST_GHOST_NAME_TEMPLATE = 'POKL'




@pytest.mark.django_db
def test_index(client):
    url = urls.reverse('index')
    response = client.get(url)
    assert response.status_code == 200




@pytest.fixture
def data01():
    for row in range(TEST_GHOST_NAME_COUNT):
        idx = '{:04d}'.format(row)
        name = TEST_GHOST_NAME_TEMPLATE + idx
        models.GhostName.objects.create(name=name)




@pytest.mark.django_db
def test_index_lists_ghostnames(client, data01):
    url = urls.reverse('index')
    response = client.get(url)
    html = response.content.decode()
    pattern = TEST_GHOST_NAME_TEMPLATE+r'\d{4}'
    found = re.findall(pattern, html)
    assert len(found) == TEST_GHOST_NAME_COUNT




@pytest.mark.django_db
def test_can_register_user(client):
    url = urls.reverse('register')
    response = client.post(
        url,
        follow=True,
        data={
            'username': 'username',
            'password': 'password',
            'confirm_password': 'password',
        }
    )
    html = response.content.decode()
    pattern = r'<h3>logged in as: <strong>.*</strong></h3>'
    found = re.findall(pattern, html)
    assert len(found) == 1
