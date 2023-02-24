import tkinter as tk

HEIGHT=500
WIDTH=500


def fermer_fenetre():
    fenetre.destroy()
def dessindisque():
    canvas.create_oval((100,100), (300, 300), fill="blue", width=5)
def dessincarre():
    canvas.create_rectangle((100,100),(300,300),fill="red")
def dessincroix():
    canvas.create_rectangle((100,100),(300,300),fill="yellow")
    canvas.create_line((100,100),(300,300),  fill="green")   

def afficher_couleur():
    while True:
        r = int(input("Teinte de rouge? "))
        v = int(input("Teinte de vert? "))
        b = int(input("Teinte de bleu? "))
        if 0 <= r <= 255 and 0 <= v <= 255 and 0 <= b <= 255:
            break    
 
fenetre=tk.Tk()
fenetre.title("Mon dessin")

canvas=tk.Canvas(fenetre,bg="black",height=HEIGHT, width=WIDTH)
canvas.grid(column=1,row=1)

Bhaut=tk.Button(fenetre, text="Choisir une couleur",command=afficher_couleur,font=("helvetica","15"))
Bhaut.grid(column=1,row=0)

B2=tk.Button(fenetre,text="Cercle",command=dessindisque  ,font=("helvetica","10"))
B2.grid(column=0,row=0,padx=15)

B3=tk.Button(fenetre,text="Carré",command=dessincarre,font=("helvetica","10"))
B3.grid(column=0,row=1)

B4=tk.Button(fenetre,text="Croix",command=dessincroix ,font=("helvetica","10"))
B4.grid()








fenetre.mainloop()