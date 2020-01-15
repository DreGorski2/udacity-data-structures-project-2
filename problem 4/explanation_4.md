
Using recursion to iterate through the ad tree. First checking to see if the user we're' looking for is the name of the
group if so break out. Then checking to see if user  is in the users of the group if so breakout and return true.
Then loop over the group structure passing in the next group. Was initially using a BFS with a queue to loop through the
tree structure queing and dequeing however the additional code needed for this seemed like it would be better handled as
a recursive function.

Time Complexity of this solution is O(depth of ad * number of users in ad ),
Space Complexity O(depth of ad * number of users in a)