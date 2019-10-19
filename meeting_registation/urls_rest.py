from django.conf.urls import url, include
from rest_framework import routers
from .views_rest import ProfileViewSet, MeetingViewSet, RegistationViewSet

router = routers.DefaultRouter()

router.register(r'profile', ProfileViewSet, r'profile')


router.register(r'meeting', MeetingViewSet, r'meeting')


router.register(r'registation', RegistationViewSet, r'registation')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
