# Спасибо, jhorman! https://gist.github.com/jhorman/8062862

from uuid import uuid4
from time import time, sleep


class RedisSemaphore:
    """ Redis base semaphore. Supports timeouts of semaphore locks """

    def __init__(self, redis, name, limit, timeout_seconds=10):
        """
        Timeout specifies how long taken semaphores are valid. Expired semaphores don't count
        toward the total taken count. Crashed clients therefore will release their locks after
        timeout seconds.
        @name Redis key name for zset
        @limit Number of locks to allow
        @timeout_seconds How long to allow old locks to persist.
        """
        super(RedisSemaphore, self).__init__()
        self.__redis = redis
        self.__name = 'semaphore:%s' % name
        self.__limit = limit
        self.__timeout = timeout_seconds
        self.__lock_id = uuid4().hex

    def __enter__(self, blocking=True, wait_for_seconds=5):
        """
        Take out a semaphore. Must be released later. Returns false
        if a lock couldn't be acquired.

        @block If true keeps trying to get the lock for timeout seconds.
        @timeout How long to wait for the lock. Returns false if lock not avail.
        """

        def acquire_lock(transaction):
            # how many locks are already taken in the set. ignores locks that have timed out.
            now = time()
            count = transaction.zcount(self.__name, now-self.__timeout, now+1)
            # set the pipline back to buffered mode
            transaction.multi()
            # if there is space in the set for an additional lock append it to the list
            if count < self.__limit:
                # the score of the lock is current time so that locks can expire
                transaction.zadd(self.__name, self.__lock_id, time())
                return True
            # no space available, return False
            return False

        # keep trying to get the lock for wait_for_seconds seconds
        start = time()
        while (time() - start) < wait_for_seconds:
            if self.__redis.transaction(acquire_lock, self.__name, value_from_callable=True):
                now = time()
                return True
            elif blocking:
                self.cleanup()
                sleep(.1)

        return False

    acquire = __enter__

    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        """ Отпустить блокировку после удаление """

        self.__redis.zrem(self.__name, self.__lock_id)

    release = __exit__

    def cleanup(self):
        """ Удаляет все замки после истечения срока действия тайм -аута из отсортированного набора """
        return self.__redis.zremrangebyscore(self.__name, 0, time()-self.__timeout)


"""
Пример использования:

redis_client = redis.Redis(host='localhost', port=6379)

semaphore = RedisSemaphore(
    redis=redis_client,
    name="api_rate_limit",
    limit=10,
    timeout_seconds=2
)

if semaphore.acquire(blocking=True, wait_for_seconds=5):
    try:
        # Выполнение API-запроса
        print("Запрос выполнен!")
    finally:
        semaphore.release()
else:
    print("Не удалось получить семафор: превышен лимит запросов.")
"""
