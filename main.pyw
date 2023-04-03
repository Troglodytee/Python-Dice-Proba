from tkinter import *
from tkinter.messagebox import *
from random import *

def change() :
    global nbdes
    global nbfacedes
    global liste
    non = 0
    a = b_nbdes.get()
    for i in range (len(a)) :
        if not a[i] == "0" and not a[i] == "1" and not a[i] == "2" and not a[i] == "3" and not a[i] == "4" and not a[i] == "5" and not a[i] == "6" and not a[i] == "7" and not a[i] == "8" and not a[i] == "9" :
            non = 1
            break
    if non == 0 :
        if not int(a) == 0 :
            nbdes = int(a)
        else :
            showerror("Erreur", "La valeur doit être un chiffre ou un nombre supérieur à 0.")
    else :
        showerror("Erreur", "La valeur doit être un chiffre ou un nombre supérieur à 0.")

    non = 0
    a = b_nbfacedes.get()
    for i in range (len(a)) :
        if not a[i] == "0" and not a[i] == "1" and not a[i] == "2" and not a[i] == "3" and not a[i] == "4" and not a[i] == "5" and not a[i] == "6" and not a[i] == "7" and not a[i] == "8" and not a[i] == "9" :
            non = 1
            break
    if non == 0 :
        if not int(a) == 0 :
            nbfacedes = int(a)
        else :
            showerror("Erreur", "La valeur doit être un chiffre ou un nombre supérieur à 0.")
    else :
        showerror("Erreur", "La valeur doit être un chiffre ou un nombre supérieur à 0.")

    liste = []
    for i in range (nbdes*nbfacedes-nbdes+1) :
        liste += [0]

    affich()

def clear() :
    global liste
    for i in range (len(liste)) :
        liste[i] = 0
    affich()

def lancer1() :
    global nbdes
    global nbfacedes
    global liste
    total = 0
    for i in range (nbdes) :
        total += randint(1,nbfacedes)
    liste[total-nbdes] += 1
    affich()

def lancer10() :
    global nbdes
    global nbfacedes
    global liste
    for i in range (10) :
        total = 0
        for i in range (nbdes) :
            total += randint(1,nbfacedes)
        liste[total-nbdes] += 1
    affich()

def lancer50() :
    global nbdes
    global nbfacedes
    global liste
    for i in range (50) :
        total = 0
        for i in range (nbdes) :
            total += randint(1,nbfacedes)
        liste[total-nbdes] += 1
    affich()

def lancer100() :
    global nbdes
    global nbfacedes
    global liste
    for i in range (100) :
        total = 0
        for i in range (nbdes) :
            total += randint(1,nbfacedes)
        liste[total-nbdes] += 1
    affich()

def affich() :
    global liste
    canvas.delete("all")
    l = canvas.create_line(50,10,50,470)
    l = canvas.create_line(50,470,790,470)
    if max(liste) > 0 :
        echelle = (460/max(liste))*0.6
        for i in range (len(liste)) :
            if liste[i] > 0 :
                r = canvas.create_rectangle((50+(i+1)*10)+((740-(len(liste)+1)*10)/len(liste))*i,470-(liste[i]*echelle),(50+(i+1)*10)+((740-(len(liste)+1)*10)/len(liste))*(i+1),470,fill="purple")
        for i in range (len(liste)) :
            txt = canvas.create_text((50+(i+1)*10)+((740-(len(liste)+1)*10)/len(liste))*i+((740-(len(liste)+1)*10)/len(liste))/2,455-(liste[i]*echelle),text=str(liste[i]),font="Arial 12",fill="black")
    for i in range (0,nbdes*nbfacedes-nbdes+1,1) :
        txt = canvas.create_text((50+(i+1)*10)+((740-(len(liste)+1)*10)/len(liste))*i+((740-(len(liste)+1)*10)/len(liste))/2,485,text=str(i+nbdes),font="Arial 16",fill="blue")

fenetre = Tk()
fenetre.title("Proba dés")

canvas = Canvas(fenetre,width=800,height=500,bg="white")
canvas.pack(side=LEFT,padx=0,pady=0)

cadre = LabelFrame(fenetre,text="",padx=5,pady=5)
cadre.pack(side=LEFT,fill="both",expand="yes")

cadre2 = LabelFrame(cadre,text="",padx=5,pady=5)
cadre2.pack(fill="both",expand="no")

b_nbdes = StringVar()
b_nbdes.set("Nombre de dés")
entree1 = Entry(cadre2,textvariable=b_nbdes,width=30)
entree1.pack()

b_nbfacedes = StringVar()
b_nbfacedes.set("Nombre de face des dés")
entree2 = Entry(cadre2,textvariable=b_nbfacedes,width=30)
entree2.pack()

b_appliquer = Button(cadre2,text="Appliquer",command=change).pack(side=TOP,padx=10,pady=5)

cadre3 = LabelFrame(cadre,text="Lancer",padx=5,pady=5)
cadre3.pack(fill="both",expand="no")

b1 = Button(cadre3,text="1",command=lancer1).pack(side=LEFT,padx=10,pady=5)
b10 = Button(cadre3,text="10",command=lancer10).pack(side=LEFT,padx=10,pady=5)
b50 = Button(cadre3,text="50",command=lancer50).pack(side=LEFT,padx=10,pady=5)
b100 = Button(cadre3,text="100",command=lancer100).pack(side=LEFT,padx=10,pady=5)

b_effacer = Button(cadre,text="Effacer les résultats",command=clear).pack(side=TOP,padx=5,pady=5)

nbdes = 1
nbfacedes = 6

liste = []
for i in range (nbdes*nbfacedes-nbdes+1) :
    liste += [0]

affich()

fenetre.mainloop()