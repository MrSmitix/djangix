from django.db.models import JSONField

from djangix.forms.fields import ReadableJSONFormField


class ReadableJSONField(JSONField):
    """ Поле для хранения json в читаемом формате """

    empty_values = [None, "", ()]

    def formfield(self, **kwargs):
        return super().formfield(**{
            "form_class": ReadableJSONFormField,
            **kwargs,
        })
