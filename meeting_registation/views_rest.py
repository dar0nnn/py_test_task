from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProfileSerializer, MeetingSerializer, RegistationSerializer
from meeting_registation.models import Profile, Meeting, Registation


class ProfileViewSet(ReadOnlyModelViewSet):
    """
    Profile API
    """

    filter_fields = ['id', 'user', 'first_name',
                     'last_name', 'registation', '__str__']
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()


class MeetingViewSet(ReadOnlyModelViewSet):
    """
    Meeting API
    """

    filter_fields = ['id', 'name', 'description',
                     'time', 'registation', '__str__']
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all()


class RegistationViewSet(ReadOnlyModelViewSet):
    """
    Registation API
    """

    filter_fields = ['id', 'profile', 'meeting', '__str__']
    serializer_class = RegistationSerializer

    def get_queryset(self):
        return Registation.objects.all()
