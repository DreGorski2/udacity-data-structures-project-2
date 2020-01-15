
union adds all nodes from each list to a set which removes dupes and allows us to output only unique values present in
the list. Intersection also uses a set for the same reason to not allow dupes so we only get the unique value present in
both lists without collisions.

**Time Complexity:** for both functions is O(n) since sets use hashtables and we're only iterating through one
                    item at any given time<br/>

**Space Complexity:** O(n) since we're storing the values in a list for both union and intersection