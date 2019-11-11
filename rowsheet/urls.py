from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import rowsheet_landing.views

urlpatterns = [
    path("", rowsheet_landing.views.index, name="index"),
    path("admin/", admin.site.urls),
]
