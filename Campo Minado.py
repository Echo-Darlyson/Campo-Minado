import tkinter as tk
import random
from functools import partial
from time import sleep
import sys

janela = tk.Tk()
janela.title ("Campo Minado")

foto0 = tk.PhotoImage (file = "white.png")
fotorepo0 = foto0.subsample (4, 4)

foto1 = tk.PhotoImage (file = "bomba1.png")
fotorepo1 = foto1.subsample (34, 34)

foto2 = tk.PhotoImage (file = "bandeira.png")
fotorepo2 = foto2.subsample (16, 16)


def Mina(n):
    listabotão [n] ["image"] = fotorepo1
    perdeu = tk.Tk()
    perdeu.geometry("110x80")
    janela.withdraw()
    l1 = tk.Label(perdeu, text = "Game Over!", font = ("Arial Black", 10), fg = "Red").place(relx = .5, rely = .3, anchor = "center")
    l2 = tk.Button(perdeu, text = "OK :(", command = sys.exit, bg = "Red", fg = "White", font = ("Arial Black", 9), relief = "solid", activeforeground = "Red", activebackground = "White").place(relx = .5, rely = .7, anchor = "center")


def SemMina(p):
    print ("Aqui não tem mina! Continue!")
    listabotão [p] ["image"] = fotorepo2
 

i = -1    
    
lista = [Mina, SemMina, SemMina, SemMina]
listabotão = list ()

for coluna in range (5):
    for linha in range (5):
        i += 1
        b = tk.Button(janela, command = partial (random.choice (lista), i), image = fotorepo0)
        b.grid(column = coluna, row = linha)
        listabotão.append (b)
            
janela.mainloop()

# Made By D4rly$0nZ
# 13/08/2021 Sexta-Feira
