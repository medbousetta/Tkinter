from tkinter import *
n=Tk()
n.geometry("400x400")
v2=IntVar()
n.title("seconde")
'''
ss=Scale(n,variable=v2).pack()
'''
s=Scrollbar(n)
s.pack(side=RIGHT,fill=Y)
l=Listbox(n,yscrollcommand=s.set)
for b in range (100):
    l.insert(b,b)
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview)
'''
def p():
 print(v2.get())
b1=Button(n,command=p).place(x=150,y=100)
'''
n.mainloop()
