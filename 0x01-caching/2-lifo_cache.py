#!/usr/bin/env python3
"""
Module: lifo_cache.py

This module defines a LIFO (Last In First Out) caching system.

Classes:
    LIFOCache: A class that implements a LIFO caching system.

Examples:
    >>> from lifo_cache import LIFOCache
    >>> cache = LIFOCache()
    >>> cache.put("key1", "value1")
    >>> cache.put("key2", "value2")
    >>> cache.get("key1")
    'value1'
    >>> cache.put("key3", "value3")
    DISCARD: key1
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a LIFO (Last In First Out) caching system.

    This class inherits from BaseCaching and implements a LIFO caching system.
    It keeps track of the last key added to the cache and discards it when the
    cache is full.
    """

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache with the given key"""
        if key is None or item is None:
            return
        if key not in self.cache_data and len(
                self.cache_data) >= BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
