# what is __init__() <------ constructor 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=age 

p1 = Person("Sandeep",25)
print(p1.name)
print(p1.age)   