from tkinter import*
import os

root1=Tk()
root1.geometry("702x550+0+0")
root1.configure(background='wheat1')
root1.title("Admin Login")

text_Input=StringVar()
operator=""


TopFrame =Frame(root1,width=702,height=100,bd=14,bg="black",padx=20,relief=RIDGE)
TopFrame.pack(side=TOP)

frame1 =Frame(root1,width=100,height=450,bd=10,bg="powder blue",padx=2,relief=RIDGE)
frame1.pack(side=LEFT)

'''frame2 =Frame(root1,width=234,height=400,bd=10,bg="cadet blue",padx=2,relief=RIDGE)
frame2.pack(side=CENTER)'''

frame3 =Frame(root1,width=100,height=450,bd=10,bg="powder blue",padx=20,relief=RIDGE)
frame3.pack(side=RIGHT)




#=====LABELS===
'''def clear():
    username.set("")
    password.set("")'''

def Reset():
    username1.set("")
    password1.set("")
    

def Cancel():
    root1.destroy()

def submit():
    #if username1=="admin" and password1=="1234" :
        #login=Label(text="Logged in successfully")
        #login.place(x=150,y=450)
        #os.startfile("menucard.py")
    root1.destroy();
    from x import root4
    

    

username1=StringVar()
password1=StringVar()

'''lblLogin = Label(frame1,font=('Times New Roman',15),text="",fg='black',bg='wheat1',anchor='w')
lblLogin.grid(row=0,column=0)'''

lblLogin = Label(root1,font=('Times New Roman',15),text="Admin Login page",fg='black')
lblLogin.place(x=290,y=30)


lblLogin = Label(root1,font=('Times New Roman',15),text="User Name",fg='black')
#lblLogin.grid(row=1,column=1,columnspan=2,rowspan=2)
lblLogin.place(x=150,y=250)

lblLogin = Label(root1,font=('Times New Roman',15),text="Password",fg='black')
lblLogin.place(x=150,y=350)

username=Entry(root1,font=('Times New Roman',16),textvariable=username1,bd=1)
username.place(x=300,y=250)

password=Entry(root1,font=('Times New Roman',16),textvariable=password1,bd=1)
password.place(x=300,y=350)

#===BUTTONS===

clear=Button(root1,padx=5,pady=5,fg='black',font=('Times New Roman',16),
            text='Clear',command=Reset)
clear.place(x=275,y=450)


cancel=Button(root1,padx=5,pady=5,fg='black',font=('Times New Roman',16),
            text='Cancel',command=Cancel)
cancel.place(x=400,y=450)



submit=Button(root1,padx=5,pady=5,fg='black',font=('Times New Roman',16),
            text='SUBMIT',command=submit)
submit.place(x=150,y=450)


'''

btn7=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='7', bg='powder blue',command=lambda:btnClick(7)).grid(row=2,column=0)


btn7=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='7', bg='powder blue',command=lambda:btnClick(7)).grid(row=2,column=0)'''









root1.mainloop()



