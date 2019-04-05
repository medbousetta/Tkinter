from tkinter import *
from tkinter import font
n=Tk()
v2=IntVar()
n.title("seconde")
n.geometry("600x500")
img=PhotoImage(file='Aler.png')
c=Canvas(n,bg='black')
f=font.Font(family='Time',size=20,weight='normal',slant='italic')
c.pack(fill=BOTH,expand=1)


c.create_image(0,0,image=img,anchor=NW)
b1=Button(c,text="ok").pack()
n.mainloop()