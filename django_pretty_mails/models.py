from django.db import models
from django.utils.translation import gettext_lazy as _
from .app_settings import SAVE_TO_LOG


if SAVE_TO_LOG:

    class Log(models.Model):
        created_at = models.DateTimeField(_('created at'), auto_now_add=True)
        mail_type = models.CharField(_('mail type'), max_length=255, db_index=True)
        subject = models.CharField(_('subject'), max_length=255)
        body = models.TextField(_('body'))
        to = models.TextField(_('to'))
        cc = models.TextField(_('cc'), default='')
        bcc = models.TextField(_('bcc'), default='')

        @classmethod
        def create(cls, mail_type, email):
            log = cls(
                mail_type=mail_type,
                subject=email.subject,
                body=email.body,
                to=','.join(email.to),
                cc=','.join(email.cc),
                bcc=','.join(email.bcc)
            )

            log.save()
            return log
