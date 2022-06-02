class person:
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def sayHI(self):
       print('hello, my name is'  + str(self.name), 'and I am' + str(self.age) + 'years old')# concatination
person1 = person('Bob',19)
person1.sayHI()
person2 = person ("lemonadfes", 20)
person2.sayHI()
person3 = person("yvonne", 19)
person3.sayHI()