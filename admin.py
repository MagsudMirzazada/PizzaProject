from tkinter import *
import sqlite3

BACKGROUND = "white"

class admin(Tk):
    def __init__(self):
        super().__init__()
        
        #initializing admin screen
        self.title("Admin")
        self.geometry("300x300+600+250")
        self.config(bg=BACKGROUND)

        self.greeting = Label(self, text="Hi Admin", padx=10, pady=10).pack(side=TOP)
        #Buttons
        self.addPizzaTypeButton = Button(self,text = "Add new pizza", command = self.addPizza, padx=10, pady=10).pack(side=BOTTOM)
        self.addExtentionButton = Button(self,text = "Add new extention", command = self.addExtention, padx=10, pady=10).pack(side=BOTTOM)
        

    def addPizza(self):
        addPizzaScreen = Toplevel(self)
        addPizzaScreen.title("Add New Pizza")
        addPizzaScreen.geometry("+800+400")

        nameLabel = Label(addPizzaScreen,text = "Pizza name:").grid(row=0, column=0)
        priceLabel = Label(addPizzaScreen,text = "Pizza price:").grid(row=1, column=0)
        ingredientsLabel = Label(addPizzaScreen, text = "Ingredients").grid(row=2, column=0)

        nameEntry = Entry(addPizzaScreen)
        priceEntry = Entry(addPizzaScreen)
        ingredientsEntry = Entry(addPizzaScreen)
        nameEntry.grid(row=0, column=1)
        priceEntry.grid(row=1, column=1)
        ingredientsEntry.grid(row=2, column=1)

        def addPizzaType():
            pizza_type = nameEntry.get()
            pizza_price = priceEntry.get()
            ingredients = ingredientsEntry.get()

            f = sqlite3.connect('pizza.db')
            c = f.cursor()
            c.execute("INSERT INTO pizzas VALUES (?,?,?)",(pizza_type, pizza_price, ingredients))
            f.commit()
            f.close()
            
            addPizzaScreen.destroy()

        addButton = Button(addPizzaScreen,text = "Add",command = addPizzaType).grid(row=3)
    
    def addExtention(self):
        addExtentionScreen = Toplevel(self)
        addExtentionScreen.title("Add new extension")
        addExtentionScreen.geometry("+800+400")

        nameLabel = Label(addExtentionScreen,text = "Extension name:").grid(row = 0,column = 0)
        priceLabel = Label(addExtentionScreen,text = "Extension price:").grid(row = 1,column = 0)

        nameEntry = Entry(addExtentionScreen)
        priceEntry = Entry(addExtentionScreen)
        nameEntry.grid(row = 0,column = 1)
        priceEntry.grid(row = 1,column = 1)

        def addNewExtention():
            name = nameEntry.get()
            price = priceEntry.get()

            f = sqlite3.connect('extensions.db')
            c = f.cursor()
            c.execute("INSERT INTO extentions VALUES (?,?)",(name, price))
            f.commit()
            f.close()
            addExtentionScreen.destroy()

        addExtentionButton = Button(addExtentionScreen,text = "Add",command = addNewExtention).grid(row=2)