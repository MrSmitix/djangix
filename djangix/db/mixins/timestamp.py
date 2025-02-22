from django.db.models import Model, DateTimeField

from django.utils.translation import gettext_lazy as _


class TimeStampMixin(Model):
    """ Миксин добавляет created_at и updated_at к модели """

    created_at = DateTimeField(verbose_name=_("created_at"), auto_now_add=True)
    updated_at = DateTimeField(verbose_name=_("updated_at"), auto_now=True)

    class Meta:
        abstract = True
