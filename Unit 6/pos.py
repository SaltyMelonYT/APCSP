class POS():
    def __init__(self):
        self.dailyEarnings=0
        self.orderNum=0
        self.food={
            1:{"item":"Spicy Chicken Sandwich","cost":6.99,"ingrediants":{"patties":1,"buns":2}},
            2:{'item':'Chicken Sandwich',"cost":6.99,"ingrediants":{"patties":1,"buns":2}}
        }
        self.drink={
            1:{"item":"Water","cost":1.99},
            2:{"item":"Fountain Drink","cost":2.99}
        }
        self.prevOrders={}
        self.actions={
            "order":self.ordering,
            "earnings":self.earnings,
            "prev":self.previousOrders,
            "inv":self.invCheck
        }

        self.inventory={
            "patties":472,
            "buns":472
        }

    def mainInterface(self):
        action=input("What would you like to do ")
        if action in self.actions:
            self.actions[action]()

    def invCheck(self):
        print(self.inventory)

    def previousOrders(self):
        for key,value in self.prevOrders.items():
            print(f"{key}: Name: {value["name"]}, Cost: {value["total"]}, Ordered Items: {value["items"]}")

    def earnings(self):
        print(round(self.dailyEarnings,2))

    def tax(self, total, trueValue=False):
        taxRate=0.04
        if trueValue:
            return round(total*taxRate,2)
        if not trueValue:
            return round(total+(total*taxRate), 2)

    def ordering(self):
        ordering=True
        ordList=[]
        total=0
        custName=input("Customers name: ")
        while ordering:
            print("1.) Food Menu\n2.) Drink Menu")
            choice=input("")
            try:
                choice=int(choice)
                if choice==1:
                    for key,value in self.food.items():
                        print(f'{key}, {value["item"]}, {value["cost"]}')
                    order=int(input())
                    ordList.append(self.food[order]["item"])
                    total+=self.food[order]["cost"]
            except ValueError:
                if choice=='stop':
                    for i in range(len(ordList)):
                        for key,value in self.food[i+1]["ingrediants"].items():
                            self.inventory[key]-=value
                    print(f"Subtotal: {total}")
                    print(f"Tax: {self.tax(total, True)}")
                    print(f"Total: {self.tax(total)}")
                    ordering=False
pos=POS()
while True:
    pos.mainInterface()