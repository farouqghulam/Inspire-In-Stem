# #check if a number is palindrome

# number = int(input("Enter a number to check if it's palindrome \n"))
# take = number
# reverse = 0

# while (number > 0):
#     digit = number% 10
#     reverse = reverse * 10 + digit
#     number = number // 10
# print ("the reverse number is:",reverse)    
# if take == reverse:
#     print("the number is palindrome")
# else:
#     print("the number is not a palindrome")    



#check if a number is palindrome

sentence = str(input("Enter a sentence to check if it's palindrome \n"))
take = sentence
reverse = 0

while (sentence > 0):
    word = sentence % 10
    reverse = reverse * 10 + word
    number = number // 10
print ("the reverse sentence is:",reverse)    
if take == reverse:
    print("the sentence is palindrome")
else:
    print("the sentence is not a palindrome")        