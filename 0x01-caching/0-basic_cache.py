#!/usr/bin/env python3

"""
Module for basic caching system.

This module provides a BasicCache class that defines a basic caching system
without limit.
It allows you to add and retrieve items from the cache using the put and get
methods.

Example:
    >>> from basic_cache import BasicCache
    >>> cache = BasicCache()
    >>> cache.put('user_id', 123)
    >>> cache.get('user_id')
    123
    >>> cache.get('non_existent_key')
    None
"""

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
