#A tuple is a collection which is ordered and unchangeable.

#Create a Tuple: 
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#Access Item
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[2])

#Change Tuple Values 
# Once a tuple is created, you cannot change its values. Tuples are unchangeable.

#Loop Through a Tuple
my_tuple = ("apple", "banana", "cherry")
for x in my_tuple:
    print(my_tuple)

#Tuple Length
my_tuple = ("apple", "banana", "cherry")
print(len(my_tuple))

#Add Values
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
my_tuple = ("apple", "banana", "cherry")
my_tuple[3] = "orange" # This will raise an error print(thistuple)   
print(my_tuple)

#Delete a Item
# We cannot delete an item as tuples are immutable.
#we can delete tuple completely
my_tuple = ("apple", "banana", "cherry")
del my_tuple
print(my_tuple)

#Tuple Constructor

my_tuple = tuple(("apple", "banana", "cherry")) #note the double round brackets
print(my_tuple)
