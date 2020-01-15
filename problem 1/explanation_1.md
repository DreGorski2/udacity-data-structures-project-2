
Initially thinking dictionary after seeing O(1) time complexity and using .get method to get values from the dict.
However we need to keep track of the order of the values which leads me to lists in particular doubly linked lists so
I can keep track of what is in front and behind of each value in the list.<br/>

**Time Complexity:** O(1) .get and .set in constant time regardless of size of array<br/>
**Space Complexity:** O(1) is the temp space created for any .get .set action performed