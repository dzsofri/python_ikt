from tkinter import *
foablak=Tk()

def ujablak():
    abl2= Toplevel(foablak)
    uz2=Message(abl2, text="Készítette: Gipsz Jakab\nPiripócs\n2009.06.04", width=300)
    gomb2=Button(abl2, text="Kilép", command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()

szov1=Label(foablak, text="Kattints a gombra!")
gomb1= Button(foablak, text="Névjegy" ,command=ujablak)

szov1.pack()
gomb1.pack() 

foablak.mainloop()