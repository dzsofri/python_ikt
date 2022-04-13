from tkinter import *
import math
#nevjegy
def nevjegy():
    abl2= Toplevel(abl1)
    uz2=Message(abl2, text="Készítette: Beréti Zsófia\nBaja\n2022.04.06", width=300)
    gomb2=Button(abl2, text="Kilép", command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()
#------------------

#TEGLATEST FELSZÍN 

def felszin():
    
    def szamit():
        a=eval(m1.get())
        b=eval(m2.get())
        c=eval(m3.get())

        if a<=0 or b<=0 or c<=0:
            m4.delete(0, END)
            m4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            felszin=2*(a*b+a*c+b*c)
            m4.delete(0,END)
            m4.insert(0,str(felszin))

    def habaromvagy():
        try:
            szamit()

        except:
            m4.delete(0, END)
            m4.insert(0, 'Hibás karakter')
            

    abl3= Toplevel(abl1)
    abl3.title("A téglatest felszíne")
    abl3.minsize(width=300, height=100)
    gomb1=Button(abl3, text="Számítás", command=habaromvagy)
    gomb2=Button(abl3, text="Kilép", command=abl3.destroy)
    sz1=Label(abl3, text="a:")
    sz2=Label(abl3, text="b:")
    sz3=Label(abl3, text="c:")
    sz4=Label(abl3, text="Eredmény:")
    m1= Entry(abl3, width=30)
    m2= Entry(abl3, width=30)
    m3= Entry(abl3, width=30)
    m4= Entry(abl3, width=30)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=3)
    sz4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=3, column=2, sticky=W)
    m4.grid(row=5, column=2, sticky=W)
    gomb2.grid(row=4, column=2, sticky=E)
    abl3.mainloop()
#--------------------------


#TÉGLATEST TÉRFOGAT

def terfogat():
    def szamit():

        a=eval(m1.get())
        b=eval(m2.get())
        c=eval(m3.get())
    
        if a<=0 or b<=0 or c<=0:
            m4.delete(0, END)
            m4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terfogat=a*b*c
            m4.delete(0,END)
            m4.insert(0,str(terfogat))

    def habaromvagy():
            try:
                szamit()

            except:
                m4.delete(0, END)
                m4.insert(0, 'Hibás karakter')

    abl3= Toplevel(abl1)
    abl3.title("A téglatest terfogata")
    abl3.minsize(width=300, height=100)
    gomb1=Button(abl3, text="Számítás", command=habaromvagy)
    gomb2=Button(abl3, text="Kilép", command=abl3.destroy)
    sz1=Label(abl3, text="a:")
    sz2=Label(abl3, text="b:")
    sz3=Label(abl3, text="c:")
    sz4=Label(abl3, text="Eredmény:")
    m1= Entry(abl3, width=30)
    m2= Entry(abl3, width=30)
    m3= Entry(abl3, width=30)
    m4= Entry(abl3, width=30)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz3.grid(row=3)
    sz4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m3.grid(row=3, column=2, sticky=W)
    m4.grid(row=5, column=2, sticky=W)
    gomb2.grid(row=4, column=2, sticky=E)
    abl3.mainloop() 
#------------------

#HENGER TÉRFOGAT

def hengerterfogat():
    def szamit():

        r=eval(m1.get())
        m=eval(m2.get())
    
        if m<=0 or r<=0:
            m4.delete(0, END)
            m4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            terfogat =round(math.pi * r * r * m)
            m4.delete(0,END)
            m4.insert(0,str(terfogat))

    def habaromvagy():
            try:
                szamit()

            except:
                m4.delete(0, END)
                m4.insert(0, 'Hibás karakter')

    abl4= Toplevel(abl1)
    abl4.title("A henger terfogata")
    abl4.minsize(width=300, height=100)
    gomb1=Button(abl4, text="Számítás", command=habaromvagy)
    gomb2=Button(abl4, text="Kilép", command=abl4.destroy)
    sz1=Label(abl4, text="magasság:")
    sz2=Label(abl4, text="sugár:")
    sz4=Label(abl4, text="Eredmény:")
    m1= Entry(abl4, width=30)
    m2= Entry(abl4, width=30)
    m4= Entry(abl4, width=30)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m4.grid(row=5, column=2, sticky=W)
    gomb2.grid(row=4, column=2, sticky=E)
    abl4.mainloop() 
#------------------

def hengerfelszin():
    def szamit():

        r=eval(m1.get())
        m=eval(m2.get())
    
        if m<=0 or r<=0:
            m4.delete(0, END)
            m4.insert(0, 'Nem lehet nulla / negatív szám')
        else:
            felszin=round(2*r**2*math.pi+2*r*math.pi*m)
            m4.delete(0,END)
            m4.insert(0,str(felszin))

    def habaromvagy():
            try:
                szamit()

            except:
                m4.delete(0, END)
                m4.insert(0, 'Hibás karakter')

    abl4= Toplevel(abl1)
    abl4.title("A henger felszíne")
    abl4.minsize(width=300, height=100)
    gomb1=Button(abl4, text="Számítás", command=habaromvagy)
    gomb2=Button(abl4, text="Kilép", command=abl4.destroy)
    sz1=Label(abl4, text="magasság:")
    sz2=Label(abl4, text="sugár:")
    sz4=Label(abl4, text="Eredmény:")
    m1= Entry(abl4, width=30)
    m2= Entry(abl4, width=30)
    m4= Entry(abl4, width=30)

    sz1.grid(row=1)
    sz2.grid(row=2)
    sz4.grid(row=5)
    gomb1.grid(row=4, column=2, sticky=W)
    m1.grid(row=1, column=2, sticky=W)
    m2.grid(row=2, column=2, sticky=W)
    m4.grid(row=5, column=2, sticky=W)
    gomb2.grid(row=4, column=2, sticky=E)
    abl4.mainloop() 
#------------------


abl1=Tk()

abl1.title("A téglatest adatai")
abl1.minsize(width=300, height=100)

menusor=Frame(abl1)
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text="Fájl", underline=0)
menu1.pack(side=LEFT)
fajl=Menu(menu1)
fajl.add_command(label="Névjegy", command=nevjegy, underline=0)
fajl.add_command(label="Kilpés", command=abl1.destroy, underline=0)
menu1.config(menu=fajl)

menu2=Menubutton(menusor, text="Téglatest", underline=0)
menu2.pack(side=LEFT)
teglatest=Menu(menu2)
teglatest.add_command(label="Felszín", command=felszin, underline=0)
teglatest.add_command(label="Térfogat", command=terfogat, underline=0)
menu2.config(menu=teglatest)

menu3=Menubutton(menusor, text="Henger", underline=0)
menu3.pack(side=LEFT)
henger=Menu(menu3)
henger.add_command(label="Felszín", command=hengerfelszin, underline=0)
henger.add_command(label="Térfogat", command=hengerterfogat, underline=0)
menu3.config(menu=henger)

abl1.mainloop()