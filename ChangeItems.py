animals = {
    "Dog":"Bow Bow",
    "Cat":"Mewow",
    "Cow":"haa"
}
#change the value
x= animals["Cow"]="Maa"
print(animals)
#update the value using inbuild function
y=animals.update({"Cow":"Maaaa"})
print(animals)