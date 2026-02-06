def proto1():
    orders={
        0:{"name":"Walid","item":"Spicy Chicken Sandwich","cost":10.99},
        1:{"name":"Sagan","item":"Original","cost":7.99},
        2:{"name":"Jonathan","item":"Small Waffle Fry","cost":2.99}
    }

    temp=0
    total=0
    for i in range(len(orders)):
        print(orders[i]["name"])
        temp=orders[i]["cost"]
        total+=temp

    print(total)
        
def proto2():
    menu={"Spicy Chicken Sandwich":7.99,
          "Original Chicken Sandwich":5.99,
          "Spicy Chicken Sandwich Deluxe":10.99,
          "Small Waffle Fry":2.99,
          "Water":1.99}
    prevOrders={}
    orderNum=0
    
    while True:
        action=input("What to do ")
        if action=="order":
            name=input("What is your name? ")
            total=0
            order=[]
            ordering=True
            while ordering:
                for key,value in menu.items():
                    print(key,value)
                add=input("What would you like to order? ")
                if add in menu:
                    order.append(add)
                if add=="stop":
                    ordering=False
            
            for i in order:
                total+=menu[i]
            print(f"{name}'s total: ${total}")
            prevOrders[orderNum]={
                "name":name,
                "cost":total,
                "items":order
            }
            orderNum+=1
        if action=="prev":
            print(prevOrders)

proto2()