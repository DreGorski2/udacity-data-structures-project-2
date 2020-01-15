
I chose to use dictionaries to store the node data and freq data since it allows for O(1) access to data
since we will be updating and pop'ing data from these objects it seemed to be the most efficient structure.
the PriorityQueue is a list object to easily keep track of the freq and node values.

Time complexity: O(n) since building the tree, queue and frequency dict, encode, decode all happen in constant time
                 where the size of the input increase the time in a linear fashion
Space Comlexity: O(n) size of the structure grows linearly as input size increases