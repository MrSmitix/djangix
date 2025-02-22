from math import pi, cos, sin, sqrt, pow, atan2


def calc_distance(first_lat: float, first_long, second_lat: float, second_long) -> float:
    """
    Функция для расчёта расстояния между двумя точками на шаре

    :param first_lat: широта первого объекта
    :param first_long: долгота первого объекта
    :param second_lat: широта второго объекта
    :param second_long: долгота второго объекта
    :return: расстояние в метрах
    """

    rad = 6372795

    lat1 = first_lat * pi / 180.
    lat2 = second_lat * pi / 180.
    long1 = first_long * pi / 180.
    long2 = second_long * pi / 180.

    cl1 = cos(lat1)
    cl2 = cos(lat2)
    sl1 = sin(lat1)
    sl2 = sin(lat2)

    delta = long2 - long1

    c_delta = cos(delta)
    s_delta = sin(delta)

    y = sqrt(pow(cl2 * s_delta, 2) + pow(cl1 * sl2 - sl1 * cl2 * c_delta, 2))
    x = sl1 * sl2 + cl1 * cl2 * c_delta

    dist = atan2(y, x) * rad

    return dist
