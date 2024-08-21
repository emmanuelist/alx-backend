#!/usr/bin/env python3

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a basic caching system without limit"""

    def put(self, key, item):
        """Add an item to the cache with the given key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache by its key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
