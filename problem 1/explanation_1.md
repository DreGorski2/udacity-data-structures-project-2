
Implementation of the LRU cache uses a doubly linked so we can keep track of the last and next value for 
each item in the list. We use a dict to store the key value pairs which allows us to perform constant
time operations on our doubly linked list.


**Time Complexity:** O(1) .get and .set are in constant time regardless of size of array
**Space Complexity:** O(n) where n is the capacity of the cache