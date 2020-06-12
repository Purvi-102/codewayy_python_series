""" List is a collection which is ordered and changeable it allow duplicate member"""

#Creation of a List
my_list=['apple','papaya','grapes','orange']
print(my_list)

#Access Items
my_list=['apple','papaya','grapes','orange']
print(my_list[2])

#Change Item Value
my_list=['apple','papaya','grapes','orange']
my_list[1]='guava'
print(my_list)

#Loop through a list
my_list=['apple','papaya','grapes','orange']
for x in my_list:
    print(x)

#List Length
my_list=['apple','papaya','grapes','orange']
print(len(my_list))

# Add Items
my_list=['apple','papaya','grapes','orange']
print(my_list.append("cherry"))

# we can use insert method to insert the fruit at specified index
my_list=['apple','papaya','grapes','orange']
my_list.insert(1,"mango")
print(my_list)

#Remove item
#remove() method remove the specified item
my_list=['apple','papaya','grapes','orange']
my_list.remove('papaya')
print(my_list)

# Pop Item
# It remove the last item if index not specified
my_list=['apple','papaya','grapes','orange']
my_list.pop()
print(my_list)

#del keyword
# Remove the specified index
my_list=['apple','papaya','grapes','orange']
del my_list[0]
print(my_list)

#del can also delete the list completely
my_list=['apple','papaya','grapes','orange']
del my_list
print(my_list)

#Copy a list
my_list=['apple','papaya','grapes','orange']
this_list=mylist.copy()
print(this_list)

#List Constructor
my_list=list(('apple','papaya','grapes','orange')) #note the double round brackets
print(my_list)
