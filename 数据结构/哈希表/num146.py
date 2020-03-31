from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()
        self._size = 0

    def get(self, key: int) -> int:
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 在cache中
        if key in self._cache:
            self._cache.move_to_end(key)
            self._cache[key] = value
        else:
            # 不在cache中，且cache未满
            if self._size < self._capacity:
                self._cache[key] = value
                self._cache.move_to_end(key)
                self._size += 1
        
            # 不在cache中，且cache已满
            else:
                self._cache.popitem(last = False)
                self._cache[key] = value
                self._cache.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)