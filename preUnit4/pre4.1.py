prices = {
    "chips": 1.50,
    "cookie": 1.25,
    "juice": 2.00,
    "granola": 1.75,
    "fruit cup": 2.50
}

orders = [
    {"name": "Ava", "items": ["chips", "juice", "cookie"]},
    {"name": "Liam", "items": ["granola", "granola", "juice"]},
    {"name": "Mia", "items": ["fruit cup"]},
    {"name": "Noah", "items": ["chips", "chips", "cookie"]},
    {"name": "Emma", "items": ["juice", "fruit cup", "cookie"]}
]

moreThan5=[]
popularity={
    "chips": 0,
    "granola": 0,
    "fruit cup": 0,
    "juice": 0,
    "cookie": 0
}
count=0
while count!=5:
    person=orders[count]
    items=person["items"]
    for person in orders:
        for item in person["items"]:
            popularity[item]+=1

    orderedPrice=sum(prices[item] for item in items)
    if orderedPrice<=5:
        moreThan5.append(person["name"])
    if count==4:
        break
    count+=1

print(moreThan5)
print(popularity)

####################################################
# Second Code
####################################################

clubs = {
    "Science Club": ["Alice", "Bob", "Charlie", "Diana"],
    "Math Club": ["Bob", "Eve", "Frank", "Alice"],
    "Art Club": ["George", "Diana", "Alice", "Helen"],
    "Drama Club": ["Charlie", "Helen", "Ian"]
}

student_clubs = {}

for club, members in clubs.items():
    for member in members:
        if member not in student_clubs:
            student_clubs[member] = set()
        student_clubs[member].add(club)

maxClub = max(clubs.items(), key=lambda x: len(x[1]))
moreThan1 = [student for student, club_set in student_clubs.items() if len(club_set) > 1]

print("Students in more than one club:", moreThan1)
print(f"Club with the most members: {maxClub[0]} ({len(maxClub[1])} members)")

print("Student to clubs mapping:")
for student, club_set in student_clubs.items():
    print(f"{student}: {club_set}")