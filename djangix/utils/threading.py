from functools import wraps


def synchronized(lock_name: str):
    """
    Декоратор на метод класса, аналог Java synchronized,
    принимает имя члена класса, которое должно являться каким-либо Lock-ом

    Пример:
        def __init__(self):
            self._lock_signals = threading.Lock()
            ...

        @synchronized('_lock_signals')
        def get_signals(self, ...):
            ...
    """

    def decorator(method):
        @wraps(method)
        def synced_method(self, *args, **kwargs):
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kwargs)
        return synced_method
    return decorator
