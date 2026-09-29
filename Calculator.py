class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(calc.add(5,3))
print(calc.multiply(4,5))
print(calc.subtract(5,6))


# can we change the values of an object everytime using method 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday ! you are now {self.age}")

p1 = Person("Linus", 25)


# Important Method 
# Can we control the print statment for class specific 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"


p1 = Person("Ram",55)
print(p1)
