#a = "hello world"
#print (a[0])

#for x in "basana":
#print(x)

#a = "hello there"
#print(len(a))

#text = "the best thing in is to have a maid!"
#if "expensive" not in text:
#    print("no, 'expensive' is not present.")


#######################
#SLICING
#######################

#b = "hello there mr"
#print(b[2:5])
########SLICE FROM THE START###############
#b = "hello there mr"
#print(b[:5])

########SLICE TO THE END###########
#b = "hello there mr"
#print(b[2:])

############NEGATIVE INDEXING################
#b = "hello there mr"
#print(b[-5:-2])

####MODIFY STRINGS########
#######Upper Case########
#a = "hello there mr"
#print(a.upper())

###########lower Case###########
#a = "HELLO THERE MR"
#print(a.lower())

#############REMOVE WHITESPACE###########
#a = "  hello there mr  "
#print(a.strip())

########REPLACE STRINGS##############
#a = "hello there mr lemon"
#print(a.replace("h", "j"))

#########SPLIT STRING#######
#a = "hello there"
#print(a.split(","))

########STRING CONCATINATION##############
#a = "hello"
#b = "there"
#c = a + " " + b
#print(c)

##########STRING FORMAT#############
#age = 54
#txt = "my name is FArouq, and I am " + str(age)

#print(txt)

###########
#quantity = 3
#temno = 545646
#price = 64.9
#myorder = "I want {} pieces of items{} for {} dollars."
#print(myorder.format(quantity, itemno, price))

#quantity = 3
#itemno = 345
#price = 60.89
#myorder ="i want to pay {2} dollars for {0} pieces of item {1}."
#print(myorder.format(quantity, itemno, price))

############ESCAPE CHARACTERS##########
#txt = "we are the so-called \"vikings\" from the North."
#print (txt)

##########BOOLEANS VALUES###################
#print(10>9)
#print(10==9)
#print
# (10<9)

#a = 200
#b = 33 

#if b > a:
#    print("b is greater than a")
#else:
#    print("b is not greater than a")

###########Evaluate Values And Variables##############
#print(bool("hello"))
#print(bool(15.0))

#x = "hello"
#y = 0

#print(bool(x))
#print(bool(y))

# print(bool("abc"))
# print(bool(123))
# print(bool(['apple', 'cherry', 'banana']))

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# class myclass():
#     def __len__(self):
#         return 0

# myobj = myclass()
# print(bool(myobj))

def myfunction():
    return True

if myfunction():
    print("yes")
else:
    print("no")        
# print(myfunction())    