from decimal import Decimal

from django.db import models

from djangix.forms.fields import CurrencyFormField


class CurrencyField(models.DecimalField):
    """
    Поле для хранения денежных значений
    По умолчанию поддерживает суммы до "999 999.99"
    """

    def __init__(self, verbose_name: str | None = None, name: str | None = None, **kwargs):
        max_digits = kwargs.pop("max_digits", 8)
        decimal_places = kwargs.pop("decimal_places", 2)

        super(CurrencyField, self).__init__(
            verbose_name=verbose_name, name=name, max_digits=max_digits, decimal_places=decimal_places, **kwargs
        )

    def to_python(self, value):
        try:
            return super().to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
            return None

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def formfield(self, **kwargs):
        defaults = {
            "form_class": CurrencyFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
