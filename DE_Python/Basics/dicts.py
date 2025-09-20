# basics dict

my_dict = {"name" : "lousi", "age": 25}
print(my_dict)


my_dict2 = dict(name="louis", age=25)
print(my_dict2)


#access value
print(my_dict2["age"])


#add value
my_dict["new_key"] = "hahha"
print(my_dict)


#delete value
my_dict.pop("new_key")

#check if key in dict
if "name" in my_dict:
    print(my_dict["name"])


#name not in dict -> error
try:
    print(my_dict["names"])
except:
    print("error")



# iterating through dict
    
# through keys
for key in my_dict:
    print(key)

#through values
for value in my_dict.values():
    print(value)  

# both
for key, value in my_dict.items():
    print(f"key: {key}, 'value: {value}")


# merge dicts
m_dict_1 = {"name" : "lousi", "age": 25, 'email':'hahah@haahha'}
m_dict_2 = {"name" : "emma", "age": 27, 'city' : 'boston'}


m_dict_1.update(m_dict_2)
print(m_dict_1)


# use tuple as key

tuple_dict = {(1,2) : 3}
print(tuple_dict)

# cannot have list as key -> error
