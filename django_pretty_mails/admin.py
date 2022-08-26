from .app_settings import SAVE_TO_LOG
from django.contrib import admin

if SAVE_TO_LOG:
    from django_pretty_mails.models import Log

    @admin.register(Log)
    class LogAdmin(admin.ModelAdmin):
        list_display = ('subject', 'to', 'cc', 'bcc', 'mail_type', 'created_at')
        search_fields = ('mail_type', 'subject', 'to', 'cc', 'bcc')
        list_filter = ('mail_type',)
        fieldsets = (
            (None, {
                'fields': ('created_at', 'mail_type', 'subject', 'to', 'cc', 'bcc', 'body'),
            }),
        )

        def has_add_permission(self, request, obj=None):
            return False

        def has_delete_permission(self, request, obj=None):
            return False

        def has_change_permission(self, request, obj=None):
            return False
