dict = {}

list = int(input("Number of people? "))
for int in range(list):
    key = input("Name? ")
    value = input("Height? ")
    dict[key]=value
print(dict)