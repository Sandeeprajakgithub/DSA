# magical methods in python 
# init
# str 
# eq

# len

# operator overloading 
# add
# contains


# __str__()

class Person:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
p1 = Person("Sandeep")
print(p1)

print("++++++++++2nd example+++++++++++++")

