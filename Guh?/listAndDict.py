# MAKING A LIST
pcParts=['CPU','GPU','RAM']
# print(pcParts)
# ACCESS ELEMENTS OF THE LIST
# print(pcParts[0])
pcPartsDict=[
    {"name": "GPU", "price": 1500},
    {"name": "CPU", "price": 300},
    {"name": "RAM", "price": 2500}
]

for i in range(len(pcPartsDict)):
    print(f"Item {i+1} is {pcPartsDict[i]["name"]} and it costs ${pcPartsDict[i]["price"]}")

