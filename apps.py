from __future__ import unicode_literals

from django.apps import AppConfig
from django.conf import settings


class {{ camel_case_app_name }}Config(AppConfig):
    name = '{{ camel_case_app_name }}'

    def ready(self):
        if not settings.DEBUG:
            return

