import os
import shutil

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings

from images.models import Image


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """Create user instance"""
    yield django_user_model.objects.create_user(
        username='John',
        email='a@a.pl',
        password='secret'
    )


@pytest.fixture(scope='function')
def remove_test_data():
    yield
    try:
        shutil.rmtree(os.environ.get('TEST_DIR'))
    except OSError:
        pass


@pytest.fixture(scope='function')
@override_settings(MEDIA_ROOT=(os.path.join(os.environ.get('TEST_DIR'), 'media')))
def test_image(user):
    image = Image.objects.create(
        author=user,
        url=SimpleUploadedFile('test_file.jpg', content=open(os.path.join('tests', 'test_image.jpg'), 'rb').read())
    )

    return image
