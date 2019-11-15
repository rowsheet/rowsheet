from django.urls import path
from django.conf.urls import url

from rowsheet_landing import views

urlpatterns = [
    path("dashboard/", views.dashboard),
    path("dashboard/apps/", views.dashboard_apps),
    path("dashboard/organizations/", views.dashboard_organizations),
    url(r"^components/", views.components),
    path("", views.index),
    path("api", views.api),
]
