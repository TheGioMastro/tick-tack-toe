#import
import tkinter as tk
import random
from tkinter import messagebox
#assegnamento variabilik
a0=""
a1=""
a2=""
b0=""
b1=""
b2=""
c0=""
c1=""
c2=""
volte=0
lista=["","","","","","","","",""]
#Masterclass
class Finestra(tk.Frame):
    #costruttrice finestra Master
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title("Tris by Giorgio Mastrogiovanni")
        self.master.geometry("400x400")
        self.master.resizable(0,0)
        self.master.columnconfigure(0, minsize=0)
        self.master.rowconfigure([0, 1], minsize=0)
        self.grid()
        self.master.configure(bg="#9effdc")
        self.crea_widgets()
    
    def crea_widgets(self):
        #funz vinci o perdi? mah.. perdi!
        #Controllo pedina utente "X"
        def giudice():
            giudica=0
            #1
            if lista[0]=="X":
                if lista[1]=="X":
                    if lista[2]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #2
            if lista[3]=="X":
                if lista[4]=="X":
                    if lista[5]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #3
            if lista[6]=="X":
                if lista[7]=="X":
                    if lista[8]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #4
            if lista[0]=="X":
                if lista[3]=="X":
                    if lista[6]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #5
            if lista[1]=="X":
                if lista[4]=="X":
                    if lista[7]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #6
            if lista[2]=="X":
                if lista[5]=="X":
                    if lista[8]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #7
            if lista[0]=="X":
                if lista[4]=="X":
                    if lista[8]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #8
            if lista[2]=="X":
                if lista[4]=="X":
                    if lista[6]=="X":
                        giudica=1
                        risp=messagebox.askquestion("Vittoria!!!",
                                                    "Beh... hai vinto!! contratulazioni!, vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            

                
            return giudica

        #giudice per bot "O"
        def giudicebot():
            
            #1
            if lista[0]=="O":
                if lista[1]=="O":
                    if lista[2]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #2
            if lista[3]=="O":
                if lista[4]=="O":
                    if lista[5]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #3
            if lista[6]=="O":
                if lista[7]=="O":
                    if lista[8]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #4
            if lista[0]=="O":
                if lista[3]=="O":
                    if lista[6]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #5
            if lista[1]=="O":
                if lista[4]=="O":
                    if lista[7]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #6
            if lista[2]=="O":
                if lista[5]=="O":
                    if lista[8]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #7
            if lista[0]=="O":
                if lista[4]=="O":
                    if lista[8]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            #8
            if lista[2]=="O":
                if lista[4]=="O":
                    if lista[6]=="O":
                       
                        risp=messagebox.askquestion("Hai perso",
                                                    "Beh... hai perso..., vui fare un'altra partita?")
                        if risp=="yes":
                            #La fine ricomincia
                            ricomincia()
            

                

        #funz ricomincia
        def ricomincia():
            #La fine ricomincia

            try:
                self.lblExample1.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample2.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample3.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample4.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample5.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample6.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample7.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample8.grid_forget()
            except AttributeError:
                pass
            try:
                self.lblExample9.grid_forget()
            except AttributeError:
                pass

            lista[0]=""
            a0=""
            lista[1]=""
            a1=""
            lista[2]=""
            a2=""
            lista[3]=""
            b0=""
            lista[4]=""
            b1=""
            lista[5]=""
            b2=""
            lista[6]=""
            c0=""
            lista[7]=""
            c1=""
            lista[8]=""
            c2=""
            
                    
            self.chk1.grid(row = 4, column = 0, sticky = "en")
            self.chk2.grid(row = 4, column = 1, sticky = "wn")
            self.chk3.grid(row = 4, column = 2, sticky = "wn")
            self.chk4.grid(row = 5, column = 0, sticky = "en")
            self.chk5.grid(row = 5, column = 1, sticky = "wn")
            self.chk6.grid(row = 5, column = 2, sticky = "wn")
            self.chk7.grid(row = 6, column = 0, sticky = "en")
            self.chk8.grid(row = 6, column = 1, sticky = "wn")
            self.chk9.grid(row = 6, column = 2, sticky = "wn")

        #funz cambio bottoni utente
        def xa0():
            a0="X"
            #1
            lista[0]="X"
            self.lblExample1= tk.Label( text = a0,bg="#9effdc",font="elephant")
            self.lblExample1.grid(row=4,column=0,sticky="en")
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xa1():
            a1="X"
            #2
            lista[1]="X"
            self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
            self.lblExample2.grid(row=4,column=1)
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xa2():
            a2="X"
            #3
            lista[2]="X"
            self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
            self.lblExample3.grid(row=4,column=2)
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xb0():
            b0="X"
            #4
            lista[3]="X"
            self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
            self.lblExample4.grid(row=5,column=0,sticky="en")
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xb1():
            b1="X"
            #5
            lista[4]="X"
            self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
            self.lblExample5.grid(row=5,column=1)
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xb2():
            b2="X"
            #6
            lista[5]="X"
            self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
            self.lblExample6.grid(row=5,column=2)
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xc0():
            c0="X"
            #7
            lista[6]="X"
            self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
            self.lblExample7.grid(row=6,column=0,sticky="en")
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xc1():
            c1="X"
            #8
            lista[7]="X"
            self.lblExample8 = tk.Label( text = c1,bg="#9effdc",font="elephant")
            self.lblExample8.grid(row=6,column=1)
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        def xc2():
            c2="X"
            #9
            lista[8]="X"
            self.lblExample9 = tk.Label( text = c2,bg="#9effdc",font="elephant")
            self.lblExample9.grid(row=6,column=2)
            giudica=giudice()
            if giudica==0:
                #numeri a caso e bot
                import random
                if "" in lista:
                    nrandom=random.randint(1,9)
                    while lista[nrandom-1]!="":
                        nrandom=random.randint(1,9)
                else:
                    giudice()
                    nrandom=0
                    risp=messagebox.askquestion("Question?",
                                        "Vui fare un'altra partita?")
                    if risp=="yes":
                        #La fine ricomincia
                        ricomincia()

                if nrandom==0:
                    giudice()
                    pass
                if nrandom==1:
                    lista[0]="O"
                    a0="O"
                    self.chk1.grid_forget()
                    self.lblExample1 = tk.Label( text = a0,bg="#9effdc",font="elephant")
                    self.lblExample1.grid(row=4,column=0,sticky="en")
                elif nrandom==2:
                    lista[1]="O"
                    a1="O"
                    self.chk2.grid_forget()
                    self.lblExample2 = tk.Label( text = a1,bg="#9effdc",font="elephant")
                    self.lblExample2.grid(row=4,column=1)
                elif nrandom==3:
                    lista[2]="O"
                    a2="O"
                    self.chk3.grid_forget()
                    self.lblExample3 = tk.Label( text = a2,bg="#9effdc",font="elephant")
                    self.lblExample3.grid(row=4,column=2)
                elif nrandom==4:
                    lista[3]="O"
                    b0="O"
                    self.chk4.grid_forget()
                    self.lblExample4 = tk.Label( text = b0,bg="#9effdc",font="elephant")
                    self.lblExample4.grid(row=5,column=0,sticky="en")
                elif nrandom==5:
                    lista[4]="O"
                    b1="O"
                    self.chk5.grid_forget()
                    self.lblExample5 = tk.Label( text = b1,bg="#9effdc",font="elephant")
                    self.lblExample5.grid(row=5,column=1)
                elif nrandom==6:
                    lista[5]="O"
                    b2="O"
                    self.chk6.grid_forget()
                    self.lblExample6 = tk.Label( text = b2,bg="#9effdc",font="elephant")
                    self.lblExample6.grid(row=5,column=2)
                elif nrandom==7:
                    lista[6]="O"
                    c0="O"
                    self.chk7.grid_forget()
                    self.lblExample7 = tk.Label( text = c0,bg="#9effdc",font="elephant")
                    self.lblExample7.grid(row=6,column=0,sticky="en")
                elif nrandom==8:
                    lista[7]="O"
                    c1="O"
                    self.chk8.grid_forget()
                    self.lblExample8= tk.Label( text = c1,bg="#9effdc",font="elephant")
                    self.lblExample8.grid(row=6,column=1)
                elif nrandom==9:
                    lista[8]="O"
                    c2="O"
                    self.chk9.grid_forget()
                    self.lblExample9= tk.Label( text = c2,bg="#9effdc",font="elephant")
                    self.lblExample9.grid(row=6,column=2)
                giudicebot()
                
        #oggetti della finestra        
        nomeimg = "trislogo.png"
        self.img = tk.PhotoImage(file = nomeimg)
        self.lblImg = tk.Label(self, image = self.img,bg="#9effdc")
        self.lblImg.grid(row = 0, column = 0)
        self.lblExample1 = tk.Label( text = " ",bg="#9effdc")
        self.lblExample1.grid(row=0,column=1)
        self.lblExample1 = tk.Label( text = " ",bg="#9effdc")
        self.lblExample1.grid(row=0,column=2)
        self.var1 = tk.IntVar(value = 0)
        self.chk1 = tk.Button(text = "",bg="#9effdc",width = 6,height=2,bd=3,
                                    #variable = self.var1,
                                   command=lambda:[self.chk1.grid_forget(),xa0()])
        self.chk1.grid(row = 4, column = 0, sticky = "en")
        self.var2 = tk.IntVar(value = 0)
        self.chk2 = tk.Button( text = "",bg="#9effdc",width = 6,height=2,bd=3,                                    #variable = self.var2,
                                    command=lambda:[self.chk2.grid_forget(),xa1()])
        self.chk2.grid(row = 4, column = 1, sticky = "wn")
        self.var3 = tk.IntVar(value = 0)
        self.chk3 = tk.Button( text = "",bg="#9effdc",width = 6,height=2,bd=3,                                    #variable = self.var3,
                                    command=lambda:[self.chk3.grid_forget(),xa2()])
        self.chk3.grid(row = 4, column = 2, sticky = "wn")
        self.var4 = tk.IntVar(value = 0)
        self.chk4 = tk.Button( text = "",bg="#9effdc",width = 6,height=2,bd=3,
                                    #variable = self.var4,
                                    command=lambda:[self.chk4.grid_forget(),xb0()])
        self.chk4.grid(row = 5, column = 0, sticky = "en")
        self.var5 = tk.IntVar(value = 0)
        self.chk5 = tk.Button( text = "",bg="#9effdc",width = 6,height=2, bd=3,                                   #variable = self.var5,
                                    command=lambda:[self.chk5.grid_forget(),xb1()])
        self.chk5.grid(row = 5, column = 1, sticky = "en")
        self.var6 = tk.IntVar(value = 0)
        self.chk6 = tk.Button( text = "",bg="#9effdc",width = 6,height=2, bd=3,                                   #variable = self.var6,
                                    command=lambda:[self.chk6.grid_forget(),xb2()])
        self.chk6.grid(row = 5, column = 2, sticky = "wn")
        self.var7 = tk.IntVar(value = 0)
        self.chk7 = tk.Button( text = "",bg="#9effdc",width = 6,height=2,bd=3,                                    #variable = self.var7,
                                    command=lambda:[self.chk7.grid_forget(),xc0()])
        self.chk7.grid(row = 6, column = 0, sticky = "en")
        self.var8 = tk.IntVar(value = 0)
        self.chk8 = tk.Button( text = "",bg="#9effdc",width = 6,height=2,bd=3,
                                    #variable = self.var8,
                                    command=lambda:[self.chk8.grid_forget(),xc1()])
        self.chk8.grid(row = 6, column = 1, sticky = "wn")
        self.var9 = tk.IntVar(value = 0)
        self.chk9 = tk.Button( text = "",bg="#9effdc",width = 6,height=2,bd=3,
                                    #variable = self.var9,
                                    command=lambda:[self.chk9.grid_forget(),xc2()])
        self.chk9.grid(row = 6, column = 2, sticky = "wn")
        
#funzione del main
def main():
    f = Finestra()
    f.mainloop()
    
#invocazione del Master main
main()
