#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

#Create a dictionary
my_dict = {   "fruit": "apple",   "color": "red" }
print(my_dict)    

#Accessing Items
my_dict = {   "fruit": "apple",   "color": "red" }
x=my_dict[color]
print(x)

#Loop through dictionary
#Print all key names in the dictionary, one by one:
my_dict = {   "fruit": "apple",   "color": "red" }
for x in my_dict:
    print(x)

#Print all values in the dictionary, one by one
my_dict = {   "fruit": "apple",   "color": "red" }
for x in my_dict:
    print(my_dict[x])

#Loop through both keys and values, by using the items() function: 
for x, y in my_dict.items():
    print(x, y)

# Dictionary Length
my_dict = {   "fruit": "apple",   "color": "red" }
print(len(my_dict))

#Add Item
my_dict = {   "fruit": "apple",   "color": "red" }
my_dict[brand]:"pure"
print(my_dict)

#POP method
#It remove the specified item with specified key name
my_dict = {   "fruit": "apple",   "color": "red" }
my_dict.pop("fruit")
print(my_dict)

# del keyword
my_dict = {   "fruit": "apple",   "color": "red" }
del my_dict
print(my_dict)

#Copy a dictionary
my_dict = {   "fruit": "apple",   "color": "red" }
this_dict=my_dict.copy()
print(this_dict)

#Dict Constructor
my_dict = (   "fruit"= "apple",   "color"= "red" )
print(my_dict)





 
