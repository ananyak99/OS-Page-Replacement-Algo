from tkinter import *
import random
import time

import sqlite3
conn = sqlite3.connect('E:\menu.sqlite')
cur = conn.cursor()


root5=Tk()
root5.geometry("1200x700+0+0")
root5.title("Restaurant Management System")
root5.configure(background='wheat1')

text_Input=StringVar()
operator=""

bevarages = StringVar()
snacks = StringVar()
chinese = StringVar()
icecream = StringVar()
chats = StringVar()

bevaragesno=StringVar()
snacksno =StringVar()
chineseno =StringVar()
icecreamno =StringVar()
chatsno =StringVar()
rand=StringVar()

bevaragesno1=StringVar()
snacksno1 =StringVar()
chineseno1 =StringVar()
icecreamno1 =StringVar()
chatsno1 =StringVar()

totalitems1=StringVar()
#totalitems2=int(totalitems1.get())
total1=StringVar()
#total2=int(total1.get())


customer=StringVar()
address=StringVar()
phone=StringVar()

#==functions

def funcbevarages(*args):
    print( bevarages.get() )

def funcsnacks(*args):
    print( snacks.get() )

def funcchinese(*args):
    print( chinese.get() )

def funcicecream(*args):
    print( icecream.get() )

def funcchats(*args):
    print( chats.get() )

def count():
    i=0
    for i in range(0, ):
        i=i+1
        print(i)

def cancel():
    root5.destroy();
    from THanks import root6

def gb():
    x= random.randrange(1,500876)
    randomRef= str(x)
    rand.set(randomRef)

  #  cur.execute("SELECT COST FROM menu WHERE ITEM=? OR COST=?", (ITEM,COST))

 #   rows = cur.fetchall()
  #  print(rows)
   # for row in rows:
       # print "{}".format(row["cost"])
    

    txtpayslip.insert(END,"\t\t   APUN KA RESTAURANT\t\t\n")
    txtpayslip.insert(END,"\t\t\tCustomer Info\t\t\n")
   # txtpayslip.insert(END,"Customer Info\t\n")
    txtpayslip.insert(END,"Customer ID:\t"+rand.get()+"\n")
    txtpayslip.insert(END,"Customer Name:\t"+customer.get()+"\n")
    txtpayslip.insert(END,"Customer Address:\t"+address.get()+"\n")
    txtpayslip.insert(END,"Phone Number:\t\n\n\n"+phone.get()+"\n")

    txtpayslip.insert(END,"\t\t\tBILL\t\t\n")
    

    txtpayslip.insert(END,"Items \t\tNumber of items\t\tCost\t\n")
    txtpayslip.insert(END,""+bevarages.get()+"\t\t"+bevaragesno.get()+"\t\t"+bevaragesno1.get()+"\n")
    txtpayslip.insert(END,""+snacks.get()+"\t\t"+snacksno.get()+"\t\t"+snacksno1.get()+"\n")
    txtpayslip.insert(END,""+chinese.get()+"\t\t"+chineseno.get()+"\t\t"+chineseno1.get()+"\n")
    txtpayslip.insert(END,""+icecream.get()+"\t\t"+icecreamno.get()+"\t\t"+icecreamno1.get()+"\n")
    txtpayslip.insert(END,""+chats.get()+"\t\t"+chatsno.get()+"\t\t"+chatsno1.get()+"\n")
    txtpayslip.insert(END,""+totalitems.get()+"\t\t"+total.get()+"\n")
    

    
  

   
#    item1=bevaragesno+snacksno+chineseno+icecreamno+chatsno
#    amount1=int(bevaragesno1.get())+int(snacksno1.get())+int(chineseno1.get())+int(icecreamno1.get())+int(chatsno1.get())
#    totalitems2.set(item1)
#    total2.set(amount1)
#def btnClick(numbers):
'''    global operator
    operator = operator+ str(item1)
    item1.set(operator)

'''

#==framing==

f1= Frame(root5,width = 1200,height = 70,bg="black",relief=SUNKEN)
f1.pack(side=TOP)

f2= Frame(root5,width = 600,height = 630,bg="white",relief=SUNKEN)
f2.pack(side=LEFT)

f3= Frame(root5,width = 600,height = 630,bg="blue1",relief=SUNKEN)
f3.pack(side=RIGHT)


#===Randommm=====
#def Ref():
    
 #ref
lblReference = Label(f2,text="Customer id")
lblReference.place(x=10,y=20)
txtReference=Entry(f2,textvariable=rand,width=36)
txtReference.place(x=250,y=20)


#=====TEXT WIDGET====
#txtpayslip=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="green",bg="powder blue")
txtpayslip=Text(f3,height=22,width=60,font=('Times New Roman',13,'bold'),bg="white")
txtpayslip.place(x=30,y=10)

#txtpayslip.insert(END,"\t\tPay Slip\n\n")


#==LABELS==
lblInfo = Label(f1, font=('Times New Roman',20,'bold'),text="SCOE Restaurant",fg='black',bd=10, anchor='w')
lblInfo.place(x=500,y=15)


#===NAME &ETC==
custname=Label(f2, text="Customer name")
custname.place(x=10,y=70)

customer_name=Entry(f2,textvariable=customer,width=36)
customer_name.place(x=250,y=70)

custadd=Label(f2, text="Address")
custadd.place(x=10,y=130)

customer_add=Entry(f2,textvariable=address,width=36)
customer_add.place(x=250,y=130)

custphone=Label(f2, text="Phone Number")
custphone.place(x=10,y=200)

