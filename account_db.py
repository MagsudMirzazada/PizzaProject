import sqlite3

class sql:
    def __init__(self):
        self.conn = sqlite3.connect('accounts.db')
        self.cursor = self.conn.cursor()
    
    def createTable(self):
        self.cursor.execute("""CREATE TABLE accounts (
                        Username text,
                        Password text
                        )""")

    def addNewAccount(self, username, password):
        self.cursor.execute("INSERT INTO accounts VALUES (:username, :password)", {'username': username, 'password': password})
        self.conn.commit()

    def findAccount(self, username, password):
        self.cursor.execute("SELECT * FROM accounts WHERE username=:username AND password=:password", {'username': username, 'password': password})
        return self.cursor.fetchall()

    def findAccountByName(self, username):
        self.cursor.execute("SELECT * FROM accounts WHERE username=:username", {'username': username})
        return self.cursor.fetchall()
    
    #def getUsername(self):

    def close_conn(self):
        return self.conn.close()



db = sql()
#db.createTable()
# #db.addNewAccount('admin', 'admin')
# print(db.findAccount('admin', 'admin'))
# for row in db.findAccountByName('a'):
#     print('var')

db.close_conn()