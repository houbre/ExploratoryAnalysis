
#product
from itertools import product

a = [1,2]
b = [3,4]

prod = product(a,b)
print(list(prod)) #[(1, 3), (1, 4), (2, 3), (2, 4)]

c = [1,2]
d = [3]

prod2 = product(c,d, repeat=2)
print(list(prod2)) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]


# permutations

from itertools import permutations

a = [1,2,3]
perm = permutations(a)
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm2 = permutations(a, 2) # permutations of length 2
print(list(perm2)) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


from itertools import combinations

a = [1,2,3]
comb = combinations(a, 2)
print(list(comb)) # [(1, 2), (1, 3), (2, 3)]



#accumulate

from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)
print(list(acc)) #[1, 3, 6, 10]


#group by
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
groupby_obj = groupby(a, key=smaller_than_3)

for key, value in groupby_obj:
    print(key, list(value))   #True [1, 2] \ False [3, 4]


persons = [{'name' : 'Tim', 'age' : 25}, {'name' : 'Dan', 'age' : 25}, {'name' : 'Lisa', 'age' : 27}, {'name' : 'Claire', 'age' : 28}]

group_by_obj = groupby(persons, key=lambda x : x['age'])

for key, value in group_by_obj:
    print(key, list(value))


# infinite iterators
from itertools import count, cycle, repeat

# count will loop forever form that value
a = [1,2,3]

for i in count(10):
    print(i)
    if i == 15:
        break


# cycle will cycle through an a forever

#for i in cycle(a):
#    print(i)




# repeat will repeat an element for every stop condition as 2nd arg
for i in repeat(10, 4):
    print(4)



