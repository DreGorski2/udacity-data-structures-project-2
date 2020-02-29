block chain is similar to a linked list but given the scope of this problem there was not a need to create a linked list
since as we do not need to quickly delete and insert nodes we just want to make sure we're linking each block so it
can be referenced by its predecessor which is why I chose an array to store the blocks.<br/>

**Time complexity:** appending to an array takes O(1) with n indicating the number of blocks in the chain, time complexity
will grow with linearly
**Space Complexity:** O(n) with n indicating the number of blocks in the array