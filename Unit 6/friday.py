prevOrder={}
daily=0
menu={
    1:{"item":"burger","cost":4.99},
    2:{"item":"Cheeseburger","cost":5.99},
    3:{"item":"Impossible Burger","cost":10.99},
    4:{"item":"Water","cost":1.99}
}

for i in range(2):
    customerName=input("Name: ")
    order=int(input("Order (Int only): "))
    prevOrder[i]={
        "cost":menu[order]["cost"],
        "name":customerName,
        "item":menu[order]["item"]
    }
    daily+=menu[order]["cost"]

print(prevOrder)
print(daily)