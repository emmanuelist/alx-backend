#!/usr/bin/env python3

"""
Module 4-mru_cache

This module provides an implementation of a Most Recently
Used (MRU) caching system.
The MRUCache class inherits from BaseCaching and provides
a cache storage dictionary
and an order list to maintain the order of access.

Classes:
    MRUCache: A Most Recently Used (MRU) caching system.

"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a Most Recently Used (MRU) caching system.

    This class inherits from BaseCaching and provides an implementation
    of an MRU cache.
    The cache stores items in a dictionary and maintains an order of
    access using a list.
    When the cache is full and a new item is added, the least recently
    used item is discarded.

    Attributes:
        cache_data (dict): The cache storage dictionary.
        order (list): The list of keys in the order of access.

    Methods:
        put(key, item): Adds an item to the cache.
        get(key): Retrieves an item from the cache.
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
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
