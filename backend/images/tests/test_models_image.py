from ..models import Image


def test_image_creation(user, test_image, remove_test_data):
    assert isinstance(test_image, Image)
    assert test_image.author == user
    assert test_image.url.url == '/media/images_files/test_file.jpg'
    assert test_image.name == 'test_file.jpg'
    assert str(test_image) == 'test_file.jpg'


def test_image_fields(db, test_image, remove_test_data):
    assert [*test_image.__dict__] == ['_state', 'id', 'author_id', 'url', 'name', 'created_at', 'updated_at']