from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('images', views.ImageViewSet, basename='images')
urlpatterns = router.urls
