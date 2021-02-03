animals = {
    "Dog":"Bow Bow",
    "Cat":"Mewow",
    "Cow":"haa"
}
#Pop the item using python in-built function
animals.pop("Cow")
print(animals)
#remove the last index using popitem function 
# if i did not give parameter pop function take last index value
animals.popitem()
print(animals)
#remove the item using Del keyword
del animals["Dog"]
print(animals)
#clear keywork clear all the items 
animals.clear()
print(animals)
