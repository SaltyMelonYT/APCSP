list = []
friend1 = input("First friend to invite? "); list.append(friend1)
friend2 = input("Second friend to invite? "); list.append(friend2)
friend3 = input("Third friend to invite? "); list.append(friend3)
friend4 = input("Fourth friend to invite? "); list.append(friend4)

list.sort()
print(list)

removeFriend1 = int(input("Who to not invite? Pick a number between 0 and 3: "))
list.pop(removeFriend1)
print(list)
removeFriend2 = int(input("Who to not invite? Pick a number between 0 and 2: "))
list.pop(removeFriend2)
list.sort()
print(f"Your party invite list is {list}")