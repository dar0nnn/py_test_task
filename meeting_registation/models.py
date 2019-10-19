from django.db import models
from ckeditor.fields import RichTextField


from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    Profile
    """

    user = models.ForeignKey("auth.User", verbose_name=_(
        'User'), null=True, blank=False, related_name='+', on_delete=models.PROTECT) # can be OneToOneField
    first_name = models.CharField(verbose_name=_(
        'First name'), null=True, blank=True, max_length=100)
    last_name = models.CharField(verbose_name=_(
        'Last name'), null=True, blank=True, max_length=100)

    def __str__(self):
        return str(self.user) or "Profile {}".format(self.id)

    class Meta:
        verbose_name = _("Profile")


class Meeting(models.Model):
    """
    Meeting
    """

    name = models.CharField(verbose_name=_(
        'Name'), null=True, blank=True, max_length=100)
    description = RichTextField(verbose_name=_(
        'Description'), null=True, blank=True)
    time = models.DateField(verbose_name=_('Time'), null=True, blank=True)

    def __str__(self):
        return str(self.name) or "Meeting {}".format(self.id)

    class Meta:
        verbose_name = _("Meeting")


class Registation(models.Model):
    """
    Registation
    """

    profile = models.ForeignKey("meeting_registation.Profile", verbose_name=_(
        'Profile'), null=True, blank=True, related_name='registation', on_delete=models.CASCADE)
    meeting = models.ForeignKey("meeting_registation.Meeting", verbose_name=_(
        'Meeting'), null=True, blank=True, related_name='registation', on_delete=models.CASCADE)

    def __str__(self):
        return _("Profile {me.profile} at {me.meeting}").format(me=self)

    class Meta:
        verbose_name = _("Registation")
