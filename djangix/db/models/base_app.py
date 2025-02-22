from django.apps import apps
from django.db.models import Model

from djangix.db.fields import BaseAppField


class BaseAppModel(Model):
    """ Базовая модель для подключенных приложений """

    app: str = BaseAppField(verbose_name='Приложение')

    class Meta:
        abstract = True

    def get_app(self):
        """ Возвращает приложение """

        return apps.get_app_config(self.app)

    @property
    def verbose_name(self):
        """ Возвращает читаемое название приложения """

        app_config = self.get_app()

        return f'{app_config.verbose_name} ({app_config.label})'

    def __str__(self):
        return self.verbose_name
