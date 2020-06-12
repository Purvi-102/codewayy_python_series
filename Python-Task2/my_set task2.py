# Set is a collection which is unordered and unindexed. It remove all duplicate entries.

#Create a Set
my_set = {"apple", "banana", "cherry"}
print(my_set)

# Access Item
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index. 
#But you can loop through the set items using a for loop
my_set = {"apple", "banana", "cherry"}  
for x in my_set:
    print(x)

#Change Item
#Once set is created you cannot change item.

#Add Item
#Add an item to a set, using the add() method:

my_set = {"apple", "banana", "cherry"}  
my_set.add("orange")  
print(my_set)

#Update() Method
#Add multiple items
my_set = {"apple", "banana", "cherry"}  
my_set.update(["orange", "mango", "grapes"])  
print(my_set)

#Length of a Set
my_set = {"apple", "banana", "cherry"}  
print(len(my_set))   

#Remove Item
my_set = {"apple", "banana", "cherry"}  
my_set.remove("banana")
print(my_set)

# Note: If the item to remove does not exist, remove() will raise an error. Example 

#Remove "banana" by using the discard() method: 
my_set = {"apple", "banana", "cherry"}  
my_set.discard("banana")  
print(my_set)  

#Note: If the item to remove does not exist, discard() will NOT raise an error

my_set = {"apple", "banana", "cherry"}  
x = my_set.pop()  
print(x)  
print(my_set)  

#Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed. 

# Del Keyword
my_set = {"apple", "banana", "cherry"}  
del my_set  
print(my_set)   

#The set() Constructor
my_set = set(("apple", "banana", "cherry")) # note the double roundbrackets
print(my_set)   



