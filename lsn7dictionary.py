#DICTIONARY ---

#1/usr/bin/python
##########################
##########################
#student = {"name":"Kaka", "age":22 ,"gender":"male"}
#print(student["name"])
#print(student["age"])
#print(student["gender"])

#adding key value to a pair
#student["id.No"] = "5456463"
#student["Hobby"] = "reading"
#student["club"] = "Arsenal"

#print(student)

#student = {}
#student["favfood"] = "Biryani"
#student["Home-city"] = "Mombasa"
#student["fav-song"] = "Big_rich_town"
#student["colour"] = "Purple"
#student["DOB"] = 2000

#print("number \t square")
#print("======================")
#for number in range (0, 100):
#    print(number, "\t", number**2)

#print("#####")

#assignment print pyramid blocks

#pyramid of stars
for R in range(1,11):
    for C in range(11-R):
        print(" ", end = " ")
    for C in range(1,R):
        print("*", end = " ")
    for R in range(R, 0, -1):
        print("*", end = " ")

    print("\n")    

   #pyramid of numbers
for R in range(1,11):
    for C in range(11-R):
        print(" ", end = " ")
    for C in range(1,R):
        print(C, end = " ")
    for R in range(R, 0, -1):
        print(R, end = " ")

    print("\n")     