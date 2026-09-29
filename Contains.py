class Company:
    def __init__(self,employees):
        self.employees = employees

    def printEmp(self):
        print(self.employees)
    # def __add__(self,person):
    #     return self.age - person.age
        # return self.name == person.name
    def printLength(self):
        return len(self.employees)

    def __len__(self):
        return len(self.employees)

    def __contains__(self,name):
        return name in self.employees

    
c = Company(["Ram","mohan","sohan"])
# print(c)
c.printEmp()

print(len(c))
print("new examples......")

print("Rama" in c)
