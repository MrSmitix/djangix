from django.db.models import Model, QuerySet


class MappingMixin(Model):
    """ Миксин добавляющий к модели функцию get_map """

    @classmethod
    def get_map(cls, field_name: str = 'pk', queryset: QuerySet | None = None):
        """
        Возвращаем hashmap по определенному полю, можем передать queryset для формирования

        :param field_name: название поля которое будет ключом hashmap
        :param queryset: QuerySet, если нужно сделать hashmap по сложному запросу, например, с агрегацией
        :return: hashmap
        """

        queryset = queryset or cls.objects.all()

        return {getattr(obj, field_name): obj for obj in queryset}

    class Meta:
        abstract = True
