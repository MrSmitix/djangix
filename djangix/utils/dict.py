def dict_cleaner(input_dict: dict):
    """ Отчищает dict от всех пустых значений """

    return {k: v for k, v in input_dict.items() if v not in (None, '', [], {}, set())}
