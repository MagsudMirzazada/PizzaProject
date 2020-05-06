from tkinter import *
from account_db import *
from customer import *
from admin import *

BACKGROUND = 'grey'

class login(Tk):
    def __init__(self):
        super().__init__()
        
        #initializing main screen
        self.title("Account")
        self.geometry("350x250+500+200")
        self.config(bg=BACKGROUND)

        #frame
        frame = LabelFrame(self, bg=BACKGROUND)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        frame.place(anchor='c', relx=0.5, rely=0.5)


        #instructions
        self.nameLabel = Label(frame, text="Username: ", font=("Calibri", 13), bg=BACKGROUND, fg="white", padx=5, pady=5, justify=CENTER).grid(row=2, column=1)
        self.pwordLabel = Label(frame, text="Password: ", font=("Calibri", 13), bg=BACKGROUND, padx=5, fg="white", pady=5, justify=CENTER).grid(row=3, column=1)

        self.nameEntry = Entry(frame, width="20")
        self.nameEntry.grid(row=2, column=2)

        self.pwordEntry = Entry(frame, width="20", show="*")
        self.pwordEntry.grid(row=3, column=2)

        #Buttons
        self.loginButton = Button(frame, text="Login", width="15", command=self.loginOnClick).grid(row=4, column=2)
        self.signupButton = Button(frame, text="Sign Up", width="15", command=self.signupOnClick).grid(row=5, column=2)
        #command=self.loginOnClick

        #mainloop
        self.mainloop()

    def loginOnClick(self):
        username = self.nameEntry.get()
        password = self.pwordEntry.get()
            
        if (username == "admin" and password == "admin"):
            self.destroy()
            newScreen = admin()
            return

        flag = False
        dataBase = sql()
        for row in dataBase.findAccount(username, password):
            self.destroy()
            newScreen = customer(username)
            flag = True
        
        # if (flag):
        #     resultLabel = Label(self, text="Login Succesfully", font=("Calibri", 11), bg="skyblue", fg="red", padx=5, pady=5).grid(row=6, column=2)

        if (flag == False):
            resultLabel = Label(self, text="Invalid username or password", font=("Calibri", 11), bg=BACKGROUND, fg="red", padx=5, pady=5).grid(row=6, column=2)

    def signupOnClick(self):
        username = self.nameEntry.get()
        password = self.pwordEntry.get()

        dataBase = sql()
        for row in dataBase.findAccountByName(username):
            resultLabel = Label(self, text="This account has been created", font=("Calibri", 11), bg=BACKGROUND, fg="red", padx=5, pady=5).grid(row=6, column=2)
            return
        
        dataBase.addNewAccount(username, password)
        #resultLabel = Label(self, text="Succesfully signed up", font=("Calibri", 11), bg="skyblue", fg="red", padx=5, pady=5).grid(row=6, column=2)
        self.loginOnClick()