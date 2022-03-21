print("Csa")
from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: "+str(c))
def kivonas():
    a = int(mezo4.get())
    b = int(mezo5.get())
    c = a - b
    mezo6.delete(0, END)
    mezo6.insert(0, "Különbség: "+str(c))
def szorzas():
    a = int(mezo4.get())
    b = int(mezo5.get())
    c = a * b
    mezo9.delete(0, END)
    mezo9.insert(0, "Különbség: "+str(c))
foablak=Tk()
cimke=Label(foablak, text="Üdvözlet!", fg="red")
cimke.pack()
gomb1=Button(foablak, text="OK")
gomb1.pack()
gomb2=Button(foablak, text="Mégse")
gomb2.pack()
gomb3=Button(foablak, text="Kilépés", command=foablak.destroy)
gomb3.pack()
mezo1=Entry(foablak)
mezo1.pack()
mezo2=Entry(foablak)
mezo2.pack()
gomb4=Button(foablak, text="Osszead", command=osszeg)
gomb4.pack()
mezo3=Entry(foablak)
mezo3.pack()

mezo4=Entry(foablak)
mezo4.pack()
mezo5=Entry(foablak)
mezo5.pack()
gomb5=Button(foablak, text="KIvonás", command=kivonas)
gomb5.pack()
mezo6=Entry(foablak)
mezo6.pack()


mezo7=Entry(foablak)
mezo7.pack()
mezo8=Entry(foablak)
mezo8.pack()
gomb6=Button(foablak, text="Szorzás", command=szorzas)
gomb6.pack()
mezo9=Entry(foablak)
mezo9.pack()

can1= Canvas(foablak, width=460, height=460, bg="white")
#photo = PhotoImage(file="SB.gif")
#item = can1.create_image(80,80, image= photo)
#can1.grid(row=9, column=1)

foablak.mainloop()