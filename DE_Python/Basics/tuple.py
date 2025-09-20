# tuple is immutable, can be more than 2 elements

my_tuple = ("louis", "mtl", 25)
print(my_tuple)
print(type(my_tuple))

#no comma is not a tuple
my_tuple_2 = ("louis")
print(my_tuple_2)
print(type(my_tuple_2)) #str


#access
item = my_tuple[0]
print(item) #louis


item2 = my_tuple[-1] #access last item 
print(item2)


#iterate trhough tuple
for x in my_tuple:
    print(x)


# check if elem is in tuple
print(25 in my_tuple)


#size of tuple
print(len(my_tuple))

#count elements in tuple
my_tuple = ("louis", "mtl", 25, 25, 25, 25)
print(my_tuple.count(25))


# search for index of element
print(my_tuple.index("mtl"))


# convert tuple to list and vice versa
my_tuple = ("louis", "mtl", 25, 25, 25, 25)

new_list = list(my_tuple)
print(new_list)


new_tuple = tuple(new_list)
print(new_tuple)


#unpac tuple
unpack_tup = ("louis", "mtl", 25)
name, city, age = unpack_tup
print(name)
print(city)
print(age)


numbers_tup = (1,2,3,4,5,6,7,8,9)
i1, *i2, i3 = numbers_tup
print(i1) # 1
print(i2) # [2, 3, 4, 5, 6, 7, 8]
print(i3) # 9


# list more expensive than tuple
import sys

tuple_size = ("louis", "mtl", 25)
list_size = ["louis", "mtl", 25]

print(sys.getsizeof(tuple_size), "bytes") #64
print(sys.getsizeof(list_size), "bytes") #88


# compare effeciency of tuple vs list

import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000)) # 5.8287998399464414e-05
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000)) # 1.0028001270256937e-05 ->  faster

