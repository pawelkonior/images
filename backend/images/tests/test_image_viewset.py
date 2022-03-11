import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate

from ..views import ImageViewSet


@pytest.mark.views
def test_user_can_see_own_image(user, test_image, api_rf, remove_test_data):
    view = ImageViewSet.as_view({'get': 'list'})

    request = api_rf.get('/api/v1/images/')
    force_authenticate(request, user)

    response = view(request)

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0].get('id') == test_image.id
    assert response.data[0].get('name') == 'test_file.jpg'
    assert response.data[0].get('author') == user.pk
