class Calculator:
    def add(self,a,b):
        return a + b
    def subs(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def dev(self,a,b):
        return a / b


c = Calculator()
print(c.add(10,20))
print(c.subs(10,20))
print(c.mul(10,20))
print(c.dev(10,20))