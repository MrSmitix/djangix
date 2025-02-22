import json

from django.forms.fields import JSONField, InvalidJSONInput


class ReadableJSONFormField(JSONField):
    """ Читаемый вывод JSON в Django admin """

    empty_values = [None, "", ()]

    def prepare_value(self, value):
        """ Подготавливает данные для отображения """

        if isinstance(value, InvalidJSONInput):
            return value

        return json.dumps(value, indent=2, ensure_ascii=False)
