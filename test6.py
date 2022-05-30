################################LOOOP LISTS##################
#Loop through things using 'for' loop
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# for x in this_is_list:
#     print (x)

#loop through the index number 'range()' and 'len'
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# for i in range (len(this_is_list)):
#     print (this_is_list[i])

#using a 'while' loop
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# i = 0
# while i < len(this_is_list):
#     print(this_is_list[i])
#     i = i + 1

    #looping using List Comprehension
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# [print(x) for x in this_is_list]    

########################LIST COMPREHENSION#####################
#-IT offers a shorter syntax when you want to create a new list based on the values of an existing list
# fruits = ["apple", "tunda", "ruman", "pine", "cherry"]
# list = []
# for x in fruits:
#     if "r" in x :
#         list.append(x)
# print(list)        

# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# list =[x for x in this_is_list if "a" in x]
# print(list)

#condition
#- is like a filter that only accepts the items that valuates to True
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# list = [x for x in this_is_list if x != "tunda"]
# print (list)

#the condition 'if x != "tunda"will return true other than tunda, making the new list contain all fruits except "tunda"

#With no If statement
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# list = [x for x in this_is_list]
# print(list)

#Iterable
#-it can be any iterable object, like a list, tuple, set etc
#- you can use the 'range()' function to create an iterable
# from re import T


# list = [x for x in range (1000000)]
# print(list)

#Expression
#The expression is the current item in the iteration but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
# this_is_list = ["apple", "tunda", "ruman", "pine", "cherry"]
# list = [x.upper() for x in this_is_list]
print (list)


#Scorers
messi2 = [3 + 13]
griezman3 = [2 + 5]
barkley = [2]
mosalah1 = [6 + 6 + 3 + 3]
haaland4 = [5]
mane5 = [3]
mbappe6 = [2]

# print (messi)
# print(griezman)
# print(barkley)
# print(mosalah)
# print(haaland)
# print(mane)
# print(mbappe)

#assisters
lukaku6 = [2]
sterling6 = [2]
ronaldo1 = [1 + 7 + 2]
griezman3 = [7]
neymar4 = [3 + 3]
messi5 = [3 + 2]
mbappe2 = [3 + 6]

print(lukaku)
print(sterling)
print(ronaldo)
print(griezman)
print(neymar)
print(messi)
print(mbappe)
