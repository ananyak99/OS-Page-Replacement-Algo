from tkinter import*
import random
import time

root2=Tk()
root2.geometry("900x600+0+0")
#root2.resizable(False)
root2.title("Menu")
root2.configure(background='Light Blue1')

text_Input=StringVar()
operator=""

def cancel():
    root2.destroy();
    from x import root4

Tops = Frame(root2,width = 50,height = 20,bg="Light Blue1",relief=SUNKEN)
Tops.pack(side=TOP)


f0 = Frame(root2,width = 400,height = 700,relief=SUNKEN,bg="Light Blue1")
f0.pack(side=LEFT)

f1 = Frame(root2,width = 500,height = 600,relief=SUNKEN,bg="Light Blue1")
f1.pack(side=LEFT)

f2 = Frame(root2,width = 450,height = 600,relief=SUNKEN,bg="Light Blue1")
f2.pack(side=RIGHT)



#====MENU LABEL====
lblInfo = Label(Tops, font=('Times New Roman',25,'bold'),text='*  SCOE Restaurant  *',fg='black',bg='snow',bd=10, anchor='center')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops, font=('Times New Roman',19,'bold'),text='Today\'s Menu',fg='black',bg='snow',bd=10, anchor='center')
lblInfo.grid(row=1,column=0)

#Bevarages

lblBevarages= Label(f1,font=('helvetica',15,'bold'),text="Bevarages",bd=16,anchor='w',bg="Light Blue1")
lblBevarages.grid(row=0,column=0)

Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Tea",bd=15,anchor='center',bg="Light Blue1").grid(row=1,column=0)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Coffee",bd=15,anchor='center',bg="Light Blue1").grid(row=2,column=0)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Cold Drinks",bd=15,anchor='center',bg="Light Blue1").grid(row=3,column=0)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Milkshake",bd=15,anchor='center',bg="Light Blue1").grid(row=4,column=0)

#Snacks

lblSnacks = Label(f1,font=('Times New Roman',15,'bold'),text="Snacks",bd=16,anchor='w',bg="Light Blue1")
lblSnacks.grid(row=6,column=0)

Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Batata Vada",bd=15,anchor='w',bg="Light Blue1").grid(row=7,column=0)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Samosa",bd=15,anchor='w',bg="Light Blue1").grid(row=8,column=0)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Misal Pav",bd=15,anchor='w',bg="Light Blue1").grid(row=10,column=0)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Idli Sambhar",bd=15,anchor='w',bg="Light Blue1").grid(row=11,column=0)

#Chinese

lblChinese= Label(f1,font=('helvetica',15,'bold'),text="Chinese",bd=16,anchor='w',bg="Light Blue1")
lblChinese.grid(row=0,column=1)

Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Noodles",bd=15,anchor='center',bg="Light Blue1").grid(row=1,column=1)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Manchurian",bd=15,anchor='center',bg="Light Blue1").grid(row=2,column=1)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Tomato Soup",bd=15,anchor='center',bg="Light Blue1").grid(row=3,column=1)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Schezwan Noodles",bd=15,anchor='center',bg="Light Blue1").grid(row=4,column=1)

#Icecream

lblIcecream = Label(f1,font=('Times New Roman',15,'bold'),text="Ice Cream",bd=16,anchor='w',bg="Light Blue1")
lblIcecream.grid(row=6,column=1)

Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Vanilla",bd=15,anchor='w',bg="Light Blue1").grid(row=7,column=1)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Strawberry",bd=15,anchor='w',bg="Light Blue1").grid(row=8,column=1)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Chocolate",bd=15,anchor='w',bg="Light Blue1").grid(row=10,column=1)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Butterscotch",bd=15,anchor='w',bg="Light Blue1").grid(row=11,column=1)

#chats

lblChats= Label(f1,font=('helvetica',15,'bold'),text="Chats",bd=16,anchor='w',bg="Light Blue1")
lblChats.grid(row=0,column=2)

Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Sev Puri",bd=15,anchor='center',bg="Light Blue1").grid(row=1,column=2)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Dahivada",bd=15,anchor='center',bg="Light Blue1").grid(row=2,column=2)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Ragada Patties",bd=15,anchor='center',bg="Light Blue1").grid(row=3,column=2)
Checkbutton(f1,font=('Times New Roman',13,'bold'),text="Pav Bhaji",bd=15,anchor='center',bg="Light Blue1").grid(row=4,column=2)

'''#Icecream

lblIcecream = Label(f1,font=('Times New Roman',19,'bold'),text="Ice Cream",bd=16,anchor='w',bg="Light Blue1")
lblIcecream.grid(row=6,column=1)

Checkbutton(f1,font=('Times New Roman',15,'bold'),text="Vanilla",bd=15,anchor='w',bg="Light Blue1").grid(row=7,column=1)
Checkbutton(f1,font=('Times New Roman',15,'bold'),text="Strawberry",bd=15,anchor='w',bg="Light Blue1").grid(row=8,column=1)
Checkbutton(f1,font=('Times New Roman',15,'bold'),text="Chocolate",bd=15,anchor='w',bg="Light Blue1").grid(row=10,column=1)
Checkbutton(f1,font=('Times New Roman',15,'bold'),text="Butterscotch",bd=15,anchor='w',bg="Light Blue1").grid(row=11,column=1)

'''
btncancel=Button(root2,text='Cancel',font=('Times New Roman',16),command=cancel)
btncancel.place(x=10,y=520)
root2.mainloop()
