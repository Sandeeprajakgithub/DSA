# list []
# Tuple () 

# 1.  What are Tuples? 
# 2.  Tuple vs List 
# 3.  Features of Tuples (Ordered, Immutable, Heterogeneous) 
# 4.  Why Do We Use Tuples? 
# 5.  Creating Tuples 
# 6.  Different Ways to Create Tuples 
# 7.  Empty Tuple 
# 8.  Single-Element Tuple (Comma Importance) 
# 9.  Tuple with Mixed Data Types 
# 10.  Tuple Constructor (`tuple()` ) 
# 11.  Accessing Tuple Elements 
# 12.  Positive Indexing 
# 13.  Negative Indexing 
# 14.  Tuple Slicing 
# 15.  Reverse a Tuple 
# 16.  Tuple Unpacking 
# 17.  Tuple Unpacking with `*`  (Asterisk) 
# 18.  Tuple Concatenation (`+` ) 
# 19.  Tuple Repetition (`*` )

# how to make a tuple 
ls = ["ram",4,2]
print(type(ls))

tp = ("ram",4,'o+')
print(tp)
print(type(tp))

print("+++++++++++++++++++++++++++++")
# second way - create a tuple using list 
tp1 = tuple(ls)
print(tp1)


print("++++++++++++++++++++++++++++++++++")
tp2 = tuple("Ram")
print(tp2)

# tp3 = tuple("ram","sita")
# How to create tuple using mixed data type 

tup3 = ("ram","sita","lakshman","mohan",1.1,2.5)
print(tup3)

# Basic operation on tuple 
print("++++++++++++++++++++++++++++")
tup4 = tuple(["mohan","Sohan","Rohan"])
print(tup4)
print(tup4[0])
print(tup4[1])
print(tup4[2])

print("++++++++++++++++++++++++++++++++")
# SandeepBhi
# 0123456789
tup5 = tuple("SandeepBhi")
print(tup5)
print(tup5[0])

# print(tup5[start index:end index]) -->start index will come in result and end index will not come in result 
print("++++")
print(tup5[1:4])
print(tup5[2:6])

# print(tup5[start index:end index:step]) 


print(tup5[2:6:2])

#reverse the tuple in sigle line
print(tup5[::-1])
print(tup5[::3])

print("+++++++++++++++++++++++++++++++++++++")
print(tup5[::3])

print("**************************************")

# Concatination of tuples 
tp1 = tuple(["mohan","Sohan","Rohan"])
tp2 = (1,2,5,3,4)
print("&&&&&&&")
print(tp2)
tp3 = tp1+tp2
print(tp3)

# how to slice a type 
tps = ("SandeepCloudSreAdda")
print(tps)
tp_1 = tps[1:]
print(tp_1)
print(tp_1[::-1])

# How to delete a tuple 
tpd = tuple(["mohan","Sohan","Rohan"])
print("*********************")
print(tpd)
# del tpd
# print(tpd)


print("**********************")

# How to unpack a tuple 
tpu = tuple(["mohan","Sohan","Rohan","Rajat"])
print(tpu)
a,b,*c = tpu
print(a)
print(b)
print(c)


# insert 
# append
# pop

tp = (1,3)*10
print(tp)

