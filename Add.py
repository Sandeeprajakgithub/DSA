class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __add__(self,person):
        return self.age - person.age
        # return self.name == person.name
p1 = Person("Sandeep",70)
p2 = Person("Ajay",50)

print("++++++++++2nd example+++++++++++++")
print(p1 + p2)


# print(p1.age + p2.age)