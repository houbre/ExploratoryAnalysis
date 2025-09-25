# pop element
my_list = [1,5,77,99,-1,33]
print(my_list)

popped = my_list.pop()
print(popped)


#reverse list
my_list = [1,5,77,99,-1,33]
print(my_list)

my_list.reverse()
print(my_list)


#sort list
my_list = [1,5,77,99,-1,33]
print(my_list)

my_list.sort()
print(my_list)



# Create new list with * operator
new_list = [5] * 10
print(new_list)


# Slicing
my_list = [1,2,3,4,5,6,7,8,9]
sliced = my_list[1:5]
print(sliced)


# Revsersing list slicing
my_list = [1,2,3,4,5,6,7,8,9]
reversed = my_list[::-1]
print(reversed)


# assigning list to a variable will share the same memory
my_list = ["hey", 'you', 'out']

my_list_2 = my_list

my_list.append("there")

print(my_list)
print(my_list_2) # my list 2 will also have the new appended word


# To avoid that, make a copy
my_list_3 = ["hey", 'you', 'out']

my_list_4 = my_list_3.copy()

my_list_3.append("there")

print(my_list_3)
print(my_list_4) # my list 2 will also have the new appended word



# List comprehension
my_list_comprehension = [1,2,3,4,5]
b = [i*i for i in my_list_comprehension]
print(b)


