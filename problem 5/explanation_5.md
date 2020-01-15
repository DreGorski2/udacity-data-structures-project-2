block chain is similar to a linked list but given the scope of this problem there was not a need to create a linked list
since as we do not need to quickly delete and insert nodes we just want to make sure we're' linking each block so it
can be referenced by its predecessor which is why I chose an array to store blocks .

Time complexity: appending to an array takes O(n) with n indicating the number of blocks in the chain
Space Complexity: also O(n) with n indicating the number of blocks