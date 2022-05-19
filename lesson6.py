#learning about lists
from ast import For


motorcycle_owner = "mojo jojo"
plate_number = ['H1234' , 'Y1234' , 'S12134']
motorcycle = ['honda','Yamaha','Suzuki']
#print(motorcycle)
#accessing list files using index
#print motorcycle
#print(motorcycle)
#motorcycle[0] = 
#print(motorcycle)

#print("i love "+str(motorcycle[1]))

#motorcycle.append('zamzama')
#print(motorcycle)

#print(motorcycle)
#print(plate_number)

#print(str(motorcycle[0]) , str(plate_number[0]))
#print(str(motorcycle[1]) , str(plate_number[1]))
#print(str(motorcycle[2]) , str(plate_number[2]

#deleting an item from a list --del

#del motorcycle[2]
#print(motorcycle)

#del plate_number[2] deleting an item from a list
#print(plate_number)

popped_motorcycle = motorcycle.pop()
#print(motorcycle)
#Task print a statement : my name is mojo jojo and I own a motorcycle plate number

#print("my name is" ,str(motorcycle_owner) , "and I own motorcycle plate numbers" ,str(plate_number))

motorcycle.remove('honda')
#print(motorcycle)

#LOOPS
school = ['joy', 'hope', 'mercy', 'happy']
pupil =['mark', 'antony', 'zarina', 'patience']

# print(str(school[0]), str(pupil[0]))
# print(str(school[1]), str(pupil[1]))
# print(str(school[2]), str(pupil[2]))
# print(str(school[3]), str(pupil[3]))

# for schoolgetschool
# for pupilgetpupil

# print("I am (pupil[0]) and I school at (school[0])")
# print("I am (pupil[0]) and I school at (school[0])")
# print("I am (pupil[0]) and I school at (school[0])")
# print("I am (pupil[0]) and I school at (school[0])")

for pupil in pupil:
    print(f'hello I am pupil {pupil}')
   
for school in school:
    print(f'I go to school {school}')