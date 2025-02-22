from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangixExtDjangoConfig(AppConfig):
    name = "djangix"
    label = "djangix"
    verbose_name = _("DjangixExtDjangoConfig")
