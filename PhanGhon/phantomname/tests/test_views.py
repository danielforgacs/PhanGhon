import re
import pytest
from django import urls
from phantomname import views
from phantomname import models


TEST_USER_COUNT = 4
TEST_USER_NAME_TEMPLATE = '__TEST_USER__'
TEST_GHOST_NAME_COUNT = 5
TEST_GHOST_NAME_TEMPLATE = 'POKL'
TEST_PASSWORD = 'PWD'




@pytest.mark.django_db
def test_index(client):
    url = urls.reverse('index')
    response = client.get(url)
    assert response.status_code == 200




@pytest.fixture
def ghostnames():
    for row in range(TEST_GHOST_NAME_COUNT):
        idx = '{:04d}'.format(row)
        name = TEST_GHOST_NAME_TEMPLATE + idx
        models.GhostName.objects.create(name=name)




@pytest.fixture
def users():
    for row in range(TEST_USER_COUNT):
        idx = '{:04d}'.format(row)
        name = TEST_USER_NAME_TEMPLATE + idx
        user = models.User.objects.create_user(username=name, password=TEST_PASSWORD)
        user.set_password(TEST_PASSWORD)
        user.save()


@pytest.mark.django_db
def test_index_lists_ghostnames(client, ghostnames):
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




@pytest.mark.django_db
def test_user_can_log_in(users, ghostnames, client):
    username = TEST_USER_NAME_TEMPLATE+'0000'
    client.login(username=username, password=TEST_PASSWORD)
    url = urls.reverse('index')
    response = client.get(url)
    html = response.content.decode()
    found = re.findall(username, html)
    assert len(found) == 1




@pytest.mark.django_db
def test_new_user_can_choose_phantom_name(users, ghostnames, client):
    username = TEST_USER_NAME_TEMPLATE+'0000'
    client.login(username=username, password=TEST_PASSWORD)
    url = urls.reverse('get_name')
    response = client.post(
        url,
        follow=True,
        data={
            'firstname': '..::firstname::..',
            'lastname': '..::lastname::..',
        }
    )
    html = response.content.decode()
    pattern = r'..::firstname::.. .*\d{4} ..::lastname::..'
    found = re.findall(pattern, html)
    assert len(found) == 3

    url = urls.reverse('save_choice')

    # We don't know which 3 ghost names random.choice
    # chooses in the view. This makes sure at least
    # one is selected.
    try:
        response = client.get(url, {'choice': 0}, follow=True)
    except:
        try:
            response = client.get(url, {'choice': 1}, follow=True)
        except:
            try:
                response = client.get(url, {'choice': 2}, follow=True)
            except:
                raise

    html = response.content.decode()
    pattern = r'..::firstname::.. .*\d{4} ..::lastname::..'
    found = re.findall(pattern, html)
    assert len(found) == 1
