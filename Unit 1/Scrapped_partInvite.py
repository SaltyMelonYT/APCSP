list = []
person = int(input("How many people do you want to invite? "))
for each in range(person):
    name = input("Enter name of your friend: ")
    list.append(name)

list.sort()
print(f"Your list is {list}")

lastPerson = list[-1]
print(lastPerson)

removeFriend1 = int(input(f"Who do you not want to invite? Choose from the list, with {list[0]} being 0 and {lastPerson} being {person - 1}: "))
list.pop(removeFriend1)
removeFriend2 = int(input(f"Who do you not want to invite? Choose from the list, with {list[0]} being 0 and {lastPerson} being {person - 1}: "))
list.pop(removeFriend2)

list.sort()
print(list)