from tkinter import *
foablak=Tk()
gyoker="H:\\IKT\\python\\"

cimke=Label(foablak, text="Első mező", pady=10)
cimke.grid(row=1, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=1, column=2)

cimke2=Label(foablak, text="Második", pady=10)
cimke2.grid(row=3, column=1)
mezo2=Entry(foablak)
mezo2.grid(row=3, column=2)

cimke3=Label(foablak, text="Harmadik", pady=10)
cimke3.grid(row=5, column=1)
mezo3=Entry(foablak)
mezo3.grid(row=5, column=2)

can1= Canvas(foablak, width=160, height=160, bg="white")
icon = PhotoImage(file=gyoker+"cica.png")
foablak.iconphoto(True, icon)
photo = PhotoImage(file=gyoker+"csavesz.png")
item = can1.create_image(80,80, image= photo)

can1.grid(row=1, column=3, rowspan=5)

foablak.mainloop()