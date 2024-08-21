#!/usr/bin/env python3

"""
FIFO Cache Module

This module provides a FIFO (First-In-First-Out) caching system.

Example usage:
    cache = FIFOCache()
    cache.put("key1", "item1")
    cache.put("key2", "item2")
    cache.put("key3", "item3")

    print(cache.get("key1"))  # Output: item1
    print(cache.get("key2"))  # Output: item2
    print(cache.get("key3"))  # Output: item3

    cache.put("key4", "item4")  # This will discard key1
    print(cache.get("key1"))  # Output: None
    print(cache.get("key2"))  # Output: item2
    print(cache.get("key3"))  # Output: item3
    print(cache.get("key4"))  # Output: item4
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key not in self.cache_data and len(
                self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")
        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
