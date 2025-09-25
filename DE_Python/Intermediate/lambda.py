

add10 = lambda x: x + 10

print(add10(5))


# same as 
#def add10_func(x):
#    return x + 10


mult = lambda x,y: x* y
print(mult(2,7))


points2D = [(1,2), (15,1), (5, -1), (10,4)]
points_sorted = sorted(points2D, key=lambda x : x[1]) # sort by y

print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points_sorted) #[(5, -1), (15, 1), (1, 2), (10, 4)]


points_sorted_sum = sorted(points2D, key = lambda x : x[0] + x[1])
print(points_sorted_sum)


# map functions

a = [1,2,3,4,5]
b = map(lambda x : x * 2, a)
print(list(b))

# same as
#for elem in a:
#    multiply_by_two(elem)

#def multiply_by_two(x):
#   return x * 2


#list comprhension is better though

c = [x * 2 for x in a]
print(c) # [2, 4, 6, 8, 10]


# FILTER FUNCTION
a = [1,2,3,4,5, 6]
b = filter(lambda x : x % 2 == 0, a)
print(list(b)) # [2, 4, 6]


from functools import reduce
# REDUCE FUCNTION
a = [1,2,3,4,5,6]
prod_a = reduce(lambda x,y : x*y, a)
print(prod_a) # 720

