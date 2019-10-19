from rest_framework import serializers
from meeting_registation.models import Profile, Meeting, Registation


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name',
                  'last_name', 'registation', '__str__']
        read_only_fields = ['__str__']


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ['id', 'name', 'description',
                  'time', 'registation', '__str__']
        read_only_fields = ['__str__']


class RegistationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registation
        fields = ['id', 'profile', 'meeting', '__str__']
        read_only_fields = ['__str__']


index = {
    Profile: {
        '_': ProfileSerializer,
    },

    Meeting: {
        '_': MeetingSerializer,
    },

    Registation: {
        '_': RegistationSerializer,
    },
}
