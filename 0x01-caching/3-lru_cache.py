#!/usr/bin/env python3
"""
LRUCache module

This module implements a LRU (Least Recently Used) caching system.

It provides a LRUCache class that inherits from BaseCaching and uses a list
to keep track of the order of access.

Classes:
    LRUCache: A LRU caching system.

"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines a LRU (Least Recently Used) caching system.

    This class inherits from BaseCaching and implements a LRU cache
    using a list
    to keep track of the order of access.

    Attributes:
        cache_data (dict): A dictionary to store the cached data.
        order (list): A list to keep track of the order of access.

    Methods:
        put(key, item): Add an item to the cache.
        get(key): Get an item from the cache.
    """

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
