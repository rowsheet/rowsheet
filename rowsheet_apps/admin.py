from django.contrib import admin

from .models import ClientApp

# Register your models here.
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
