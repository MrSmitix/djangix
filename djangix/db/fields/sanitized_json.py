from typing import Callable

from json import dumps

from django.db.models import JSONField
from django.db.models.expressions import Expression


class SanitizedJSONField(JSONField):
    """ Поле использующее функцию для отчистки json """

    def __init__(self, *args, sanitizer: Callable[[dict], dict], **kwargs):
        super().__init__(*args, **kwargs)
        self._sanitizer_method = sanitizer

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["sanitizer"] = self._sanitizer_method
        return name, path, args, kwargs

    def get_db_prep_save(self, value: dict, connection):
        """ Сохраняет отчищенное значение """

        if isinstance(value, Expression):
            return value

        return dumps(self._sanitizer_method(value))
