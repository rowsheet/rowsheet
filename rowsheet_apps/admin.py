from django.contrib import admin

from .models import ClientApp
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "name",
        "description",
        "creation_timestamp",
        "last_changed_timestamp",
        "job_timestamp",
    )
admin.site.register(Organization, OrganizationAdmin)

class ClientAppAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "name",
        "description",
        "creation_timestamp",
        "last_changed_timestamp",
        "job_timestamp",
    )
admin.site.register(ClientApp, ClientAppAdmin)
