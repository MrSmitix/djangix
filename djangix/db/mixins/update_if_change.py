from django.db.models import Model


class UpdateIfChangedMixin(Model):
    """ Миксин добавляющий к модели функцию update_if_changed """

    def _update_fields_if_changed(self, data: dict, force_update_fields: list or None = None) -> [str]:
        """
        Обновление значений у полей объекта

        :param data: новые (или нет) значения для полей
        :param force_update_fields: названия полей, которые нужно обновить ни смотря ни на что
        :return: список обновленных полей
        """

        updated_fields = []  # Список для хранения изменённых полей

        if force_update_fields is None:
            force_update_fields = []  # По умолчанию пустой список

        for field, new_value in data.items():
            if hasattr(self, field):
                current_value = getattr(self, field)
                if current_value != new_value or field in force_update_fields:
                    setattr(self, field, new_value)
                    updated_fields.append(field)  # Добавляем поле в список изменённых

        return updated_fields

    def update_if_changed(self, data: dict, force_update_fields: list or None = None) -> (bool, list):
        """
        Обновляет поля модели, только если они изменились.
        Сохраняет только изменённые поля через update_fields.
        Также обновляет поля, указанные в force_update_fields, даже если их значения не изменились

        :param data: Словарь с данными
        :param force_update_fields: Список полей, которые нужно обновить принудительно
        :return: True и список обновленных полей, если были внесены изменения, иначе False и пустой список
        """

        updated_fields = self._update_fields_if_changed(data=data, force_update_fields=force_update_fields)

        if updated_fields:
            self.save(update_fields=updated_fields)
            return True, updated_fields

        return False, []

    class Meta:
        abstract = True
