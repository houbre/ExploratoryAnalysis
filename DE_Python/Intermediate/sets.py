my_set = set([1,2,3])
print(my_set)

# add 
my_set.add(4)
my_set.add(6)
my_set.add(5)

print(my_set)

# remove if found in set
my_set.remove(3)
print(my_set)

# key error if removing elem not in set
#my_set.remove(11)

# use discard : removes if found
my_set.discard(4)
print(my_set)


print(my_set.pop())



# union of sets

odds = {1,3,5,7}
even = {2,4,6,8}

u = odds.union(even)
print(u)

# can also calculate difference and inersection
#d = odds.difference(even)
#i = odds.intersection(even)


# update sets by adding elements to it
print(odds)
odds.update(even)
print(odds)


# frozenset is immutable version of normal set

a = frozenset([1,2,3,4])

#a.add(5) error!
