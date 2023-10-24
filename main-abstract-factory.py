from abc import ABC, abstractmethod
from enum import Enum
from moke import RedisWindows, MemcachedWindows, RedisLinux, MemcachedLinux


class ClientCacheBase(ABC):
    """Interface for Cache clients."""

    @abstractmethod
    def set(self, key, value):
        """Caching Set: function used to set cache"""

    @abstractmethod
    def get(self, key):
        """Caching Get: function used to get cache"""


class RedisWindowsClient(ClientCacheBase):
    def __init__(self, port, host, db):
        self.redis = RedisWindows(port, host, db)

    def set(self, key, value):
        self.redis.redis_set(key, value)

    def get(self, key):
        return self.redis.redis_get(key)


class MemcachedWindowsClient(ClientCacheBase):
    def __init__(self, port, host):
        self.memcached = MemcachedWindows(port, host)

    def set(self, key, value):
        self.memcached.memcached_set(key, value)

    def get(self, key):
        return self.memcached.memcached_get(key)


class RedisLinuxClient(ClientCacheBase):
    def __init__(self, port, host, db):
        self.redis = RedisLinux(port, host, db)

    def set(self, key, value):
        self.redis.redis_set(key, value)

    def get(self, key):
        return self.redis.redis_get(key)


class MemcachedLinuxClient(ClientCacheBase):
    def __init__(self, port, host):
        self.memcached = MemcachedLinux(port, host)

    def set(self, key, value):
        self.memcached.memcached_set(key, value)

    def get(self, key):
        return self.memcached.memcached_get(key)


class CacheType(Enum):
    REDIS = 0
    MEMCACHED = 1


class AbstractFactory(ABC):
    """Interface for Abstract Factory."""

    @abstractmethod
    def getClient(self, cache_type: CacheType):
        """getClient method"""


class WindowsCacheFactory(AbstractFactory):
    def getClient(self, cache_type: CacheType):
        if cache_type == CacheType.REDIS:
            return RedisWindowsClient(host="localhost", port=6379, db=0)
        elif cache_type == CacheType.MEMCACHED:
            return MemcachedWindowsClient(host="localhost", port=11211)


class LinuxCacheFactory(AbstractFactory):
    def getClient(self, cache_type: CacheType):
        if cache_type == CacheType.REDIS:
            return RedisLinuxClient(host="localhost", port=6379, db=0)
        elif cache_type == CacheType.MEMCACHED:
            return MemcachedLinuxClient(host="localhost", port=11211)


class CacheFactoryEnvironment:
    def getCacheFactory(self, is_windows: bool):
        if is_windows:
            return WindowsCacheFactory()
        else:
            return LinuxCacheFactory()


if __name__ == "__main__":
    # Assuming that the environment is Windows
    is_windows = True

    cache_environment = CacheFactoryEnvironment()
    cache_provider: AbstractFactory = cache_environment.getCacheFactory(is_windows)

    redis = cache_provider.getClient(CacheType.REDIS)
    memcached = cache_provider.getClient(CacheType.MEMCACHED)

    redis.set("username", "john_doe")
    username = redis.get("username")
    print(username)
    memcached.set("username", "john_doe2")
    username = memcached.get("username")
    print(username)
