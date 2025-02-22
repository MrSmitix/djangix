from django.db.models import TextChoices


class DjangoTextChoices(TextChoices):
    """
    Базовый класс для Enum с поддержкой свойства max_length

    Пример использования: models.CharField(choices=*.choices, default=*.*, max_length=*.max_length())
    """

    @classmethod
    def max_length(cls):
        """ Возвращает максимальную длину значения в Enum """

        return max(len(str(getattr(choice, 'value'))) for choice in cls)

    @classmethod
    def choices_with_max_length(cls):
        """ Возвращает choices и max_length для удобного использования в моделях """

        return cls.choices, cls.max_length
