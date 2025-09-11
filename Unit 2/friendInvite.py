friends = []
height = []
numPeople = int(input("How many people are coming? "))
for i in range(numPeople):
    name = input(f"What is person {i+1}'s name? ")
    nameHeight = input(f"What is {name}'s height? ")
    friends.append(name)
    height.append(nameHeight)
print(friends)
print(height)
friendsHeights = {}
for i in range(len(friends)):
    friendsHeights[friends[i]]=height[i]
print(friendsHeights)