# patient = "John"
# patient = "20 years old"
# print(patient)

# name = input("What is your name? ")
# print("hello" , name)

# birth_year = input("enter you birth year:")
# age = 2022 - int(birth_year)
# print (age)

# print (10.1 + 20)

# first = float(input("first: "))
# second = float(input("second: "))
# sum = (first )+ (second)


#The program below shall count as long as the numbers are less than 9
# count = 0
# while (count<9):
#     print("the count is:", count)
#     # count = count + 1


import random
print("Welcome to our password generator")
character = str("Saikayan047")
num_passwords = int(input("How many passwords"))
len_password = int(input("How long would you like your password to be?"))
print("Here are your passwords")
for password in range(num_passwords):
    password = ''
    for c in range(len_password):
        password += random.choice(character)
    print(password)