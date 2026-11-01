class MyHashMap:

    def __init__(self):
        # Use an array of buckets (769 is a prime number to reduce collisions)
        self.key_range = 769
        self.bucket = [[] for _ in range(self.key_range)]

    def _hash(self, key: int) -> int:
        return key % self.key_range

    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        found = False
        for i, kv in enumerate(self.bucket[bucket_index]):
            if kv[0] == key:
                self.bucket[bucket_index][i] = (key, value)
                found = True
                break
        if not found:
            self.bucket[bucket_index].append((key, value))

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        for kv in self.bucket[bucket_index]:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        for i, kv in enumerate(self.bucket[bucket_index]):
            if kv[0] == key:
                del self.bucket[bucket_index][i]
                return