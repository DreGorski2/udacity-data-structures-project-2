
I chose to use dictionaries to store the node data and freq data since it allows for O(1) access to the data
since we will be updating and pop'ing data from these objects it seemed to be the most efficient structure.
the PriorityQueue is a list object and allows us to keep track of the freq and node values.<br/>

**Time complexity:** O(N^2)) building the tree, queue and frequency dict, encode, decode all happen in constant time
however given the pop_lfu function is nested in the while loop this make our time complexity O(n^2)
where the run time increase exponentially
**Space Complexity:** O(n) size of the structure grows linearly as input size increases where n is the size of the alphabet
being used