import factory

from tests.factories.UserFactory import UserCreationFactory


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'meeting_registation.Profile'

    user = factory.SubFactory(UserCreationFactory)
    first_name = 'test'
    last_name = 'testovich'
