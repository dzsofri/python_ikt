from tkinter import *
foablak=Tk()
gyoker="H:\\IKT\\python\\"
import math

def terfogat():
    r = int(mezo1.get())
    m = int(mezo2.get())
    terfogat = round (math.pi * r * r * m )
    liter=0.001*terfogat
    mezo3.delete(0, END)
    mezo3.insert(0, str(liter)+' l')
    borocska= int(mezo4.get())
    telitett=0
    telitett= terfogat/borocska 
    if borocska<=liter:
        mezo3.delete(0, END)
        mezo3.insert(0, str(liter)+' l')
        mezo5.delete(0, END)
        mezo5.insert(0, str(liter-borocska)+' l')
        mezo6.delete(0, END)
        mezo6.insert(0, str(telitett)+" %")      
    else:
        mezo3.delete(0, END)
        mezo3.insert(0, 'A hordó túl kicsi')
        mezo6.delete(0, END)
        mezo6.insert(0, 'A hordó túl kicsi')



cimke4=Label(foablak, text="Hány liter bor (l):")
cimke4.grid(row=1, column=1, sticky="e")
mezo4=Entry(foablak)
mezo4.grid(row=1, column=2, columnspan=4)

cimke1=Label(foablak, text="Sugár (cm):")
cimke1.grid(row=2, column=1, sticky="e")
mezo1=Entry(foablak)
mezo1.grid(row=2, column=2, columnspan=4)

cimke2=Label(foablak, text="Magasság (cm):")
cimke2.grid(row=3, column=1, sticky="e")
mezo2=Entry(foablak)
mezo2.grid(row=3, column=2, columnspan=4)

gomb1=Button(foablak, text="Kiszámít", command=terfogat) 
gomb1.grid(row=4, column=2, sticky="w")

cimke3=Label(foablak, text="A hordó ennyi liter:")
cimke3.grid(row=5, column=1, sticky="e")
mezo3=Entry(foablak)
mezo3.grid(row=5, column=2, columnspan=4)

cimke5=Label(foablak, text="A hordóba ennyi liter fér még:")
cimke5.grid(row=6, column=1, sticky="e")
mezo5=Entry(foablak)
mezo5.grid(row=6, column=2, columnspan=4)

cimke6=Label(foablak, text="Telítetség")
cimke6.grid(row=7, column=1, sticky="e")
mezo6=Entry(foablak)
mezo6.grid(row=7, column=2, columnspan=4)

foablak.mainloop()