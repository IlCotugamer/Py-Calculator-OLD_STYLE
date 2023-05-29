import tkinter


# massimi caratteri che la entry visualizza correttamente <20
def pressione(num):
    global operazione
    global temp
    global c
    c += 1
    temp = operazione
    operazione = operazione + str(num)
    risultato.set(operazione)


def canc():
    global operazione
    global temp
    global c
    operazione = ""
    temp = ""
    c = 0
    risultato.set(operazione)


def risul():
    global operazione
    global temp
    global c
    try:
        tot = str(eval(operazione))
        risultato.set(tot)
        operazione = ""
        temp = ""
        c = 0
    except:
        risultato.set("Errore")
        operazione = ""
        temp = ""
        c = 0


def indietro():
    global operazione
    global c
    c -= 1
    operazione = operazione[0:c]
    risultato.set(operazione)


c = 0
temp = ""
f = tkinter.Tk()
f.title("Calcolatrice")
f.resizable(width=False, height=False)
f.iconbitmap("icona.ico")
f.configure(bg="#000000")

operazione = ""
risultato = tkinter.StringVar()

testo = tkinter.Entry(f, width=20, bd=5, state='readonly', textvariable=risultato)
testo.focus_set()

elimina = tkinter.Button(f, text="C", bg="#142e47", fg="#3c97e8", bd=1, width=10, height=5, command=canc)
cancella = tkinter.Button(f, text="<--", bg="#142e47", fg="#3c97e8", bd=1, width=10, height=5,
                          command=indietro)
p1 = tkinter.Button(f, text="1", width=10, height=5, command=lambda: pressione(1))
p2 = tkinter.Button(f, text="2", width=10, height=5, command=lambda: pressione(2))
p3 = tkinter.Button(f, text="3", width=10, height=5, command=lambda: pressione(3))
p4 = tkinter.Button(f, text="4", width=10, height=5, command=lambda: pressione(4))
p5 = tkinter.Button(f, text="5", width=10, height=5, command=lambda: pressione(5))
p6 = tkinter.Button(f, text="6", width=10, height=5, command=lambda: pressione(6))
p7 = tkinter.Button(f, text="7", width=10, height=5, command=lambda: pressione(7))
p8 = tkinter.Button(f, text="8", width=10, height=5, command=lambda: pressione(8))
p9 = tkinter.Button(f, text="9", width=10, height=5, command=lambda: pressione(9))
p0 = tkinter.Button(f, text="0", width=10, height=5, command=lambda: pressione(0))
perce = tkinter.Button(f, text="%", width=10, height=5, command=lambda: pressione("%"))
virgola = tkinter.Button(f, text=",", width=10, height=5, command=lambda: pressione("."))
meno = tkinter.Button(f, text="-", bg="#142e47", fg="#3c97e8", bd=1, width=10, height=5, command=lambda: pressione("-"))
piu = tkinter.Button(f, text="+", bg="#142e47", fg="#3c97e8", bd=1, width=10, height=5, command=lambda: pressione("+"))
per = tkinter.Button(f, text="X", bg="#142e47", fg="#3c97e8", bd=1, width=10, height=5, command=lambda: pressione("*"))
diviso = tkinter.Button(f, text="÷", bg="#142e47", fg="#3c97e8", bd=1, width=10, height=5,
                        command=lambda: pressione("/"))
uguale = tkinter.Button(f, text="=", bg="#142e47", fg="#3c97e8", activeforeground="#374d62", bd=1, width=10, height=11,
                        command=risul)

testo.grid(columnspan=4, ipadx=1, ipady=3, pady=15)
p1.grid(row=4, column=0, pady=3)
p2.grid(row=4, column=1, pady=3)
p3.grid(row=4, column=2, pady=3)
p4.grid(row=3, column=0, pady=3)
p5.grid(row=3, column=1, pady=3)
p6.grid(row=3, column=2, pady=3)
p7.grid(row=2, column=0, pady=3)
p8.grid(row=2, column=1, pady=3)
p9.grid(row=2, column=2, pady=3)
p0.grid(row=5, column=1, pady=3)
perce.grid(row=5, column=0, pady=3)
virgola.grid(row=5, column=2, pady=3)
meno.grid(row=3, column=3, pady=3)
piu.grid(row=2, column=3, pady=3)
diviso.grid(row=1, column=1, pady=3)
per.grid(row=1, column=2, pady=3)
uguale.grid(row=4, column=3, rowspan=2, pady=1, padx=3)
elimina.grid(row=1, pady=3)
cancella.grid(row=1, column=3, pady=3)

f.mainloop()
