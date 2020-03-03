The main component of our block chain is going to be linking each block so it can be
referenced by its predecessor which is why I chose to store the blocks in a linked list<br/>

**Time complexity:** Creating the linked list and assigning values to the Block take both take O(1) and run time does
stays linear regardless of input size. adding a block to the chain will take O(n) where n indicates the blocks

**Space Complexity:** O(n) with n indicating the number of blocks in the array