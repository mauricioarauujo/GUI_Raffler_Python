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

        self.widget_botao = Frame(master)
             
        self.botao_sorteio = Button(self.widget_botao, text = "Sortear", width =10, font = ("Calibri", "9"))

        self.widget3 = Frame(master)
        

        self.resultado = Label(self.widget3, text = str(np.random.randint(0, 101)) , background = "black", foreground = "white")
        self.resultado["font"] = ("Calibri", "33", "bold")
        self.botao_sorteio.bind("<Button-1>", self.sortear)

        self.widget3.pack(padx = 75, pady = 75)
        self.botao_sorteio.pack(side = BOTTOM)
        self.widget_botao.pack()
        self.resultado.pack()
        

    def sortear(self, event):
        self.resultado['text'] = str(np.random.randint(0, 101))


def main():
    sorteado = False
    app = Tk()
    app.title("Sorteio")
    app.geometry("500x300")
    app.configure(background = "#FFF")

    Application(app)
    app.mainloop()
    


if __name__ == "__main__":
    main()
