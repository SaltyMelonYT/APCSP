#Monday, Unsure what unit module, potentially 3.1
def deleteName(list, name):
    if name in list:
        list.remove(name)
        print(f"\n{name} removed!\n")
    else:
        print(f"\n{name} was not found in the list.\n")
        while True:
            name=input("Try again. ")
            if name in list:
                list.remove(name)
                print(f"\n{name} removed!\n")
                break

names=["Jonathan","Lucas","Robbie","Sagan","Walid","Denilson","Ben"]
print(names)
amount=int(input("How many names to remove? "))

if amount > len(names):
    while amount > len(names):
        print("There are not enough names to remove, please do a maximum of", len(names))
        amount=int(input("How many names to remove? "))
elif amount == 0:
    print("Can't remove 0 people from list! Quitting process...")

for i in range(amount):
    name=input(f"Name to remove? {i+1}/{amount} ")
    deleteName(names, name)
    print(names)