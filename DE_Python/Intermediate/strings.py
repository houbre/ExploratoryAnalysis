
# back lash tells string to continue on same line
my_string = """Hello \
    world"""

print(my_string)


# back lash tells string to continue on same line
my_string2 = """Hello 
    world"""

print(my_string2)


#strings are immutable

strstring = "hello world"

subStr = strstring[1:5]
print(subStr)


# concat strings with +
name = "louis"
last_name = "habre"

print(name + " " + last_name)


# iterate through string
for letter in last_name:
    print(letter)



# remove whitespaces
    
wssring = '          Hello World       '
print(wssring)
stripped = wssring.strip()
print(stripped)


#upper, lower, startswith, endswith
stringgg = 'Hello World'
print(stringgg.startswith('He')) # true
print(stringgg.endswith('ld')) # true
print(stringgg.lower()) #hello world
print(stringgg.upper()) #HELLO WORLD



#find index
some_string = 'Hello World'
print(some_string.find('o')) # index 4
print(some_string.count('o')) # 2 occurence of 'o'


# replace : returns new string
print(some_string.replace('World', 'Earth'))


# split string
split_string = 'How are you doing'
haha_list = split_string.split() # ['How', 'are', 'you', 'doing']
print(haha_list)


comma_string = 'How,are,you,doing'
hahaha_list = comma_string.split(",") # ['How', 'are', 'you', 'doing']
print(hahaha_list)


# to string .join
conv_str = ' '.join(haha_list)
print(conv_str) # How are you doing -> back to the original list


# ways to make a string in python
from timeit import default_timer as timer

a_list = ['a'] * 6


#badddddd
start = timer()
for_string =  ''
for i in a_list:
    for_string += i
stop = timer()
print(stop - start) # result : 11.674408320001021 (the test is  with 6000000)

#good!!
start = timer()
a_list_str = ''.join(a_list)
stop = timer()
print(stop - start) # result : 0.5410210649988585 (the test is  with 6000000)


# formatting string

# either % operator, .format or f-string
var = "Tom"
c_string = "the variable is %s" % var
print(c_string)


var = 5.678958373
d_string = "the variable is %.2f" % var
print(d_string)


# new way is .format
var = 5.678958373
e_string = "the variable is {}".format(var)
print(e_string)

# new way is .format
var = 5.678958373
f_string = "the variable is {:.2f}".format(var)
print(f_string)


# with 2 variables
var = 5.678958373
var2 = 7.443
g_string = "the variable is {:.2f} and {}".format(var, var2)
print(g_string)


# new new mordern way : f string
var = "hahahaha"
h_string = f"the variable is {var}"
print(h_string)







