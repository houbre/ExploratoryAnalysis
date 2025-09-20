# collection: Counter, namedtuple, ordereddict, defaultdict, deque


from collections import Counter

a = 'aaaaaaabbbbbbbbbbbbbbbccccdcdvefvveefvfvfefevecfceccecfe'
my_counter = Counter(a)
print(my_counter) #Counter({'b': 15, 'c': 10, 'e': 9, 'a': 7, 'f': 7, 'v': 6, 'd': 2})
print(my_counter.keys()) # dict_keys(['a', 'b', 'c', 'd', 'v', 'e', 'f'])
print(my_counter.values()) # dict_values([7, 15, 10, 2, 6, 9, 7])
print(my_counter.most_common(2)) #[('b', 15), ('c', 10)] : list with tuples in it
print(my_counter.most_common(1)[0][0]) # most common key


#convert counter to list
print(list(my_counter.elements())) #['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'v', 'v', 'v', 'v', 'v', 'v', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'f', 'f', 'f', 'f', 'f', 'f', 'f']



# basically creates a class
from collections import namedtuple

point = namedtuple("Point", "x,y")
pt = point(1, 6)
print(pt) # Point(x=1, y=6)


from collections import OrderedDict

my_dict = OrderedDict()
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3
my_dict['d'] = 4

print(my_dict)


from collections import defaultdict

my_dict = defaultdict(int)
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3
my_dict['d'] = 4

print(my_dict['0'])
print(my_dict)


from collections import deque

dequeue = deque()

dequeue.append(1)
dequeue.append(2)
dequeue.append(3)
dequeue.append(4)

print(dequeue)


dequeue.appendleft(99)
print(dequeue) #99, 1, 2, 3, 4]






