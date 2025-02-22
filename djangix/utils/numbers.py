from decimal import Decimal


def round_decimal(value: Decimal, places: int):
    """
    Округляет decimal до указанного знака

    :param value: оригинальный decimal
    :param places: точность, чисел после ,
    :return: decimal
    """

    if value is not None:
        return value.quantize(Decimal(10) ** -places)

    return value
