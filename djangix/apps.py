from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangixExtDjangoConfig(AppConfig):
    name = "djangix.django"
    label = "django_djangix"
    verbose_name = _("DjangixExtDjangoConfig")
