from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

import meeting_registation.urls
import meeting_registation.urls_rest

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(meeting_registation.urls_rest)),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^', include(meeting_registation.urls)),
]