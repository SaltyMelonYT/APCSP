dict={}
numPeople = int(input("How many people are coming? "))
for i in range(numPeople):
    name = input(f"What is person {i+1}'s name? ")
    nameHeight = input(f"What is {name}'s height? ")
    dict[name[i]]=name
    dict[f"height[i]"]=nameHeight
print(dict)