class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age=age 

p1 = Animal("Lion",25)
print(p1.name)
print(p1.age) 

# Run a method implemented inside a class 


print("+++++++++++++++++++++++++++++++")

class Pan:
    def printObject(self):
        print(self.name)
        print(self.durability)
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability


p1 = Pan("Wall Pan", 100)
p1.printObject()