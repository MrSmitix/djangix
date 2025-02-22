from typing import Callable, Optional

import logging

from functools import wraps
from time import perf_counter_ns

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("TimedLogger")


def timed(
        *,
        logger: logging.Logger = logger,
        level: int = logging.INFO,
        precision: int = 9,
        extra_msg: Optional[str] = None
) -> Callable:
    """
    Декоратор для измерения времени выполнения функции

    :param logger: Используемый логгер
    :param level: Уровень логирования
    :param precision: Точность измерения времени (знаков после запятой)
    :param extra_msg: Дополнительное сообщение для логирования
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = perf_counter_ns()
            try:
                result = func(*args, **kwargs)
            finally:
                end_time = perf_counter_ns()
                elapsed = (end_time - start_time) / 1e9  # наносекунды в секунды

                base_msg = f"Функция {func.__name__} выполнена за {elapsed:.{precision}f} сек"
                message = f"{base_msg} [{extra_msg}]" if extra_msg else base_msg

                logger.log(level, message)

            return result

        return wrapper

    return decorator
