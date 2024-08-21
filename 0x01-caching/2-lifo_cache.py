#!/usr/bin/env python3

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a LIFO caching sysytem"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache with the given key"""
        if key is None or item is None:
            return
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
