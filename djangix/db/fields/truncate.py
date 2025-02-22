from django.db.models import CharField


class TruncateCharField(CharField):
    """ Автоматически обрезает строку до max_length """

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return value[:self.max_length] if value else value
