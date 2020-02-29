
I used recursion because A. we could have solved this problem with a for loop , and B. there was a base condition that
could be met (travers all directories/files)<br/>

**Time complexity:** O(m*n) m being the directories/subdirectories, n being the number of files in those directories
since time comlexity is calculated as such because we need to first loop over all sub-directories (m) then loop over all the
files within those subdirectories(n) until we have looped over all sub-directories and their associated files.
**Space Complexity:** O(m*n) is dependent on the amount of subdirectories and the number of files in those directories
that meet our specified criteria noting that we're tracking the path list throughout this recursion append at each level 
of the directory