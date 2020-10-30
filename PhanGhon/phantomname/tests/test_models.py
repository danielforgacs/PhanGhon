import pytest
from phantomname import models




@pytest.mark.django_db
def test_ghostname_phantomname():
    user_01, _ = models.User.objects.get_or_create(username='user_01')
    ghostname_01 = models.GhostName.objects.create(
        name='ghostname_01',
        description='ghostname_01 description',)

    assert ghostname_01.phantomname is None

    phantomname_01 = models.PhantomName.objects.create(
        user=user_01,
        ghostname=ghostname_01,)

    assert ghostname_01.phantomname == phantomname_01
