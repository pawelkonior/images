import pytest
from ..serializers import ImageSerializer


@pytest.mark.serializers
def test_fields(db, test_image, remove_test_data):
    serializer = ImageSerializer(instance=test_image)
    serializer_data = serializer.data

    assert list(serializer_data.keys()) == ['id', 'url', 'name', 'created_at', 'updated_at', 'author']
