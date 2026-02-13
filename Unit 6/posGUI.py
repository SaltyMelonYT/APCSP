from tkinter import *
from tkinter import ttk

class POS():
    def __init__(self):
        self.root=Tk()
        self.frm = ttk.Frame(self.root, padding=20)
        self.frm.grid()
        self.root.geometry("500x500")
        self.order=[]
        self.root.title("POS System")
        self.prevOrders={}
        self.cart=''
        self.cart_text=StringVar()
        self.cart_text.set("No Items Yet")
        self.subtotal=0
        self.index=0
        self.prevList=''
        self.invList_text=StringVar()
        self.invList_text.set("")
        self.prevList_text=StringVar()
        self.prevList_text.set("")
        self.subtotal_text=StringVar()
        self.subtotal_text.set("Subtotal: $0.00")
        self.food={
            1:{"item":"Burger","cost":3.99},
            2:{"item":"Cheeseburger","cost":4.99}
        }
        self.drinks={
            1:{"item":"Water","cost":1.99},
            2:{"item":"Fountain Drink","cost":3.99}
        }
        self.inventory={
            "Burger":243,
            "Cheeseburger":319,
            "Water":1023,
            "Fountain Drink":732
        }
        self.mainMenu()
        self.root.mainloop()

    def mainMenu(self):
        for widget in self.frm.winfo_children():
            widget.destroy()
        ttk.Label(self.frm, text="test").grid(column=0, row=0)
        ttk.Label(self.frm, textvariable=self.prevList_text).grid(column=1, row=3, sticky=W)
        ttk.Label(self.frm, textvariable=self.invList_text).grid(column=1, row=4, sticky=W)
        ttk.Button(self.frm, text="Begin Ordering", command=self.orderScreen, width=20).grid(column=0, row=0,sticky=N)
        ttk.Button(self.frm, text="Previous Orders", command=self.pastOrders, width=20).grid(column=0, row=1,sticky=N)
        ttk.Button(self.frm, text="Inventory", command=self.invCheck, width=20).grid(column=0, row=2,sticky=N)

    def invCheck(self):
        invList=''
        for key,value in self.inventory.items():
            invList+=f'{key}: {value}\n'
        self.invList_text.set(invList)
        self.cart_text.set("")

    def pastOrders(self):
        self.prevList=''
        for key,value in self.prevOrders.items():
            self.prevList+=f"{key}: Cost: {value["totalCost"]}, Ordered Items: {value["orderedItems"]}\n"
        self.prevList_text.set(self.prevList)
        self.cart_text.set("")
    
    def orderScreen(self):
        self.order=[]
        self.subtotal=0
        for widget in self.frm.winfo_children():
            widget.destroy()
        ttk.Label(self.frm, textvariable=self.subtotal_text).grid(column=2,row=0)
        ttk.Label(self.frm, textvariable=self.cart_text).grid(column=2, row=4, rowspan=10)
        # Food orders :p
        ttk.Button(self.frm, text="Burger, $3.99", command=lambda: self.addToOrder(self.food,1), width=20).grid(column=0, row=0)
        ttk.Button(self.frm, text="Cheeseburger, $4.99", command=lambda: self.addToOrder(self.food,2),width=20).grid(column=0, row=1)
        # Drink orders :P
        ttk.Button(self.frm, text="Water, $1.99", command=lambda: self.addToOrder(self.drinks,1), width=20).grid(column=1, row=0)
        ttk.Button(self.frm, text="Fountain Drink, 3.99", command=lambda: self.addToOrder(self.drinks,2),width=20).grid(column=1, row=1)


        ttk.Button(self.frm, text="Place Order", command=self.finishOrder, width=42).grid(column=0,row=2,columnspan=2)
        ttk.Button(self.frm, text="Go Back", command=self.mainMenu, width=20).grid(column=0, row=3)

    def addToOrder(self, menuType, foodItem):
        self.order.append(menuType[foodItem]["item"])
        self.subtotal+=menuType[foodItem]["cost"]
        self.subtotal_text.set(f"Subtotal: {round(self.subtotal, 2)}")
        self.cartList()
    
    def cartList(self):
        self.cart_text.set("")
        self.cart=""
        self.order.sort()
        for item in self.order:
            self.cart+=f"{item}\n"
            self.cart_text.set(self.cart)
        self.invList_text.set("")

    def finishOrder(self):
        orderDict={}
        if self.order:
            for i in self.order:
                if i not in orderDict:
                    orderDict[i]=1
                else:
                    orderDict[i]+=1
            self.prevOrders[self.index]={
                "totalCost":round(self.subtotal,2),
                "orderedItems":orderDict
            }
            self.order=[]
            self.cart_text.set("No Items Yet")
            self.subtotal_text.set("Subtotal: $0.00")
            self.subtotal=0
            self.index+=1
            for key,value in orderDict.items():
                self.inventory[key]-=value
            self.mainMenu()
pos=POS()