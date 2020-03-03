
union adds all nodes from each list to a set which removes dupes and allows us to output only unique values present in
the list. Intersection also uses a set for the same reason to not allow dupes so we only get the unique value present in
both lists without collisions.

**Time Complexity:** O(n1 + n2) where n is the size of each set the intersection of these two sets then becomes O(n)
where n is the large of the two lists <br/>

**Space Complexity:** O(n) since we're storing the values in a list for both union and intersection where the lists we
create represent n