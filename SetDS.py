# Unchangable but can remove and add new items
# Sets are unordered 
# Sets do not allow duplicates 


# How to create a set in python 
s = {"A","B","C"}
print(s)

# 2nd method 
# using constructor 
sc = set(("A","B","D"))
print(sc)

# Set dont allow duplicates 
sd = {"A","B","C","A"}
print(sd)

# true == 1
# false == 0

sd = {"A","B","C","A",True, 1}
print(sd)

sd = {"A","B","C","A",False, 0}
print(sd)

# what types of data can be stored in a set data structure 
sds = {"string","sting1","string2"}
sds1 = {1,3,3,4,5,5,6}
sds2 = {True, False, False, 0, 1}

print(sds)
print(sds1)
print(type(sds2))

sm = {"Ram",10,"Prakash","MP",145.5}
print(sm)


# Traversal 
thisset = set(("AK","ChaCha","bothchutiya"))
print(thisset)

# print(thisset[0])
# in - "weather the value exists in a set or not"
# or else use forloop 

# for loop 
for value in thisset:
    print(value)

# in - how it works 
if "bothchutiya" in thisset:
    print("sach mein chutiya h")

if "GoodPeople" not in thisset:
    print("No acchaii in dur dur taak- proved by system")

# How to add items inside a set 
thisset = set(("A","B","C")) 
thisset.add("D")
print(thisset)

# update - updates one set items into another set, update the original set 
thisset = set(("A","B","C")) 
thisset1 = set(("AK","ChaCha","bothchutiya","A"))

thisset.update(thisset1)
print(thisset)

# How to remove items from a set 
thisset = {"apple", "banana", "cherry"}
# thisset.remove("apple")
# thisset.remove("appl")

# method - discard 
print(thisset.discard("appl"))
print(thisset)

# What is the difference bw remove and discard method in set  
# remove - It throws the error if the item doesn't exist in a set
# discard - It doesnt throw the error if the item doesn't exits

# pop method 
popedItem = thisset.pop()
print("Pop Methods")
print(popedItem)
print(thisset)

# how does clear method words 
thisset3 = {"apple", "banana", "cherry"}
print("Explaining clear method")
print(thisset3)
thisset3.clear()
print(thisset3)

# how does del keyword works in python 
thisset4 = {"apple", "banana", "cherry","BBBBBBBBBBBBBBBBBBBBB"}
print("Explaining del keyword")
# print(thisset4)
# del thisset4
# print(thisset4)


# Union, Intersection, |, &

thisset = {"apple", "banana", "cherry"}
thisset1 = {"apple", "kela", "papaya"}

thisset3 = thisset.union(thisset1)
print(thisset3)

thisset5 = thisset | thisset1
print(thisset5)

# Iterview question 
thisset = {"apple", "banana", "cherry"}
ls = ["apple", "kela", "papaya"]

print("difference")
thisset3 = thisset.union(ls)
print(thisset3)

# thisset5 = thisset | ls
# print(thisset5)

# How to join multiple sets in Python 
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"ram", "Sita"}
set4 = {"apple","bananana","cherry"}

myset = set1.union(set2,set3,set4)
print(myset)

# Intersection - &
set1 = {"a","b","c"}
set2 = [1,2,"a"]
set3 = {"ram", "a"}
set4 = {"a","bananana","cherry"}

newinterset = set1.intersection(set2,set3,set4)
print(newinterset)

# Intersection - &
set1 = {"a","b","c"}
set2 = [1,2,"a"]
set3 = {"ram", "a"}
set4 = {"a","bananana","cherry"}

newinterset = set1 & set2
print(newinterset)