class POS():
    def __init__(self):
        self.dailyEarnings=0
        self.orderNum=0
        self.food={
            1:{"item":"Spicy Chicken Sandwich","cost":6.99},
            2:{'item':'Chicken Sandwich',"cost":6.99}
        }
        self.drink={
            1:{"item":"Water","cost":1.99},
            2:{"item":"Fountain Drink","cost":2.99}
        }
        self.prevOrders={}
        self.actions={
            "order":self.ordering,
            "earnings":self.earnings,
            "prev":self.previousOrders
        }

    def mainInterface(self):
        action=input("What would you like to do ")
        if action in self.actions:
            self.actions[action]()

    def previousOrders(self):
        for key,value in self.prevOrders.items():
            print(f"{key}: Name: {value["name"]}, Cost: {value["total"]}, Ordered Items: {value["items"]}")

    def earnings(self):
        print(self.dailyEarnings)

    def tax(self, total):
        taxRate=0.04
        return round(total+(total*taxRate), 2)

    def ordering(self):
        name=input("Customer Name: ")
        ordering=True
        total=0
        order=[]
        while ordering:
            for key,value in self.food.items():
                print(f'{key}.) {value["item"]}, ${value["cost"]}')
            add=input("What to add to cart? ")
            if add.lower()=='stop':
                ordering=False
                print(f"{name}'s total is ${self.tax(total)}")
                
            elif int(add) in self.food:
                order.append(self.food[int(add)]["item"])
                total+=self.food[int(add)]["cost"]
                print(self.tax(total))
        self.dailyEarnings+=self.tax(total)
        self.orderNum+=1
        self.prevOrders[self.orderNum]={
            "name":name,
            "total":self.tax(total),
            "items":order
            }
            
pos=POS()
while True:
    pos.mainInterface()