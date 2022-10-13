
#creating an empty dictionary
empty_dict = {}
empty_dict2 = dict()

#creating a dictionary with intial values
my_dict = {"key1" : "value1", "key2" : 34}

print(my_dict)

#accessing a value inside the dictioary

print(my_dict["key1"])

#using get

print(my_dict.get("rand_key", "deafult value"))

#Adding a new element to the dictionary
my_dict["fav_fruit"] = "Apple"

print(my_dict)

#Adding elements to the dict using update
my_dict.update(key5 = "Value 5", fav_team = "Liverpool")

print(my_dict)

#using a multideimenstional array
my_dict.update([ ["key7", "value7"], ["key8", "value8"]  ])

print(my_dict)

#to delete an element from the dictionary

del my_dict["key1"]

deleted_element = my_dict.pop("key5")
print(deleted_element)

popped_last_element = my_dict.popitem()
print(popped_last_element)

#To test if a key is in the dictionary
if "fav_team" in my_dict:
    print(my_dict["fav_team"])


#looping through a dictionary
for key in my_dict:
    print(my_dict[key])


for key, value in my_dict.items():
    print(f"the key is : {key} , and the value is {value} ")


for value in my_dict.values():
    print(f"the value is : {value}")




print(list(my_dict.keys()))

print(list(my_dict.values()))

print(list(my_dict.items()))