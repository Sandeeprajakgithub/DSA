# what is python dictionary 

# Mera name sandeep hasattr
# name:sandeep
# key : value 

# dictionary is a data structure in  python which is used to store key value pairs.

# Ordered
# No duplicates allowed 
# change 
# 
# 
# Section 1 
print("++++++++++++++Start of section 1++++++++++++++")
#how to make dictionary 
# Method 1
car = {
    "name":"Tata",
    "model":"v2",
    "year":2020
} 

print(car)

car1 = dict({"name":"Volvo","model":"v3","year":2017})
print(car1)
print("++++++++++++++End of section 1++++++++++++++")
#How to triverse in a dictionary 

print("++++++++++++++Start of section 2++++++++++++++")
print(car1["name"])
print(car1["model"])

# method - 2 get()
print(car1.get("name"))
print(car1.get("model"))
print(car1.get("year"))

# keys()
print(car1.keys())
print(type(car1.keys()))

x = car1.keys()
print(x)
for item in x:
    # print(item)
    print(car1[item])
print("+++++")

for i in car1.items():
    print(type(i))

# lets learn values method

for j in car1.values():
    print(j)

car1 = dict({"name":"Volvo","model":"v3","year":2017})
car1["name"] = "Nexon"
print(car1)

car1 = dict({"name":"Volvo","model":"v3","year":2017,"year":2019})

print(car1)
# How to get length of a dictionary 
print(len(car1))

# how many data types can we use in dict?


car = {
    "name":"Tata",
    "model":"v2",
    "year":2020,
    "feature":["ABS","automatic","good looks"]
} 

print(car)
print(len(car["feature"]))
print("print feature")
print(car["feature"][0])
print(car["feature"][1])
print(car["feature"][2])

print("How to check weather a key is part of a dict or not?")
if "break" in car.keys():
    print("Hn mil gya")
else:
    print("nhi mila")

if "model" in car.keys():
    print("Mil gya")

if "Tata" in car.values():
    print("Found the brand name")


if "model" in car:
    print("Mil gya")

# How to update dictionary using update keyword
print("car object before change"+" : ",car)

car.update({"name":"MG"})
print("car object after change : ", car)
print("++++++++++++++End of section 2++++++++++++++")


print("++++++++++++++Start of section 3++++++++++++++")
newDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before  -", newDict)
newDict["color"] = "Yellow"
print("After - ", newDict)


print("Method - 2")
newDict.update({"Tyre":"MRF"})
print(newDict)
print("++++++++++++++End of section 3++++++++++++++")
# Remove Items from the dictionary 

print("++++++++++++++Start of section 4++++++++++++++")
newRmDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(newRmDict)
# # pop(paramter)
 
# method 1 
# newRmDict.pop("brand")
# print(newRmDict)

# method 2
#popitem()
# 3.7 version applicaable

# newRmDict.popitem()
# print(newRmDict)

# method 3 
# del newRmDict["brand"]
# del newRmDict


# clear ()
print(newRmDict)
newRmDict.clear()
print(newRmDict)
print("++++++++++++++End of section 3++++++++++++++")
