This project involves implementing different caching systems using various cache replacement policies such as FIFO (First In, First Out), LIFO (Last In, First Out), LRU (Least Recently Used), MRU (Most Recently Used), and LFU (Least Frequently Used). Each caching system is to be implemented in a Python class that inherits from a provided `BaseCaching` class. Here is a breakdown of the tasks:

### Task 0: Basic Dictionary Caching (`BasicCache`)

- **Class:** `BasicCache`
- **Methods to implement:**
  - `put(self, key, item)`: Adds an item to the cache.
  - `get(self, key)`: Retrieves an item from the cache by key.
- **Notes:**
  - No cache limit.
  - If `key` or `item` is `None`, the method should do nothing.

### Task 1: FIFO Caching (`FIFOCache`)

- **Class:** `FIFOCache`
- **Methods to implement:**
  - `put(self, key, item)`: Adds an item to the cache using the FIFO strategy.
  - `get(self, key)`: Retrieves an item from the cache by key.
- **Notes:**
  - When the cache exceeds the limit (`MAX_ITEMS`), discard the first added item.
  - Print `DISCARD:` followed by the discarded key.

### Task 2: LIFO Caching (`LIFOCache`)

- **Class:** `LIFOCache`
- **Methods to implement:**
  - `put(self, key, item)`: Adds an item to the cache using the LIFO strategy.
  - `get(self, key)`: Retrieves an item from the cache by key.
- **Notes:**
  - When the cache exceeds the limit, discard the last added item.
  - Print `DISCARD:` followed by the discarded key.

### Task 3: LRU Caching (`LRUCache`)

- **Class:** `LRUCache`
- **Methods to implement:**
  - `put(self, key, item)`: Adds an item to the cache using the LRU strategy.
  - `get(self, key)`: Retrieves an item from the cache by key.
- **Notes:**
  - When the cache exceeds the limit, discard the least recently used item.
  - Print `DISCARD:` followed by the discarded key.

### Task 4: MRU Caching (`MRUCache`)

- **Class:** `MRUCache`
- **Methods to implement:**
  - `put(self, key, item)`: Adds an item to the cache using the MRU strategy.
  - `get(self, key)`: Retrieves an item from the cache by key.
- **Notes:**
  - When the cache exceeds the limit, discard the most recently used item.
  - Print `DISCARD:` followed by the discarded key.

### Task 5: LFU Caching (`LFUCache`) [Advanced]

- **Class:** `LFUCache`
- **Methods to implement:**
  - `put(self, key, item)`: Adds an item to the cache using the LFU strategy.
  - `get(self, key)`: Retrieves an item from the cache by key.
- **Notes:**
  - When the cache exceeds the limit, discard the least frequently used item.
  - If there’s a tie in frequency, discard the least recently used item.
  - Print `DISCARD:` followed by the discarded key.

### Implementation Tips:

1. **BaseCaching Class:** Ensure your classes properly inherit from `BaseCaching`.
2. **Documentation:** Include appropriate docstrings for each module, class, and method.
3. **Testing:** You can test your implementation using the provided `main.py` files to ensure correctness.
