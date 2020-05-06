from tkinter import *
from Pizza import *
from PIL import ImageTk, Image
import sqlite3

BACKGROUND = "white"

class customer(Tk):
    def __init__(self, customer):
        super().__init__()
        self.currentCustomer = customer
        self.currentPizza = None
        self.result = None

        #initializing customer screen
        self.title("Customer")
        self.geometry("800x600+350+150")
        self.config(bg=BACKGROUND)

        self.greeting = Label(self, text="Hi " + self.currentCustomer, padx=10, pady=10).pack()

        #pictureframe
        pictureFrame = LabelFrame(self, bg=BACKGROUND, width=25, height=15)

        # image = Image.open("Barbeque.jpg")
        # render = ImageTk.PhotoImage(pictureFrame, image=image)

        # img = Label(pictureFrame, image=render)
        # img.image = render
        # img.place()

        pictureFrame.pack(fill='both', expand=True, padx=20, pady=20)

        #mainbuttons
        self.selectPizzaButton = Button(self, text="Select", width=10, padx=10, pady=10, command=self.selectPizzaOnClick).pack()
        self.extensionsButton = Button(self, text="Extensions", width=10, padx=10, pady=10, command=self.extensionsOnClick).pack()

        self.orderButton = Button(self, text="Order", width=7, pady=5, command=self.orderOnClick).pack(side=BOTTOM)

    

    def selectPizzaOnClick(self):
        pizzaScreen = Toplevel(self)
        pizzaScreen.title("Select your Pizza")
        pizzaScreen.geometry("+500+200")
        pizzaList = Listbox(pizzaScreen)

        #database
        db = sqlite3.connect("pizza.db")
        c = db.cursor()

        for i in (c.execute("SELECT pizza_type FROM pizzas")):
            pizzaList.insert(END,i[0])
        db.commit()

        #second select button
        def selectPizzaType():
            pizzaType = pizzaList.get(ANCHOR)
            c.execute("SELECT pizza_price FROM pizzas WHERE pizza_type=?",(pizzaType,))
            self.currentPizza = PizzaBuilder(pizzaType)#, c.fetchone()[0])
            pizzaScreen.destroy()
            db.close()

        selectButton = Button(pizzaScreen,text = "Select", command = selectPizzaType)
    
        pizzaList.pack()
        selectButton.pack()

    def extensionsOnClick(self):
        extensionScreen = Toplevel(self)
        extensionScreen.title("Extensions")
        extensionScreen.geometry("300x300+500+200")
        extensionsList = Listbox(extensionScreen, selectmod=MULTIPLE)

        #database
        db = sqlite3.connect("extensions.db")
        c = db.cursor()

        for i in (c.execute("SELECT name FROM extentions")):
            extensionsList.insert(END, i[0])
        db.commit()

        #second select button
        def selectExtensions():
            reslist = list()
            selections = extensionsList.curselection()

            for i in selections:
                reslist.append(extensionsList.get(i))

            for val in reslist:
                c.execute("SELECT name FROM extentions WHERE name=?", (val,))
                self.currentPizza.add_extention(val)#,c.fetchone()[0])

            db.close()
            extensionScreen.destroy()

        selectButton = Button(extensionScreen,text = "Select", command=selectExtensions)
        extensionsList.pack()
        selectButton.pack()


    def orderOnClick(self):
        if self.result != None:
            self.result.destroy()
        self.result = Label(self, text= "Pizza: " + self.currentPizza.get_status() + "\n" + "Price: " + str(self.currentPizza.get_price()))
        self.result.pack()