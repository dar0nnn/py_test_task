from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from meeting_registation.models import Profile, Meeting, Registation
from django.views.generic import TemplateView, CreateView
from app.utils.views import Data, ZmeiDataViewMixin, RedirectAction
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.forms import ModelForm
from django.db.models import ProtectedError


class MeetingRegistationIndexView(ZmeiDataViewMixin, AccessMixin, TemplateView):

    def dispatch(self, *args, **kwargs):
        request = self.request

        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        return super().dispatch(*args, **kwargs)

    template_name = "meeting_registation/index.html"

    def get_data(self, url, request, inherited=False):
        data = Data()

        profile_item_list = Profile.objects.all()
        profile_can_edit = True
        meetings_item_list = Meeting.objects.all()
        meetings_can_edit = True
        registation_item_list = Registation.objects.all()
        registation_can_edit = True

        data.update({'url': url, 'profile_item_list': profile_item_list, 'profile_can_edit': profile_can_edit,
                     'meetings_item_list': meetings_item_list,
                     'meetings_can_edit': meetings_can_edit, 'registation_item_list': registation_item_list,
                     'registation_can_edit': registation_can_edit})

        return data


class MeetingMeetingsCreateForm(ModelForm):
    prefix = 'meetings'

    class Meta:
        model = Meeting
        fields = ['name', 'description', 'time']


class MeetingRegistationIndexMeetingsCreateView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_meetings_create.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        form_meetings = MeetingMeetingsCreateForm(
            request.POST if request.method == 'POST' else None, request.FILES if request.method == 'POST' else None,
            instance=Meeting(None))

        if request.method == "POST":

            if form_meetings.is_valid():
                model = form_meetings.save()

            raise RedirectAction('meeting_registation.index', )

        data.update({'url': url, 'form_meetings': form_meetings})

        return data

    post = MeetingRegistationIndexView.get


class MeetingMeetingsDeleteForm(ModelForm):
    prefix = 'meetings'

    class Meta:
        model = Meeting
        fields = []


class MeetingRegistationIndexMeetingsDeleteView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_meetings_delete.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        meetings_item = Meeting.objects.all().get(pk=url.meetings_pk)
        form_meetings = MeetingMeetingsDeleteForm(
            request.POST if request.method == 'POST' else None, request.FILES if request.method == 'POST' else None,
            instance=meetings_item)

        if request.method == "POST":

            form_meetings.full_clean()
            try:
                meetings_item.delete()
                raise RedirectAction('meeting_registation.index', )
            except ProtectedError as e:
                v.add_error(None, str(e))

        data.update({'url': url, 'meetings_item': meetings_item,
                     'form_meetings': form_meetings})

        return data

    post = MeetingRegistationIndexView.get


class MeetingRegistationIndexMeetingsDetailView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_meetings_detail.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        meetings_item = Meeting.objects.all().get(pk=url.meetings_pk)

        data.update({'url': url, 'meetings_item': meetings_item})

        return data


class MeetingMeetingsEditForm(ModelForm):
    prefix = 'meetings'

    class Meta:
        model = Meeting
        fields = ['name', 'description', 'time']


class MeetingRegistationIndexMeetingsEditView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_meetings_edit.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        meetings_item = Meeting.objects.all().get(pk=url.meetings_pk)
        form_meetings = MeetingMeetingsEditForm(request.POST if request.method == 'POST' else None,
                                                request.FILES if request.method == 'POST' else None,
                                                instance=meetings_item)

        if request.method == "POST":

            if form_meetings.is_valid():
                model = form_meetings.save()

            raise RedirectAction('meeting_registation.index', )

        data.update({'url': url, 'meetings_item': meetings_item,
                     'form_meetings': form_meetings})

        return data

    post = MeetingRegistationIndexView.get


class ProfileProfileCreateForm(ModelForm):
    prefix = 'profile'

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name']


class MeetingRegistationIndexProfileCreateView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_profile_create.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        form_profile = ProfileProfileCreateForm(request.POST if request.method == 'POST' else None,
                                                request.FILES if request.method == 'POST' else None,
                                                instance=Profile(None))

        if request.method == "POST":

            if form_profile.is_valid():
                model = form_profile.save()

            raise RedirectAction('meeting_registation.index', )

        data.update({'url': url, 'form_profile': form_profile})

        return data

    post = MeetingRegistationIndexView.get


