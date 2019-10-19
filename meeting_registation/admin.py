from django.contrib import admin
from django import forms
from meeting_registation.models import Profile, Meeting, Registation
from django.contrib.admin import ModelAdmin


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ()
        widgets = {

        }


class ProfileAdmin(ModelAdmin):
    """
    #profile
    Profile Admin
    """

    form = ProfileModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['user', 'first_name', 'last_name']
        }),)


admin.site.register(Profile, ProfileAdmin)


class MeetingModelForm(forms.ModelForm):
    class Meta:
        model = Meeting
        exclude = ()
        widgets = {

        }


class MeetingAdmin(ModelAdmin):
    """
    #meeting
    Meeting Admin
    """

    form = MeetingModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name', 'description', 'time']
        }),)


admin.site.register(Meeting, MeetingAdmin)


class RegistationModelForm(forms.ModelForm):
    class Meta:
        model = Registation
        exclude = ()
        widgets = {

        }


class RegistationAdmin(ModelAdmin):
    """
    #registation
    Registation Admin
    """

    form = RegistationModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['profile', 'meeting']
        }),)


admin.site.register(Registation, RegistationAdmin)
