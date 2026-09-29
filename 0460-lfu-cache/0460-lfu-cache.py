from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_map = {}  # key -> (value, freq)
        self.freq_map = defaultdict(OrderedDict)  # freq -> OrderedDict(key -> None)
        self.min_freq = 0

    def _update_freq(self, key, value=None):
        """Helper to increment the frequency of a key."""
        val, freq = self.key_map[key]
        if value is not None:
            val = value  # Update value if provided during put
        
        # Remove key from its current frequency list
        del self.freq_map[freq][key]
        
        # If the current frequency list is empty and it was min_freq, increment min_freq
        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1
            
        # Move key to the next frequency list
        freq += 1
        self.key_map[key] = (val, freq)
        self.freq_map[freq][key] = None
        return val

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_map:
            return -1
        return self._update_freq(key)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity <= 0:
            return

        # If key already exists, update its value and increment frequency
        if key in self.key_map:
            self._update_freq(key, value)
            return

        # If cache is full, evict the LFU (and LRU) key
        if len(self.key_map) >= self.capacity:
            # popitem(last=False) pops in FIFO order (least recently used)
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[evict_key]

        # Insert new key with frequency 1
        self.key_map[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1