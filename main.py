from tkinter import *
import numpy as np

class Application:
    
    def __init__(self, master):
        
        #self.numero_sorteado = ""

        self.frame_titulo = Frame(master)
        self.frame_titulo.pack(side = TOP)
        self.msg = Label(self.frame_titulo, text = "Sorteio", background = "#FFF")
        self.msg["font"] = ("Verdana", "23", "italic", "bold")
        self.msg.pack()

        self.frame_minimo = Frame(master)
        self.frame_minimo.pack()

        self.frame_maximo = Frame(master)
        self.frame_maximo.pack()

        self.frame_resultado = Frame(master)
        self.frame_resultado.pack(padx = 50, pady = 50)

        self.frame_botao = Frame(master)
        self.frame_botao.pack()

        self.frame_observacao = Frame(master)
        self.frame_observacao.pack(side = "bottom")

        self.widget_minimo = Label(self.frame_minimo, text = "Valor mínimo: ",width = 12,font=('Verdana','14','bold'), background = "#FFF")
        self.widget_maximo = Label(self.frame_maximo, text = "Valor máximo: ", width = 12, font=('Verdana','14','bold'), background = "#FFF")

        self.entrada_valor_minimo = Entry(self.frame_minimo, width = 12, font = ("Verdana", "8", "italic", "bold"), background = "#FFF")
        self.entrada_valor_minimo.focus_force()
        self.entrada_valor_maximo = Entry(self.frame_maximo, width = 12, font = ("Verdana", "8", "italic", "bold"), background = "#FFF")
            
        self.botao_sorteio = Button(self.frame_botao, text = "Sortear", width =10, font = ("Calibri", "9"))
       
        self.observacao = Label(self.frame_observacao, text = "O range padrão ou para intervalos inválidos é [0,100]", font = ("Calibri", "8"))

        self.resultado = Label(self.frame_resultado, text = "   " , background = "black", foreground = "white")
        self.resultado["font"] = ("Calibri", "33", "bold")
        self.botao_sorteio.bind("<Button-1>", self.sortear)

        self.widget_minimo.pack(side = "left")
        self.widget_maximo.pack(side = "left")
        self.entrada_valor_minimo.pack()
        self.entrada_valor_maximo.pack()


        self.observacao.pack(pady= 5)
        self.botao_sorteio.pack(side = BOTTOM)
        self.resultado.pack()
        

    def sortear(self, event):
        try:
            MIN= int(self.entrada_valor_minimo.get())
            MAX= int(self.entrada_valor_maximo.get())
        except:
            MIN = 0
            MAX = 100
        self.resultado['text'] = str(np.random.randint(MIN, MAX + 1))


def main():
    sorteado = False
    app = Tk()
    app.title("Sorteio")
    app.geometry("500x400")
    app.configure(background = "#FFF")

    Application(app)
    app.mainloop()
    


if __name__ == "__main__":
    main()
