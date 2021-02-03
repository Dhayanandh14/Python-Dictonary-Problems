animals = {
    "Dog":"Bow Bow",
    "Cat":"Mewow",
}
#Accessing item using one key 

key = animals["Dog"]
print("Access using key so out put is: ",key)
print()
#Accessing items using keys (keyword)
key = animals.keys()
print("Access key using Keys keyword:",key)
print()

#Accessing items using values (keyword)
value = animals.values()
print("Access value using values keyword:",value)
print()
#Accessing all items using items (keyword)

item=animals.items()
print("This method using items keyword: ",item)

#check the value is there or not 
if "Dog" in animals: 
  print("Yes value is there in the dictonary")
else :
  print("No value is not there in the dictonary")

