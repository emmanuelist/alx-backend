#!/usr/bin/env python3

"""
LFUCache module

This module provides an implementation of a Least Frequently Used (LFU)
caching system.
It defines a single class, LFUCache, which inherits from BaseCaching and
provides an LFU cache implementation.

The LFUCache class uses a dictionary to store the cache data, a defaultdict to
store the frequency of each key,
and a list to store the order of access.

Example usage:
    >>> from lfu_cache import LFUCache
    >>> cache = LFUCache()
    >>> cache.put("key1", "value1")
    >>> cache.put("key2", "value2")
    >>> cache.get("key1")
    'value1'
"""

from collections import defaultdict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used (LFU) caching system.

    This class inherits from BaseCaching and provides an implementation
    of an LFU cache.
    It uses a dictionary to store the cache data, a defaultdict to store
    the frequency of each key,
    and a list to store the order of access.

    Attributes:
        freq (defaultdict): A dictionary to store the frequency of each key.
        order (list): A list to store the order of access.

    Methods:
        put(key, item): Add an item to the cache.
        get(key): Get an item from the cache by key.
    """

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.freq = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key = min(
                self.order,
                key=lambda k: (
                    self.freq[k],
                    self.order.index(k)))
            del self.cache_data[lfu_key]
            del self.freq[lfu_key]
            self.order.remove(lfu_key)
            print(f"DISCARD: {lfu_key}")
        self.cache_data[key] = item
        self.freq[key] += 1
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
