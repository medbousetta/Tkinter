from tkinter import *
from tkinter import messagebox
from tkinter import ttk
n=Tk()
n.title("test")
n.config(background="#e1d8b2")





#style
Style=ttk.Style()
Style.theme_use('classic')
Style.configure('TLabel',background="#e1d8b2")
Style.configure('TButton',background="#e1d8b2")
Style.configure('TRadiobutton',background="#e1d8b2")


#full name
ttk.Label(n,text="path file").grid(row=0,column=0,padx=10,pady=10)
EntryFullname=ttk.Entry(n,width=30,font=('Arial',16))
EntryFullname.grid(row=0,column=1,columnspan=2,pady=10)
#gendre
ttk.Label(n,text="Test Type").grid(row=1,column=0)
SpanGendre=StringVar()
ttk.Radiobutton(n,text="Steps",variable=SpanGendre,value="male").grid(row=1,column=1)
ttk.Radiobutton(n,text="Actors",variable=SpanGendre,value="Actors").grid(row=1,column=2)
ttk.Radiobutton(n,text="Cooding",variable=SpanGendre,value="Cooding").grid(row=1,column=3)

#comment
OK=ttk.Button(n,text="ok")
OK.grid(row=3,column=3)
OK2=ttk.Button(n,text="ok")
OK2.grid(row=3,column=2)

#comment
ttk.Label(n,text="Changes").grid(row=2,column=0)
txtComments=Text(n,width=30,height=15,font=('Arial',16)).grid(row=2,column=1,columnspan=2)

n.mainloop()
