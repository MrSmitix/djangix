def levenshtein_distance(first, second):
    """
    Расчёт "идентичности" двух строк по Левенштейну

    :param first: первая строка
    :param second: вторая строка
    :return: коэффициент похожести
    """

    n, m = len(first), len(second)

    if n > m:
        second, first = second, first
        n, m = m, n

    current_row = list(range(n + 1))

    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if first[j - 1] != second[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def unicode_strike(text: str) -> str:
    """ Зачеркивание текста, спасибо unicode """

    return "\u0336".join(text) + "\u0336" if text else text
