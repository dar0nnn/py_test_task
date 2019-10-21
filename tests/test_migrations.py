from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from django.test import TestCase
from meeting_registation.models import Profile
from tests.factories.ProfileFactory import ProfileFactory
from tests.factories.UserFactory import UserCreationFactory


class TestMigrations(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = UserCreationFactory()

    def test_migrations_created(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        ProfileFactory(user=self.user)
        profile = Profile.objects.all()[0]
        assert profile
        request = client.get(reverse('profile-list'))
        assert request.status_code == status.HTTP_200_OK
        assert profile.first_name == request.json()[0]['first_name']
