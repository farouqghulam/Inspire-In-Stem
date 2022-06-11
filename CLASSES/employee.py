class Employee:
    def __init__(self,name,age,salary,location,id):
       self.name = name
       self.age = age
       self.salary = salary
       self.location = location
       self.id = id
    
    def sayHI(self):
       print('hello, my name is'  + str(self.name), 'and I am' + str(self.age) + 'years old')
       print("I earn a salary of " + str(self.salary) + " my identity number is")
       print(str(self.id), + "  and i come from " + "location")
Employee1 = Employee('shagalabagala',40,4000000,'mombasa',65464)
Employee1.sayHI
