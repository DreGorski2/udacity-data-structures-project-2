
Using recursion to iterate through the ad tree. First checking to see if the user we're looking for is the name of the
group, then checking to see if user is in the users of the group, then loop over the group structure passing in the next
group. I was initially using a BFS with a queue to loop through the tree structure queing and dequeing however the
during implementation of the code seemed very repetitive which lead me to a recursive function.<br/>

**Time Complexity:** O(n*m) where n is the depth of the ad tree and m is the number of users in the ad 
**Space Complexity:** O(n) is dependant on the the number of returns that occur between the users and group lists