cust_phone=Entry(f2,textvariable=phone,width=36)
cust_phone.place(x=250,y=200)

lblMenu=Label(f2, font=('Times New Roman',13,'bold'),text="Dishes",fg='black',bd=10)
lblMenu.place(x=50,y=240)

lblquantity=Label(f2, font=('Times New Roman',13,'bold'),text="Quantity",fg='black',bd=10)
lblquantity.place(x=250,y=240)

lblCost=Label(f2, font=('Times New Roman',13,'bold'),text="Cost",fg='black',bd=10)
lblCost.place(x=400,y=240)

billtotal=Label(f2, text="  TOTAL  ")
billtotal.place(x=10,y=520)

totalitems=Entry(f2,textvariable=totalitems1,width=13)
totalitems.place(x=250,y=520)

total=Entry(f2,textvariable=total1,width=13)
total.place(x=400,y=520)


#bevarages
choices = { 'Tea','Coffee','Cold Drinks','Milkshake'}
bevarages.set('Choose one')
popupMenu = OptionMenu(f2,bevarages , *choices)
Label(f2, text="Bevarages").place(x=10,y=300)
popupMenu.place(x=100,y=300)
bevarages.trace('w', funcbevarages)

#Snacks
choices = { 'Batata Vada','Samosa','Misal Pav','Idli Sambhar'}
snacks.set('Choose one')
popupMenu = OptionMenu(f2, snacks, *choices)
Label(f2, text="Snacks").place(x=10,y=340)
popupMenu.place(x=100,y=340)
snacks.trace('w', funcsnacks)

#Chinese
choices = { 'Hakka Noodles ','Tomato soup','Manchurian','Schezwan Noodles'}
chinese.set('Choose one')
popupMenu = OptionMenu(f2,chinese , *choices)
Label(f2, text="Chinese").place(x=10,y=380)
popupMenu.place(x=100,y=380)
chinese.trace('w', funcchinese)

#Icecream
choices = { 'Vanilla','Strawberry','Chocolate','Butter scotch'}
icecream.set('Choose one')
popupMenu = OptionMenu(f2, icecream, *choices)
Label(f2, text="Icecream").place(x=10,y=420)
popupMenu.place(x=100,y=420)
icecream.trace('w', funcicecream)

#Chats
choices = { 'Sev Puri','Dahi vada','Ragada Patties','Pav Bhaji'}
chats.set('Choose one')
popupMenu = OptionMenu(f2, chats, *choices)
Label(f2, text="Chats").place(x=10,y=460)
popupMenu.place(x=100,y=460)
chats.trace('w', funcchats)

#===============Number of items selected==============

Number_of_Bevarages=Entry(f2,font=('Times New Roman',16),textvariable=bevaragesno,width=7)
Number_of_Bevarages.place(x=250,y=300)
#bevaragesno=int(Number_of_Bevarages.get())

Number_of_Snacks=Entry(f2,font=('Times New Roman',16),textvariable=snacksno,width=7)
Number_of_Snacks.place(x=250,y=340)
#snacksno=int(Number_of_Snacks.get())

Number_of_Chinese=Entry(f2,font=('Times New Roman',16),textvariable=chineseno,width=7)
Number_of_Chinese.place(x=250,y=380)
#chineseno=int(Number_of_Chinese.get())

Number_of_Icecream=Entry(f2,font=('Times New Roman',16),textvariable=icecreamno,width=7)
Number_of_Icecream.place(x=250,y=420)
#icecreamno=int(Number_of_Icecream.get())

Number_of_chats=Entry(f2,font=('Times New Roman',16),textvariable=chatsno,width=7)
Number_of_chats.place(x=250,y=460)
#chatsno=int(Number_of_chats.get())

#===============COST FOR ITEMS=========================
Number_of_Bevarages1=Entry(f2,font=('Times New Roman',16),textvariable=bevaragesno1,width=7)
Number_of_Bevarages1.place(x=400,y=300)
#bevaragesno=int(Number_of_Bevarages.get())

Number_of_Snacks1=Entry(f2,font=('Times New Roman',16),textvariable=snacksno1,width=7)
Number_of_Snacks1.place(x=400,y=340)
#snacksno=int(Number_of_Snacks.get())

Number_of_Chinese1=Entry(f2,font=('Times New Roman',16),textvariable=chineseno1,width=7)
Number_of_Chinese1.place(x=400,y=380)
#chineseno=int(Number_of_Chinese.get())

Number_of_Icecream1=Entry(f2,font=('Times New Roman',16),textvariable=icecreamno1,width=7)
Number_of_Icecream1.place(x=400,y=420)
#icecreamno=int(Number_of_Icecream.get())

Number_of_chats1=Entry(f2,font=('Times New Roman',16),textvariable=chatsno1,width=7)
Number_of_chats1.place(x=400,y=460)



'''lbltotal_no_of_items=Label(f2,font=('Times New Roman',16),text="Total number of items",fg='black')
lbltotal_no_of_items.place(x=30,y=530)
'''
#===BUTTONS===
btngen=Button(f3,text='Generate',font=('Times New Roman',16),command=gb)
btngen.place(x=100,y=520)

btncancel=Button(f3,text='Cancel',font=('Times New Roman',16),command=cancel)
btncancel.place(x=300,y=520)



'''def shree():
    global anjali
   
    x=(int(bevaragesno))
    print(x)


def btnClick(textvariable):
    global operator
    operator = operator+ str(textvariable)
    text_Input.set(operator)

b=Button(text="total",height=1,width=2,command=btnClick)
b.place(x=280,y=580)

'''





root5.mainloop()
