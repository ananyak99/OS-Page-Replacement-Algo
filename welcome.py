from tkinter import*
import random


root=Tk()
root.geometry("1600x8000")
root.title("WELCOME")

def btnClick():
    root.destroy();
    from Login03 import root1
    """global operator
    operator=0
    if operator==0:
        
   #sdef run(runfile):
        with open(runfile,'r') as rnf:
            exec(rnf.read())
    run("Login.py")
   """


Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

lblInfo=Label(Tops,font=('times new roman',40,'bold'),text="WELCOME ",fg="magenta",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('times new roman',40,'bold'),text=" ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

lblInfo=Label(Tops,font=('times new roman',40,'bold'),text="TO ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=2,column=0)

lblInfo=Label(Tops,font=('times new roman',40,'bold'),text="",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=3,column=0)

lblInfo=Label(Tops,font=('times new roman',40,'bold'),text="SCOE RESTAURANT ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=4,column=0)

lblInfo=Label(Tops,font=('times new roman',40,'bold'),text="",fg="magenta",bd=10,anchor='w')
lblInfo.grid(row=5,column=0)

'''def my_callback():
    print("You clicked go button")'''

btnGo=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),command=btnClick,text="GO")
btnGo.place(x=50,y=50)
#root.destroy()
'''def run(runfile):
    with open(runfile,'r') as rnf:
        exec(rnf.read())
run("Login.py")
'''
'''btnGo=Button(f1,text="GO",command=my_callback)
btnGo.pack()'''


root.mainloop()



