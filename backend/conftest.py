import pytest


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """Create user instance"""
    yield django_user_model.objects.create_user(
        username='John',
        email='a@a.pl',
        password='secret'
    )