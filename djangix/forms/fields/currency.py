from django.forms.fields import DecimalField


def sanitize_separators(value):
    """
    Приводит строковое представление числа к стандартному формату,
    удаляя разделители тысяч и заменяя десятичный разделитель на точку.
    """

    if isinstance(value, str):
        parts = []  # Список для хранения целой и дробной частей числа

        decimal_separator = ","  # Устанавливаем десятичный разделитель

        # Проверяем, есть ли десятичный разделитель в строке
        if decimal_separator in value:
            # Разделяем строку на целую и дробную части
            value, decimals = value.split(decimal_separator, maxsplit=1)
            parts.append(decimals)  # Добавляем дробную часть в список

        # Удаляем разделители тысяч (пробел, апостроф, обратная кавычка)
        for replacement in {" ", "'", "`"}:
            value = value.replace(replacement, "")  # Заменяем разделители на пустую строку

        parts.append(value)  # Добавляем целую часть в список
        # Объединяем части в строку, используя точку в качестве разделителя
        value = ".".join(reversed(parts))

    return value


class CurrencyFormField(DecimalField):
    """ Поле для CurrencyField, обрабатывает ".", "," и пробел между разрядами """

    def to_python(self, value):
        return super().to_python(sanitize_separators(value))
