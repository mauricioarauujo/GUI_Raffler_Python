from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side = TOP)
        self.msg = Label(self.widget1, text = "Sorteio", background = "#FFF")
        self.msg["font"] = ("Verdana", "23", "italic", "bold")
        self.msg.pack()

        self.widget2 = Frame(master)
        self.widget2.pack(side = BOTTOM)
        self.widget2.place(x = 220, y = 250)
        self.sortear = Button(self.widget2)
        self.sortear["text"] = "Sortear"
        self.sortear["font"] = ("Calibri", "9")
        self.sortear["width"] = 10
        self.sortear["command"] = self.sortear
        self.sortear.pack (side = BOTTOM)


    def sortear(self):
        if self.msg["text"] == "A sortear":
            self.msg['text'] = "Sorteado"
        else:
            self.msg['text'] = "A sortear"

app = Tk()
app.title("Sorteio")
app.geometry("500x300")
app.configure(background = "#FFF")

Application(app)
app.mainloop()