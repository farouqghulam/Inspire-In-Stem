#ASSIGNMENT 3
#-Write a program to withdraw ksh.25000 if account balance is btwn ksh.
# 100k to 200k.30% if account balance is btwn 500k and 1M.
# Above 1M deduct 15000


#gender = input("What is your gender. Male/Female?")
#print(" my gender is " + gender )

#age = input('how old are you')
#print("you are" +str(age) + " years old ")

#acc_bal = 0

#if (int(age) > 25) and (int(age) < 30):
#    acc_bal = acc_bal + 10000
#    print("confirmed you have recieved the amount")
#else:
##    print ("sorry no money for you")

#gender = input("What is your gender. Male/Female?")
#print(" my gender is " + gender )

#age = input('how old are you')
#print("you are" +str(age) + " years old ")


#if (int(acc_bal)>100000) and (int(acc_bal)<200000):
    #acc_bal = acc_bal - 25000
    #print()

 #if (int(acc_bal)>500000) and (int(acc_bal)<1000000)





acc_bal = input("enter account balance:")

if(int(acc_bal)>100000 and int(acc_bal),200000):
    acc_bal = acc_bal - 25000
    print("we have deducted ksh 25000")
elif (int(acc_bal)>500000 and int(acc_bal)<1000000):
    acc_bal = acc_bal-float(0.3*acc_bal)
    print("we havededucted 30%")
elif int(acc_bal) >1000000:
    acc_bal = acc_bal-15000
    print("we have deducted ksh 15000")

else :
    print("no deduction done")    
    

