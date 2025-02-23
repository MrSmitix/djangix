from functools import wraps
from time import time, sleep

from django.core.cache import caches


class RedisRateLimiter:
    def __init__(self, default_limit=10, default_window=60, default_delay=0):
        self.settings = {}
        self.default_settings = {
            'limit': default_limit,
            'window': default_window,
            'delay': default_delay
        }

    def add_service(self, service_name, limit=None, window=None, delay=None):
        self.settings[service_name] = {
            'limit': limit or self.default_settings['limit'],
            'window': window or self.default_settings['window'],
            'delay': delay or self.default_settings['delay']
        }

    def _get_service_settings(self, service_name):
        return self.settings.get(service_name, self.default_settings)

    def __call__(self, service_name, timeout: int = 10):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                service_settings = self._get_service_settings(service_name)
                limit = service_settings['limit']
                window = service_settings['window']
                delay = service_settings['delay']

                cache = caches['default']
                lock_key = f'ratelimit:{service_name}:lock'
                count_key = f'ratelimit:{service_name}:count'
                timestamp_key = f'ratelimit:{service_name}:timestamp'

                while True:
                    with cache.lock(lock_key, timeout=timeout):
                        now = time()
                        last_timestamp = cache.get(timestamp_key) or now
                        current_count = cache.get(count_key) or 0

                        # Reset counter if window has passed
                        if now - last_timestamp > window:
                            current_count = 0
                            last_timestamp = now

                        if current_count < limit:
                            # Update counters
                            cache.set(count_key, current_count + 1, timeout=window)
                            cache.set(timestamp_key, last_timestamp, timeout=window)
                            break

                        # Calculate wait time and sleep
                        wait_time = window - (now - last_timestamp)
                        sleep(max(wait_time, 0))

                    # Sleep outside the lock to allow other processes
                    sleep(0.1)

                # Add per-request delay if needed
                if delay > 0:
                    sleep(delay)

                return func(*args, **kwargs)

            return wrapper

        return decorator


"""
Пример использования:

limiter = RedisRateLimiter(default_limit=1, default_window=1, default_delay=1)

limiter.add_service('my_api', limit=1, window=1, delay=1)  # 1 запрос в секунду
limiter.add_service('my_api_hourly', limit=10000, window=3600)  # 10к запросов в час

@limiter('my_api')
def call_my_api():
    return "OK"
"""
