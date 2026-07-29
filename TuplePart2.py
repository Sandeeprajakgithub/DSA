# 1. Membership Operators (`in` , `not in` )
# 2.  Iterating Through Tuples 
# 3.  Built-in Functions (`len()` , `min()` , `max()` , `sum()` ) 
# 4.  Useful Tuple Methods (`count()` , `index()` ) 
# 5.  Nested Tuples 
# 6.  Mutable Objects Inside Immutable Tuples 
# 7.  Packing vs Unpacking 
# 8.  Deleting a Tuple (`del` ) 
# 9.  Common Errors in Tuples 
# 10.  Tuple Interview Questions 
# 11.  Real-World Use Cases of Tuples 
# 12.  Coding Practice Problems 
# 13.  Summary & Key Takeaways 

# 1. Membership Operators (`in` , `not in` )

# ()
# tuple()

tp = ("apple","mango","bananan")
print(tp)
print("apple" in tp)
print("apple" not in tp)

# 2.  Iterating Through Tuples

# Using for loop
print("+++++++++++++++++++++++++++++++++")
fruits = ("apple","mango","bananan")

for fruit in fruits:
    print(fruit)

# Using indexes 

print(len(fruits))

print(range(len(fruits)))

for i in range(len(fruits)):
    print(i,fruits[i])

# 3.  Built-in Functions (`len()` , `min()` , `max()` , `sum()` ) 
print("+++++++++++++++++++++++++++++++++++++++++++")

print("len",len(fruits))
print("min", min(fruits))
print("max",max(fruits))
# print("sum",sum(fruits))

# 4.  Useful Tuple Methods (`count()` , `index()` ) 
t = (1,2,2,3,4,5,6)
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print(t)
print(t.count(2))

# index - search by value
t = ("ram","sita","lakshman","hanuman")
print("index of lakshman", t.index("lakshman"))

# 5.  Nested Tuples 
nestTup = (((1,2,3,4),(5,6,7)),(8,9,10,11))
print(nestTup)

print("+++++++++++++++++++++++++++")
for tup in nestTup:
    for singletup in tup:
        print(singletup)

# 6.  Mutable Objects Inside Immutable Tuples 
tp = ("abc","def","ghi","jkl")
print("+++++++++++++++++++++++++++++++____________")

print(tp)
tp1 = (1,2,3,tp,4,5)
# tp1.append(60)
# print(tp1)

print("++++++++++++++")
ls = ["abc","def","ghi","jkl"]
print("+++++++++++++++++++++++++++++++____________")
tp = (1,2,3,ls,4,5) #immutable object <<-- mutable object 
print(tp)
tp[3].append(50)
print(tp)

#comman errors 
# tp [1] = "ram"

# Questions - swapping using variable

a = 10
b = 20 
print("before swap a, b -",a,b)
# c = a
# a = b 
# b = c
# print("after swap a, b",a,b)

# without variable 

a,b = b,a
print("a - ",a)
print("b -",b)
