from django.contrib import admin

from .models import ScriptInfo


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "subject", "created_on")


admin.site.register(ScriptInfo, ContactFormAdmin)
