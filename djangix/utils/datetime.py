from zoneinfo import ZoneInfo
from datetime import datetime, date


def get_utc_offset(tz_name: str):
    """ Возвращает смещение по UTC в секундах """

    return datetime.now(ZoneInfo(tz_name)).utcoffset().total_seconds()


def calc_age(birthdate: date, target_date: date | None = None) -> int:
    """
    Вычисление возраста на определенную дату (или на сегодня) по дате рождения

    :param birthdate: дата рождения пользователя
    :param target_date: дата на которую нужно посчитать, по умолчанию - текущая
    :return: возраст в годах
    """

    today = target_date or date.today()

    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
