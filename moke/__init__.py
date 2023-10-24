# Factory Pattern Example
class Redis:
    def __init__(self, port, host, db):
        self.cache = {}

    def redis_set(self, key, value):
        self.cache[key] = value

    def redis_get(self, key):
        return self.cache.get(key)


class Memcached:
    def __init__(self, host, port):
        self.cache = {}

    def memcached_set(self, key, value):
        self.cache[key] = value

    def memcached_get(self, key):
        return self.cache.get(key)


# Abtract Factory Pattern Example
class RedisWindows:
    def __init__(self, port, host, db):
        self.cache = {}

    def redis_set(self, key, value):
        self.cache[key] = value

    def redis_get(self, key):
        return self.cache.get(key)


class MemcachedWindows:
    def __init__(self, host, port):
        self.cache = {}

    def memcached_set(self, key, value):
        self.cache[key] = value

    def memcached_get(self, key):
        return self.cache.get(key)


class RedisLinux:
    def __init__(self, port, host, db):
        self.cache = {}

    def redis_set(self, key, value):
        self.cache[key] = value

    def redis_get(self, key):
        return self.cache.get(key)


class MemcachedLinux:
    def __init__(self, host, port):
        self.cache = {}

    def memcached_set(self, key, value):
        self.cache[key] = value

    def memcached_get(self, key):
        return self.cache.get(key)
