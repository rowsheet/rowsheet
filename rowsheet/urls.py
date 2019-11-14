from django.urls import path, include
from django.conf.urls import url

from django.contrib import admin

admin.autodiscover()

import rowsheet_landing.views

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^accounts/", include("allauth.urls")),
    url(r"^", include("rowsheet_landing.urls")),
    # path("", rowsheet_landing.views.index, name="index"),
]
