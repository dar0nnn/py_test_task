from django.conf.urls import url
from .views import MeetingRegistationIndexView, MeetingRegistationIndexMeetingsCreateView, \
    MeetingRegistationIndexMeetingsDeleteView, MeetingRegistationIndexMeetingsDetailView, \
    MeetingRegistationIndexMeetingsEditView, MeetingRegistationIndexProfileCreateView, \
    MeetingRegistationIndexProfileDeleteView, MeetingRegistationIndexProfileDetailView, \
    MeetingRegistationIndexProfileEditView, MeetingRegistationIndexRegistationCreateView, \
    MeetingRegistationIndexRegistationDeleteView, MeetingRegistationIndexRegistationDetailView, \
    MeetingRegistationIndexRegistationEditView, SignUp

urlpatterns = (
    url(r'^$', MeetingRegistationIndexView.as_view(),
        name='meeting_registation.index'),

    url(r'^meetings/create$', MeetingRegistationIndexMeetingsCreateView.as_view(),
        name='meeting_registation.index_meetings_create'),

    url(r'^meetings/(?P<meetings_pk>[^\/]+)/delete$', MeetingRegistationIndexMeetingsDeleteView.as_view(
    ), name='meeting_registation.index_meetings_delete'),

    url(r'^meetings/(?P<meetings_pk>[^\/]+)/detail$', MeetingRegistationIndexMeetingsDetailView.as_view(
    ), name='meeting_registation.index_meetings_detail'),

    url(r'^meetings/(?P<meetings_pk>[^\/]+)/edit$', MeetingRegistationIndexMeetingsEditView.as_view(
    ), name='meeting_registation.index_meetings_edit'),

    url(r'^profile/create$', MeetingRegistationIndexProfileCreateView.as_view(),
        name='meeting_registation.index_profile_create'),

    url(r'^profile/(?P<profile_pk>[^\/]+)/delete$', MeetingRegistationIndexProfileDeleteView.as_view(
    ), name='meeting_registation.index_profile_delete'),

    url(r'^profile/(?P<profile_pk>[^\/]+)/detail$', MeetingRegistationIndexProfileDetailView.as_view(
    ), name='meeting_registation.index_profile_detail'),

    url(r'^profile/(?P<profile_pk>[^\/]+)/edit$', MeetingRegistationIndexProfileEditView.as_view(
    ), name='meeting_registation.index_profile_edit'),

    url(r'^registation/create$', MeetingRegistationIndexRegistationCreateView.as_view(),
        name='meeting_registation.index_registation_create'),

    url(r'^registation/(?P<registation_pk>[^\/]+)/delete$', MeetingRegistationIndexRegistationDeleteView.as_view(
    ), name='meeting_registation.index_registation_delete'),

    url(r'^registation/(?P<registation_pk>[^\/]+)/detail$', MeetingRegistationIndexRegistationDetailView.as_view(
    ), name='meeting_registation.index_registation_detail'),

    url(r'^registation/(?P<registation_pk>[^\/]+)/edit$', MeetingRegistationIndexRegistationEditView.as_view(
    ), name='meeting_registation.index_registation_edit'),
    url('accounts/', SignUp.as_view(), name='register'),
)
