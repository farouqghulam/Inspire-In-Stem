from math import factorial


# number = int(input ("enter the number"))
# factorial = -1
# if number < 0:
#     print("factorial of negative number doesnt exist")
# else :
#     for i in range (1,number+ 1):
#         factorial = factorial*i
#         print("factorial of ",number,"is",factorial)    


##########Arithmetic Progression#########
a = int(input("enter the first number"))
d = 2
n = 4

for i in range (1, n +1):
    n_term = a +(i - 1)*d
    print(n_term)

sum_n = (n_term/2) * (2*a +(n-1)*d)
print(sum_n)            

