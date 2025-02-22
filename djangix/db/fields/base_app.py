from django.apps import apps
from django.db.models import CharField


class BaseAppField(CharField):
    """
    Поле для выбора среди установленных приложений
    Поиск по prefix работаем только в том случае, если приложения хранятся в своих папках

    Пример использования:
    class SupplierAppField(BaseAppField):
        def __init__(self, *args, **kwargs):
            super().__init__(prefix='supplier.', *args, **kwargs)
    """

    def __init__(self, prefix=None, *args, **kwargs):
        kwargs.setdefault('max_length', 64)
        super().__init__(*args, **kwargs)

        # Генерируем choices
        self.choices = self.get_installed_apps(prefix)
        # Считаем max_length  # TODO: Подумать, не хочется просто вставлять это значение в max_length
        self._max_length = max([len(app[0]) for app in self.choices])

    def get_max_length(self, prefix: str | None = None):
        return max([len(app[0]) for app in self.get_installed_apps(prefix=prefix)])

    @staticmethod
    def get_installed_apps(prefix: str | None = None):
        return [
            (app.label, app.verbose_name) for app in apps.get_app_configs()
            if prefix is None or app.name.startswith(prefix)
        ]
