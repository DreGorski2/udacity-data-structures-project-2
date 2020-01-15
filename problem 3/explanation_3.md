
I chose to use dictionaries to store the node data and freq data since it allows for O(1) access to the data
since we will be updating and pop'ing data from these objects it seemed to be the most efficient structure.
the PriorityQueue is a list object and allows us to keep track of the freq and node values.<br/>

**Time complexity:** O(n) since building the tree, queue and frequency dict, encode, decode all happen in constant time
                 where the size of the input increase the time in a linear fashion<br/>
**Space Complexity:** O(n) size of the structure grows linearly as input size increases