# magical methods in python 
# init
# str 
# eq
# len
# add
# contains


# __str__()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self,person):
        # return self.age == person.age
        return self.name == person.name
p1 = Person("Sandeep",30)
p2 = Person("Ajay",30)

print("++++++++++2nd example+++++++++++++")
print(p1 == p2)