# ##############PYTHON LISTS##################
# -Lists are used to store multiple items in a single variable

# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# allowing duplicates
# fruits = ["apple", "banana", "cherry", "banana", "cherry"]
# print(fruits)

# list length
# fruits = ConnectionRefusedError
# print(len(fruits))

# list items - Data Types
# list1 = ["apple", "banana", "cherry", "banana", "cherry"]
# list2 = [1, 2, 3, 4, 5, 6]
# list3 = [True, False, False, True]

# print(len(list1))
# print(type(list2))
# print(type(list3))

# #################The List Constructor######################
# this_is_list = list(("apple", "banana", "cherry", "banana", "cherry"))
# print(this_is_list)

# #################Python Collections (Arrays)##############
# --LIST = is a collection which is ordered and changeable.Allows duplicate memebers
# --TUPLE = is a collection which is odered and unchangeable.Allows duplicate members
# --SET = is a collection which is unordered, unchangeable, and un indexed.No duplicate members.
# --Dictionary = is a collection which is ordered** and changeable.No duplicate memebers.

# ################Access List Items#################
# this_is_list = ["apple", "banana", "pie", "banana", "cherry"]
# print(this_is_list[-3])

# ########Range of Indexing##############
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# print (this_is_list[-4:-3])

# ########Check If Items Exist#################
# To Determine use 'in' keyword
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# if 'apple' in this_is_list:
#     print("yes , 'apple' is in the fruit list")

# ####Change List Items######
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list[4] = "blackcurrent"
# print (this_is_list)

# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list[4:1] = "blackcurrent", "melon"
# print (this_is_list)

# ######Insert Items###########
# use the 'insert()'------inserts an item at a specified index
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list.insert(3, "watermelon")
# print (this_is_list)

# ##########Add List Items###########
# Use the 'append()'----used to add an item at the end
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list.append("orange")
# print(this_is_list)

# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list.insert(3, "orange")
# print(this_is_list)

# #####Extend List######
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# list3 = ["tomoko", "satap", "reibena", "zagav", "zabibu"]
# this_is_list.extend(list3)
# print(this_is_list)

# #######Remove List Items##########
# ----'.remove()' = Removes the specified item
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list.remove("tunda")
# print(this_is_list)

# -------'pop()'  = Renoves the specified index
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list.pop(2)
# print(this_is_list)

# --------'pop()' =! if you dont specify the index the pop removes the last item in the list
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list.pop()
# print(this_is_list)

# ---------'del' = also delets specified item in the list
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# del this_is_list

# ----------'clear()' = the method empties the list
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# this_is_list.clear()
# print(this_is_list)