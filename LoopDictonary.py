animals = {
    "Dog":"Bow Bow",
    "Cat":"Mewow",
    "Cow":"haa"
}
#This loop will print every keys
for i in animals:
    print(i)
#This loop will print all items
for i in animals.items():
    print(i)
#This loop will print all values
for i in animals:
    print(animals[i])
#This loop will print items keys values
for x in animals.keys():
  print(x)
for x in animals.values():
  print(x,end=" ")

