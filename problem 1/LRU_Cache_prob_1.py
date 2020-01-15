# For our first problem, the goal will be to design a data structure known as a
#  Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we
#  remove the least recently used entry when the cache memory reaches its limit.
#  For the current problem, consider both get() and set() operations as an use operation.
#
# # Your job is to use an appropriate data structure(s) to implement the cache.
# #
# # In case of a cache hit, your get() operation should return the appropriate value.
# # In case of a cache miss, your get() should return -1.
# # While putting an element in the cache, your put() / set() operation must insert the element.
#  If the cache is full, you must write code that removes the least recently used entry first
#  and then insert the element.
# # All operations must take O(1) time.
# #
# # For the current problem, you can consider the size of cache = 5.

# problem solved as a doubly linked list

class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = DoubleNode(0, 0)
        self.tail = DoubleNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if key in self.dict:
            self.remove(self.dict[key])
        node = DoubleNode(key, value)
        self.add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dict[node.key]
        pass

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail


our_cache = LRU_Cache(5)


print(our_cache.set(1, 1))
print(our_cache.set(2, 2))
print(our_cache.set(3, 3))
print(our_cache.set(4, 4))



print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

print(our_cache.set(5, 5))
print(our_cache.set(6, 6))

print(our_cache.get(3))  # -1 added 5, 6  3 was pushed out of the cache
print(our_cache.dict)



