from tkinter import *
n=Tk()
n.geometry("400x400")
n.title("simple project")
def p1():
    print("hello")
def p2():
    print("goodbye")
menubar= Menu(n)
file_menu=Menu(menubar,tearoff=0)
edit_menu=Menu(menubar,tearoff=0)
file_menu.add_command(label="new",command=p1)
file_menu.add_separator()
file_menu.add_command(label="copy",command=p2)
edit_menu.add_command(label="new",command=p1)
edit_menu.add_command(label="copy",command=p2)
menubar.add_cascade(label= "File",menu=file_menu)
menubar.add_cascade(label= "Edit",menu=edit_menu)

n.config(menu=menubar)
n.mainloop()