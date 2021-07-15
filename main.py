from tkinter import *
import numpy as np

class Application:
    
    def __init__(self, master=None):
        
        #self.numero_sorteado = ""

        self.widget1 = Frame(master)
        self.widget1.pack(side = TOP)
        self.msg = Label(self.widget1, text = "Sorteio", background = "#FFF")
        self.msg["font"] = ("Verdana", "23", "italic", "bold")
        self.msg.pack()

        self.widget2 = Frame(master)
        self.widget2.place(x = 220, y = 250)
        #self.widget2.pack(ipadx = 20, ipady = 20, padx = 5, pady = 5 ,side = BOTTOM)
        self.sortear = Button(self.widget2)
        self.sortear["text"] = "Sortear"
        self.sortear["font"] = ("Calibri", "9")
        self.sortear["width"] = 10

        self.widget3 = Frame(master)
        self.widget3.place(x = 220, y = 150)

        self.resultado = Label(self.widget3, text = str(np.random.randint(0, 101)) , background = "#FFF" )
        self.sortear["command"] = resultado.
        self.sortear.pack (side = BOTTOM)
        self.resultado.pack()


    def sortear(self):
        self.numero_sorteado =  str(np.random.randint(0, 101))

app = Tk()
app.title("Sorteio")
app.geometry("500x300")
app.configure(background = "#FFF")

Application(app)
app.mainloop()