class ProfileProfileDeleteForm(ModelForm):
    prefix = 'profile'

    class Meta:
        model = Profile
        fields = []


class MeetingRegistationIndexProfileDeleteView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_profile_delete.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        profile_item = Profile.objects.all().get(pk=url.profile_pk)
        form_profile = ProfileProfileDeleteForm(
            request.POST if request.method == 'POST' else None, request.FILES if request.method == 'POST' else None,
            instance=profile_item)

        if request.method == "POST":

            form_profile.full_clean()
            try:
                profile_item.delete()
                raise RedirectAction('meeting_registation.index', )
            except ProtectedError as e:
                v.add_error(None, str(e))

        data.update({'url': url, 'profile_item': profile_item,
                     'form_profile': form_profile})

        return data

    post = MeetingRegistationIndexView.get


class MeetingRegistationIndexProfileDetailView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_profile_detail.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        profile_item = Profile.objects.all().get(pk=url.profile_pk)

        data.update({'url': url, 'profile_item': profile_item})

        return data


class ProfileProfileEditForm(ModelForm):
    prefix = 'profile'

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name']


class MeetingRegistationIndexProfileEditView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_profile_edit.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        profile_item = Profile.objects.all().get(pk=url.profile_pk)
        form_profile = ProfileProfileEditForm(request.POST if request.method == 'POST' else None,
                                              request.FILES if request.method == 'POST' else None,
                                              instance=profile_item)

        if request.method == "POST":

            if form_profile.is_valid():
                model = form_profile.save()

            raise RedirectAction('meeting_registation.index', )

        data.update({'url': url, 'profile_item': profile_item,
                     'form_profile': form_profile})

        return data

    post = MeetingRegistationIndexView.get


class RegistationRegistationCreateForm(ModelForm):
    prefix = 'registation'

    class Meta:
        model = Registation
        fields = ['profile', 'meeting']


class MeetingRegistationIndexRegistationCreateView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_registation_create.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        form_registation = RegistationRegistationCreateForm(
            request.POST if request.method == 'POST' else None, request.FILES if request.method == 'POST' else None,
            instance=Registation(None))

        if request.method == "POST":

            if form_registation.is_valid():
                model = form_registation.save()

            raise RedirectAction('meeting_registation.index', )

        data.update({'url': url, 'form_registation': form_registation})

        return data

    post = MeetingRegistationIndexView.get


class RegistationRegistationDeleteForm(ModelForm):
    prefix = 'registation'

    class Meta:
        model = Registation
        fields = []


class MeetingRegistationIndexRegistationDeleteView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_registation_delete.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        registation_item = Registation.objects.all().get(pk=url.registation_pk)
        form_registation = RegistationRegistationDeleteForm(
            request.POST if request.method == 'POST' else None, request.FILES if request.method == 'POST' else None,
            instance=registation_item)

        if request.method == "POST":

            form_registation.full_clean()
            try:
                registation_item.delete()
                raise RedirectAction('meeting_registation.index', )
            except ProtectedError as e:
                v.add_error(None, str(e))

        data.update({'url': url, 'registation_item': registation_item,
                     'form_registation': form_registation})

        return data

    post = MeetingRegistationIndexView.get


class MeetingRegistationIndexRegistationDetailView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_registation_detail.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        registation_item = Registation.objects.all().get(pk=url.registation_pk)

        data.update({'url': url, 'registation_item': registation_item})

        return data


class RegistationRegistationEditForm(ModelForm):
    prefix = 'registation'

    class Meta:
        model = Registation
        fields = ['profile', 'meeting']


class MeetingRegistationIndexRegistationEditView(MeetingRegistationIndexView):
    template_name = "meeting_registation/index_registation_edit.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        registation_item = Registation.objects.all().get(pk=url.registation_pk)
        form_registation = RegistationRegistationEditForm(
            request.POST if request.method == 'POST' else None, request.FILES if request.method == 'POST' else None,
            instance=registation_item)

        if request.method == "POST":

            if form_registation.is_valid():
                model = form_registation.save()

            raise RedirectAction('meeting_registation.index', )

        data.update({'url': url, 'registation_item': registation_item,
                     'form_registation': form_registation})

        return data

    post = MeetingRegistationIndexView.get


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
