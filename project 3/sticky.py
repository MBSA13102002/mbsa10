    





import time
import os
from tkinter import*
from tkinter import messagebox
import mysql.connector
from datetime import date 
today=date.today()
mycon=mysql.connector.connect(host="localhost",user="root",passwd="tigron",database="BankMangement")
if mycon.is_connected():
    print("successfully connected")
qa=mycon.cursor()
global w
global p10
global var
global c3
root1=Tk()
root1.geometry("1366x768")
root1.title("INITIATOR")
       
def mh():
    
    os.system("rand.mp4")
    root1.destroy()
    
    
    
    
    
qz=Canvas(root1,bg="red",width=1366,height=768)
d=Label(root1,text="LETS BEGIN THE EXPLORATION",bg="black",fg="green yellow")
d.config(font=("Helvetica",44))
d.place(x=250,y=100)
d=Label(root1,text="CLICK NEXT TO BEGIN",bg="black",fg="green yellow")
d.config(font=("Helvetica",44))
d.place(x=250,y=200)
q11=Button(root1,text="NEXT",width=20,bg="cyan",command=mh)
q11.place(x=250,y=400)
q11.config(font=("Helvetica",35)) 


qz.place(x=0,y=0)
root1.mainloop()
time.sleep(0)
root=Tk()
root.title("BANK MANAGEMENT")
root.geometry("1366x768")
def gen():
    global gen
    import random
    rd=random.randint(1,999999999999999999)
    bcd="1013"
    ccd="91"
    ckd="19"
    gen=str(rd)+bcd+ccd+ckd
    return gen
def db():
    qa=mycon.cursor()
    uy="create table {}{}1(CURDATE varchar(56),ACCBALANCE varchar(56))".format(e.get(),p1.get())
    uy1="create table {}{}2(SNO varchar(56),CURDATE varchar(56),ACCWITHDRAWL varchar(56),AMOUNTAVAL varchar(56))".format(e.get(),p1.get())
    uy2="create table {}{}4(BALANCE varchar(56))".format(e.get(),p1.get())
    uy3="create table {}{}3(CURDATE varchar(56),DEPOSIT varchar(56),AMOUNTAVAL varchar(56))".format(e.get(),p1.get())                                                                                                                  
    uy4="insert into {}{}1(CURDATE ,ACCBALANCE)values('{}','{}')".format(e.get(),p1.get(),today,p10.get())
    uy5="insert into {}{}4(BALANCE)values('{}')".format(e.get(),p1.get(),p10.get())
    uy6="create table {}{}5(AMOUNT varchar(56))".format(e.get(),p1.get())
    uy7="insert into {}{}5(AMOUNT)values('{}')".format(e.get(),p1.get(),p10.get())
    uy8="create table {}{}6(DATE varchar(56),WITHDRAWL VARCHAR(56),DEPOSIT varchar(56),AMOUNTAVAL varchar(56))".format(e.get(),p1.get())

    qa.execute(uy)
    qa.execute(uy1)
    qa.execute(uy2)
    qa.execute(uy3)
    qa.execute(uy4)
    qa.execute(uy5)
    qa.execute(uy6)
    qa.execute(uy7)
    qa.execute(uy8)
    
    mycon.commit()                               
                                   
    
    
def mb():
    ans=messagebox.askquestion("successful","go further!!!")
    if ans=="no":
       root.quit()
    if ans=="yes":
       root=Tk()
       root.geometry("1366x768")
def nm():
     ans=messagebox.showwarning("WARNING","WRONG INPUT PLEASE CHECK!!!")
def t1():
     ans=messagebox.showwarning("WARNING","YOUR ACCOUNT BALANCE IS LOW,TRANSACTION NOT ALLOWED !!!")
def pin():
     ans=messagebox.showwarning("WARNING","WRONG PIN PLEASE CHECK!!!")
def popup():
     ans=messagebox.showwarning("WARNING","PLEASE ENTER AMOUNT!!!")
def nm1():
     ans=messagebox.showwarning("WARNING","EMPTY ENTRIES. PLEASE FILL!!!")
def nm2():
     ans=messagebox.showwarning("WARNING","WRONG FORMAT OF ADDRESS(ONLY LETTERS)PLEASE CHECK!!!")
def nm3():
     ans=messagebox.showwarning("WARNING","WRONG FORMAT OF USERNAME(ONLY LETTERS)PLEASE CHECK!!!")
def nm4():
     ans=messagebox.showwarning("WARNING","WRONG FORMAT OF AGE(ONLY DIGITS)PLEASE CHECK!!!")
def nm5():
     ans=messagebox.showwarning("WARNING","WRONG FORMAT OF INITIALDEPOSIT(ONLY DIGITS)PLEASE CHECK!!!")
def nm6():
     ans=messagebox.showwarning("WARNING","WRONG FORMAT OF D.O.B(ONLY DIGITS)PLEASE CHECK!!!")
def nm7():
     ans=messagebox.showwarning("WARNING","WRONG FORMAT OF GENDER(ONLY LETTER)PLEASE CHECK!!!")
def nm8():
     ans=messagebox.showwarning("WARNING","PLEASE CHECK THE PHONE NO. AND PRESS THE CONFIRM !!!")
def nm9():
     ans=messagebox.showwarning("WARNING","WRONG FORMAT OF AADHAR(ONLY DIGITS)PLEASE CHECK!!!")
def nb():
     ans=messagebox.showwarning("WARNING","PHONE NUMBER SHOULD BE OF 10 DIGITS!!!")
def nb1():
     ans=messagebox.showwarning("WARNING","PHONE NUMBER MUST BE OF DIGITS!!!")
def mb0():
     ans=messagebox.showwarning("WARNING","FORMAT SHOULD BE AS:(AAABV1234C) PLEASE CHECK!!!")
def mb1():
     ans=messagebox.showwarning("WARNING","PHONE NUMBER DOSN'T MATCH !!!")
def mb4():
     ans=messagebox.showwarning("WARNING","PASSWORD SHOULD BE EQUAL!!!")     
def mb5():
    st="insert into coders(USERNAME,PHONENO)values('{0}','{1}')".format(e.get(),p1.get())
    st1="update coders set ADDRESS='{0}' where USERNAME='{1}'".format(p3.get(),e.get())
    st2="update coders set PANNO='{0}' where USERNAME='{1}'".format(p4.get(),e.get())
    st3="update coders set DOB='{0}' where USERNAME='{1}'".format(p8.get(),e.get())
    st4="update coders set GENDERSEX='{0}' where USERNAME='{1}'".format(j.get(),e.get())
    st5="update coders set AADHARNO ='{0}' where USERNAME='{1}'".format(p5.get(),e.get())
    st6="update coders set AGE='{0}' where USERNAME='{1}'".format(p6.get(),e.get())
    st7="update coders set PASSWORD='{0}' where USERNAME='{1}'".format(c3.get(),e.get())
    st8="update coders set PINNO='{0}' where USERNAME='{1}'".format(p9.get(),e.get())
    st9="update coders set INITIALDEPOSIT='{0}' where USERNAME='{1}'".format(p10.get(),e.get())
    st10="update coders set ACCNO='{0}' where USERNAME='{1}'".format(gen(),e.get())
    qa.execute(st)
    qa.execute(st1)
    qa.execute(st2)
    qa.execute(st3)
    qa.execute(st4)
    qa.execute(st5)
    qa.execute(st6)
    qa.execute(st7)
    qa.execute(st8)
    qa.execute(st9)
    qa.execute(st10)

       
    
    
    
    mycon.commit()
    ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
def mb2():
    ans=messagebox.askquestion("SUCCESSFUL","PROCEED")
def mb3():
    def mb6():
        if c3.get()!=c4.get():
           mb4()
        elif c3.get() is None and c4.get() is None:
             mb4()
        elif c3.get() is None:
             mb4()
        else:
             mb5()
             
    root=Tk()
    root.title(" SET PASSWORD ")
    root.geometry("250x250+550+280")
    ti=Frame(root,bg="black",width=1366,height=766)
    ti.place(x=0,y=0)
    
    global c3
    c3=Entry(root,show="*",width=20,bg="OliveDrab1")
    c3.place(x=70,y=40)
    global c4
    c4=Entry(root,show="*",bg="OliveDrab1")
    c4.place(x=70,y=100)
   
 

    s=Label(root,text="PASSWORD",bg="black",fg="yellow")
    s.place(x=60,y=10)
    q=Label(root,text="CONFIRM PASSWORD",bg="black",fg="yellow")
    q.place(x=60,y=70)
    
    d=Button(root,text="CONFIRM",bg="lawn green",command=mb6)
    d.place(x=100,y=130)
    db()
    global rt
    
    rt=c3.get()
    global ed
    ed=c4.get()
    
       
def EU():
     a=Canvas(root,bg="brown4",width=500,height=500)
     a.place(x=860,y=150)
     b1=a.create_line(0,0,0,500,fill="black",width=15)
     b2=a.create_line(0,0,500,0,fill="black",width=15)
     b3=a.create_line(0,500,500,500,fill="black",width=15)
     b4=a.create_line(500,0,500,500,fill="black",width=15)

     def mj():
         kl=lee.get()
         if kl=="yes" or kl=="YES":
            mb7()
            le.destroy()
            lee.destroy()
            u.destroy()
         elif kl=="no" or kl=="NO":
             o=Label(a,text="CREATE A NEW ACCOUNT",bg="brown4",fg="medium spring green")
             o.place(x=30,y=270)
             o.config(font=("Algerian",20))
             NU()
         else:
             nm()
     le=Label(a,text="I AM AN EXISTING USER:-",bg="black",fg="medium spring green")
     le.place(x=30,y=40)
     le.config(font=("Algerian",20))
     lee=Entry(a,width=25,bg="medium spring green",fg="red")
     lee.place(x=30,y=100)
     lee.config(font=("courier",15))
     
     u=Button(a,text="CONFIRM",width=20,height=3,bg="black",fg="yellow",command=mj)
     u.place(x=35,y=150)
     u.config(font=("courier",15))
def mb7():
    def mb8():
        if c7.get().isalpha()==True and c4.get().isalnum()==True and c5.get().isdigit()==True and c7.get is not None and c4.get() is not None and c5.get is not None :  
           qa.execute("select USERNAME,PHONENO,PASSWORD from coders")
           u=qa.fetchall()
           def mb9():
               root=Tk()
               root.title("BANK MANAGEMENT2 ")
               root.geometry("1366x768")
               global l
               global r
               qa.execute("select*from coders where PHONENO='{}'".format(c5.get()))
               l=qa.fetchone()
               d=list(l)
               r=Frame(root,bg="dark green",width=1500,height=1500)
               r.place(x=0,y=0)
               s=Label(root,text="USERNAME",width=12,bg="orange")
               s.place(x=10,y=10)
               s.config(font=("Courier",15))
    
               q=Label(root,text="PHONE.No ",width=12,bg="orange")
               q.place(x=10,y=40)
               q.config(font=("Courier",15))

               q2=Label(root,text="ADDRESS: ",width=12,bg="orange")
               q2.place(x=10,y=70)
               q2.config(font=("Courier",15))

               q3=Label(root,text="PAN.NO: ",width=12,bg="orange")
               q3.place(x=400,y=10)
               q3.config(font=("Courier",15))

               q4=Label(root,text="AADHAR.NO: ",width=12,bg="orange")
               q4.place(x=400,y=40)
               q4.config(font=("Courier",15))

               q5=Label(root,text="AGE: ",width=12,bg="orange")
               q5.place(x=400,y=70)
               q5.config(font=("Courier",15))  
  
               q6=Label(root,text="SEX/GENDER: ",width=12,bg="orange")
               q6.place(x=790,y=10)
               q6.config(font=("Courier",15)) 

               q7=Label(root,text="D.O.B: ",width=12,bg="orange")
               q7.place(x=790,y=40)
               q7.config(font=("Courier",15))
            
               q8=Label(root,text="INITIAL DEPOSIT ",width=16,bg="orange")
               q8.place(x=790,y=70)
               q8.config(font=("Courier",15))


               q6=Label(root,width=18,text="{}".format(l[0]),bg="black",fg="red")
               q6.place(x=165,y=10)
               q6.config(font=("Courier",15)) 

               q7=Label(root,width=18,text="{}".format(l[2]),bg="black",fg="red")
               q7.place(x=165,y=40)
               q7.config(font=("Courier",15))


               q6=Label(root,width=18,text="{}".format(l[1]),bg="black",fg="red")
               q6.place(x=165,y=70)
               q6.config(font=("Courier",15)) 

               q7=Label(root,width=18,text="{}".format(l[5]),bg="black",fg="red")
               q7.place(x=560,y=10)
               q7.config(font=("Courier",15))

        
               q6=Label(root,width=18,text="{}".format(l[6]),bg="black",fg="red")
               q6.place(x=560,y=40)
               q6.config(font=("Courier",15)) 

               q7=Label(root,width=18,text="{}".format(l[7]),bg="black",fg="red")
               q7.place(x=560,y=70)
               q7.config(font=("Courier",15))

            
               q6=Label(root,width=18,text="{}".format(l[4]),bg="black",fg="red")
               q6.place(x=950,y=10)
               q6.config(font=("Courier",15)) 

               q7=Label(root,width=18,text="{}".format(l[3]),bg="black",fg="red")
               q7.place(x=950,y=40)
               q7.config(font=("Courier",15))

            
               q6=Label(root,width=18,text="{}".format(l[10]),bg="black",fg="red")
               q6.place(x=1000,y=70)
               q6.config(font=("Courier",15))
               def ed():
                   global m2   
                   m11=Tk()
                   m11.title("EDIT INFO SHELL")
                   m11.geometry("1000x600+230+70")
                   mm11=Canvas(m11,bg="light sea green",width=1366,height=768)
                   mm11.place(x=0,y=0)
                   dis=Label(mm11,text="WELCOME MR.{}".format(c7.get()),bg="light sea green",fg="gray25",width=25)
                   dis.place(x=250,y=10)
                   dis.config(font=("Algerian",25))
                   
                   dis1=Label(mm11,text="PLEASE CLICK THE FOLLOWING,TO CHANGE DETAILS",bg="light sea green",fg="gray25",width=40)
                   dis1.place(x=20,y=60)
                   dis1.config(font=("Algerian",25))
                   def PNE():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR NEW PHONENO.",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms2():
                           qa=mycon.cursor()
                           ug="update coders set ALTNO='{0}' where PASSWORD='{1}'".format(eis1.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms2)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15)) 
                   

                   
                   pan=Button(mm11,text="PHONE NO",bg="dark green",fg="yellow",width=15,command=PNE)
                   pan.place(x=200,y=150)
                   pan.config(font=("Cambridge",15))
                   def dd():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR NEW ADDRESS.",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms2():
                           qa=mycon.cursor()
                           ug="update coders set ADDRESS='{0}' where USERNAME='{1}'AND PASSWORD='{2}'".format(eis1.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms2)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15)) 
                   
                   addr=Button(mm11,text="ADDRESS",bg="dark green",fg="yellow",width=15,command=dd)
                   addr.place(x=30,y=190)
                   addr.config(font=("Cambridge",15))
                   def pno1():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR CORRECT PANNO.",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms3():
                           qa=mycon.cursor()
                           ug="update coders set PANNO='{0}' where USERNAME='{1}'AND PASSWORD='{2}'".format(eis1.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms3)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15))
                       
                   pan=Button(mm11,text="PANNO",bg="dark green",fg="yellow",width=15,command=pno1)
                   pan.place(x=200,y=230)
                   pan.config(font=("Cambridge",15))
                   def DOB():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR CORRECT D.O.B",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms4():
                           qa=mycon.cursor()
                           ug="update coders set DOB='{0}' where USERNAME='{1}'AND PASSWORD='{2}'".format(eis1.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms4)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15))    
                   
                   dob=Button(mm11,text="D.O.B",bg="dark green",fg="yellow",width=15,command=DOB)
                   dob.place(x=30,y=270)
                   dob.config(font=("Cambridge",15))
                   
                   def AGE():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR CORRECT AGE. ",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms5():
                           qa=mycon.cursor()
                           ug="update coders set AGE='{0}' where USERNAME='{1}'AND PASSWORD='{2}'".format(eis1.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms5)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15))   
                   
                   age=Button(mm11,text="AGE",bg="dark green",fg="yellow",width=15,command=AGE)
                   age.place(x=200,y=310)
                   age.config(font=("Cambridge",15))
                   def PIN():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR NEW PIN",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms6():
                           qa=mycon.cursor()
                           ug="update coders set PINNO='{0}' where PASSWORD='{1}'".format(eis1.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms6)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15)) 
                   
                   pin=Button(mm11,text="PIN",bg="dark green",fg="yellow",width=15,command=PIN)
                   pin.place(x=30,y=350)
                   pin.config(font=("Cambridge",15))
                   def SEG():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x500+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR CORRECT GENDER.",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       global ty
                       ty=StringVar()
                       re=Radiobutton(mm551,text="male",value="male",variable=ty)
                       re.place(x=300,y=160)
                       re.config(font=("helvetica",20))
                       re=Radiobutton(mm551,text="female",value="female",variable=ty)
                       re.place(x=400,y=160)
                       re.config(font=("helvetica",20))
                       
                       def dbms7():
                           qa=mycon.cursor()
                           ug="update coders set GENDERSEX='{}' where USERNAME='{}'AND PASSWORD='{}'".format(ty.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms7)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15))
                       
                   gs=Button(mm11,text="GENDER",bg="dark green",fg="yellow",width=15,command=SEG)
                   gs.place(x=200,y=390)
                   gs.config(font=("Cambridge",15))
                   def RAMU():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR CORRECT AADHAR NO.",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms8():
                           qa=mycon.cursor()
                           ug="update coders set AADHARNO='{0}' where USERNAME='{1}'AND PASSWORD='{2}'".format(eis1.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms8)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15))        
                   
                   aad=Button(mm11,text="AADHAR",bg="dark green",fg="yellow",width=15,command=RAMU)
                   aad.place(x=30,y=430)
                   aad.config(font=("Cambridge",15))
                   def sword():
                       m51=Tk()
                       m51.title(" CHANGE SHELL")
                       m51.geometry("500x400+550+200")
                       mm551=Canvas(m51,bg="SeaGreen1",width=1366,height=768)
                       mm551.place(x=0,y=0)
                       dis1=Label(mm551,text="WELCOME COUSTOMER",bg="SeaGreen1",fg="red",width=20)
                       dis1.place(x=10,y=10)
                       dis1.config(font=("Algerian",25))
                       dis13=Label(mm551,text="ENTER YOUR NEW PASSWORD.",bg="SeaGreen1",fg="blue",)
                       dis13.place(x=50,y=120)
                       dis13.config(font=("Algerian",15))
                       eis1=Entry(mm551,width=30,bg="medium spring green",bd=6,fg="red")
                       eis1.place(x=30,y=160)
                       eis1.config(font=("Helvetica",15))
                       def dbms9():
                           qa=mycon.cursor()
                           ug="update coders set PASSWORD='{0}' where USERNAME='{1}'AND PASSWORD='{2}'".format(eis1.get(),c7.get(),c4.get())
                           qa.execute(ug)
                           mycon.commit()
                           ans=messagebox.showinfo("success","SUCCESFULLY CREATED")
                           
                       bis1=Button(mm551,text="CHANGE",bg="OrangeRed2",fg="yellow",width=15,height=1,command=dbms9)
                       bis1.place(x=50,y=200)
                       bis1.config(font=("Cambridge",15))
                               
                   
                   pas=Button(mm11,text="PASSWORD",bg="dark green",fg="yellow",width=15,command=sword)
                   pas.place(x=200,y=470)
                   pas.config(font=("Cambridge",15))

                   
               def ms():
                   txt=Tk()
                   txt.title("MINI STATEMENT")
                   scroll=Scrollbar(txt)
                   scroll.pack(side=RIGHT,fill=Y)
                   txt.geometry("1000x400+230+150")
                   txt1=Text(txt,width=1366,height=768,bg="yellow",fg="navy",font="courier",selectbackground="red",yscrollcommand=scroll.set)
                   scroll.config(command=txt1.yview)
                   dep="select * from {}{}6".format(c7.get(),c5.get())
                   qa.execute(dep)
                   dep1=qa.fetchall()

                   acc="select ACCNO from coders where USERNAME='{}'".format(c7.get())
                   qa.execute(acc)
                   acc1=qa.fetchone()
                   txt1.insert(INSERT,"USERNAME: {}...............ACCOUNT NO: {}\n".format(c7.get(),acc1[0]))
                   txt1.insert(INSERT,"|                                           |\n")
                   txt1.insert(INSERT,"|                                           |\n")
                   txt1.insert(INSERT,"    DATE         |    WITHDRAWL       |   DEPOSIT    |   BALANCE   \n")
                   txt1.insert(INSERT,"|-------------------------------------------------------------------|\n")
                   for h in dep1:
                       rp=h
                       txt1.insert(INSERT,"|  {}    ".format(rp[0]))
                       txt1.insert(INSERT,"|  {}      ".format(rp[1]))
                       txt1.insert(INSERT,"        |")
                       txt1.insert(INSERT,"    {}         ".format(rp[2]))
                       txt1.insert(INSERT,"|     {}     \n".format(rp[3]))
                       txt1.insert(INSERT,"|===================================================================|\n")
                   txt1.config(state="disabled")
                   txt1.pack()
                   txt.mainloop()
                       
               def bl():
                   dep="select * from {}{}5".format(c7.get(),c5.get())
                   qa.execute(dep)
                   dep1=qa.fetchall()
                   lk=len(dep1)
                   
                   for ik in dep1:           
                       up=dep1[lk-1]
                   m3=Tk()
                   m3.title("BALANCE ENQUIRY")
                   m3.geometry("1000x400+230+150")
                   mm=Canvas(m3,bg="light sea green",width=1366,height=768)
                   mm.place(x=0,y=0)
                   k2=Label(mm,text="MR.{} YOUR AVAILABLE BALANCE".format(c7.get()),bg="light sea green",fg="red",width=35)
                   k2.place(x=8,y=30)
                   k2.config(font=("Algerian",30))
                   kk2=Label(mm,text="RS::{}".format(up[0]),bg="light sea green",fg="red",width=20)
                   kk2.place(x=150,y=150)
                   kk2.config(font=("Algerian",45))
                   def bck1():
                       m3.destroy()
                   bk1=Button(mm,text="QUIT",bg="black",fg="yellow",command=bck1)
                   bk1.place(x=450,y=300)
                   bk1.config(font=("Cambridge",25))                   
                   
               def dp():
                   global m2   
                   m2=Tk()
                   m2.title("DEPOSIT SHELL")
                   m2.geometry("1000x600+230+70")
                   mm=Canvas(m2,bg="light sea green",width=1366,height=768)
                   mm.place(x=0,y=0)
                   k2=Label(m2,text="ENTER THE AMOUNT",bg="blue",fg="yellow",width=20)
                   k2.place(x=300,y=30)
                   k2.config(font=("Algerian",25))
                   en=Entry(m2,bg="yellow2",fg="red",width=15,bd=5)
                   en.place(x=355,y=95)
                   en.config(font=("Algerian",25))
                   def bck2():
                       m2.destroy()
                   bk2=Button(mm,text="QUIT",bg="black",fg="yellow",command=bck2)
                   bk2.place(x=10,y=20)
                   bk2.config(font=("Cambridge",25))
                   def dp1():
                       cd=en.get()
                       global wd
                       wd=cd
                       
                       yu=Canvas(m2,width=1366,height=250,bg="dark olive green")
                       yu.place(x=0,y=230)
                       fu=Label(yu,text="ENTER THE PIN:",bg="red2",fg="black",width=20)
                       fu.place(x=300,y=20)
                       fu.config(font=("Algerian",25))
                       hu=Entry(yu,show="*",width=15,bg="yellow2",fg="red",bd=5)
                       hu.place(x=355,y=85)
                       hu.config(font=("Algerian",25))
                       def pin3():
                           er1="select PINNO from coders where USERNAME='{}'".format(c7.get())
                           qa.execute(er1)
                           s2=qa.fetchone()
                           mh=s2[0]
                           if(hu.get()==mh):
                              dp2()
                           else:
                               pin()
                       def dp2():
                           m2.destroy()
                           m21=Tk()
                           m21.title("DEPOSIT SHELL")
                           m21.geometry("800x400+350+180")
                           m8=Canvas(m21,width=1366,height=768,bg="blue")
                           m8.place(x=0,y=0)
                           k=Label(m8,text="PLEASE COME AGAIN !!!",bg="blue",fg="yellow",width=40)
                           k.place(x=0,y=0)
                           k.config(font=("Algerian",25))
                           k=Label(m8,text="AVAILABLE BALANCE::-",bg="black",fg="yellow",width=40)
                           k.place(x=40,y=50)
                           k.config(font=("Algerian",20))
                           def bck():
                               dp()
                               m21.destroy()
                           bk=Button(m8,text="BACK",bg="black",fg="yellow",command=bck)
                           bk.place(x=330,y=200)
                           bk.config(font=("Cambridge",25))


                           we="select BALANCE from {}{}4".format(c7.get(),c5.get())
                           qa.execute(we)
                           h2=qa.fetchall()

                           we1="select * from {}{}3".format(c7.get(),c5.get())
                           qa.execute(we1)
                           h22=qa.fetchall()
                           x=len(h22)

                           dep="select * from {}{}5".format(c7.get(),c5.get())
                           qa.execute(dep)
                           dep1=qa.fetchall()
                           lk=len(dep1)

                           
                           if len(h2)==1:
                              i=h2[0]
                              for ik in dep1:
                                  up=dep1[lk-1]
                                  var1=int(up[0])+int(wd)
                              if var1<1000:
                                t1()
                              else: 
                                  tr1="insert into {}{}3(CURDATE,DEPOSIT,AMOUNTAVAL)values('{}','{}','{}')".format(c7.get(),c5.get(),today,wd,var1)             
                                  tr3="insert into {}{}4(BALANCE)values('{}')".format(c7.get(),c5.get(),var1)
                                  tr4="insert into {}{}5(AMOUNT)values('{}')".format(c7.get(),c5.get(),var1)
                                  tr5="insert into {}{}6(DATE,WITHDRAWL,DEPOSIT,AMOUNTAVAL)values('{}','{}','{}','{}')".format(c7.get(),c5.get(),today,0,wd,var1)
                                  qa.execute(tr1)
                                 
                                  qa.execute(tr3)
                                  qa.execute(tr4)
                                  qa.execute(tr5)
                                  mycon.commit()
                                  ss7=Label(m8,text="Rs.{}".format(var1),bg="red",fg="white")
                                  ss7.place(x=325,y=100)
                                  ss7.config(font=("Algerian",20))
                           elif (len(h2)==len(h22)+1): 
                                for i in h2:
                                    for j in h22:
                                        ios=j[2]
                                        pop=int(ios)
                                        o=i
                                        oo=int(o[0])
                                if oo==pop:
                                   for ik in dep1:
                                       up=dep1[lk-1]
                                       var1=int(up[0])+int(wd)
                                   if var1<1000:
                                      t1()
                                   else:
                                       tr7="insert into {}{}3(CURDATE,DEPOSIT,AMOUNTAVAL)values('{}','{}','{}')".format(c7.get(),c5.get(),today,wd,var1)
                                       tr8="insert into {}{}4(BALANCE)values('{}')".format(c7.get(),c5.get(),var1)
                                       tr9="insert into {}{}5(AMOUNT)values('{}')".format(c7.get(),c5.get(),var1)
                                       tr10="insert into {}{}6(DATE,WITHDRAWL,DEPOSIT,AMOUNTAVAL)values('{}','{}','{}','{}')".format(c7.get(),c5.get(),today,0,wd,var1)
                                           
                                       qa.execute(tr7)
                                       qa.execute(tr8)
                                       qa.execute(tr9)
                                       qa.execute(tr10)
                                       mycon.commit()
                                       ss7=Label(m8,text="Rs.{}".format(var1),bg="red",fg="white")
                                       ss7.place(x=325,y=100)
                                       ss7.config(font=("Algerian",20))



                       
                       v1=Button(yu,text="PROCEED",bg="black",fg="yellow",command=pin3)
                       v1.place(x=440,y=150)
                       v1.config(font=("Cambridge",15))

                   
                   v=Button(mm,text="PROCEED",bg="black",fg="yellow",command=dp1)
                   v.place(x=445,y=160)
                   v.config(font=("Cambridge",15))                   

                   
               
               
               def wd():
                   a=Canvas(root,bg="OrangeRed2",width=800,height=240)
                   a.place(x=200,y=200)
                   global er
                   er=Entry(a,bd=5,width=25,bg="orange2")
                   er.place(x=200,y=60)
                   er.config(font=("Algerian",15))
                   def nw():
                       try:
                           c=er.get()
                           w=c
                       except:
                           print("successfull")
                       
                       d=Canvas(root,width=800,height=240,bg="SpringGreen3")
                       d.place(x=200,y=200)
                       f=Label(d,text="ENTER PIN NO.",bg="SpringGreen3",fg="red")
                       f.place(x=250,y=20)
                       f.config(font=("Algerian",35))
                       h=Entry(d,show="*",width=20,bg="RoyalBlue1")
                       h.place(x=250,y=80)
                       h.config(font=("Algerian",20))
                       se="select * from coders where USERNAME='{}'".format(c7.get())
                       qa.execute(se)
                       global t
                       t=qa.fetchone()
                       def nw11():
                           er="select PINNO from coders where USERNAME='{}'".format(c7.get())
                           qa.execute(er)
                           s=qa.fetchone()
                           mh=s[0]
                           if(h.get()==mh):
                              nw1()
                              d.destroy()
                           else:
                               pin()
                       def nw1():
                           m=Canvas(root,width=800,height=240,bg="blue")
                           m.place(x=200,y=200)
                           k=Label(m,text="PLEASE COLLECT THE MONEY FROM CASHIER!!!",bg="blue",fg="yellow",width=40)
                           k.place(x=0,y=0)
                           k.config(font=("Algerian",25))
                           k=Label(m,text="AVAILABLE BALANCE::-",bg="black",fg="yellow",width=40)
                           k.place(x=40,y=50)
                           k.config(font=("Algerian",20))
                           we="select ACCBALANCE from {}{}1".format(c7.get(),c5.get())
                           qa.execute(we)
                           h=qa.fetchall()

                           we1="select * from {}{}2".format(c7.get(),c5.get())
                           qa.execute(we1)
                           h1=qa.fetchall()
                           x=len(h)

                           wit="select * from {}{}5".format(c7.get(),c5.get())
                           qa.execute(wit)
                           wit1=qa.fetchall()
                           lk1=len(wit1)

                           
                           if len(h)==1:
                              i=h[0]
                              for ik1 in wit1:
                                  up1=wit1[lk1-1]
                                  var=int(up1[0])-int(w)
                              
                              if var<1000:
                                 t1()
                              else: 
                                   tr1="insert into {}{}2(SNO,CURDATE,ACCWITHDRAWL,AMOUNTAVAL)values('{}','{}','{}','{}')".format(c7.get(),c5.get(),x,today,w,var)

                                   tr2="insert into {}{}1(ACCBALANCE)values('{}')".format(c7.get(),c5.get(),var)
                                   tr3="insert into {}{}5(AMOUNT)values('{}')".format(c7.get(),c5.get(),var)
                                   tr4="insert into {}{}6(DATE,WITHDRAWL,DEPOSIT,AMOUNTAVAL)values('{}','{}','{}','{}')".format(c7.get(),c5.get(),today,w,0,var)  
                                   qa.execute(tr1)
                                   qa.execute(tr2)
                                   qa.execute(tr3)
                                   qa.execute(tr4)
                                   mycon.commit()
                                   ss1=Label(m,text="Rs.{}".format(var),bg="red",fg="white")
                                   ss1.place(x=325,y=100)
                                   ss1.config(font=("Algerian",20))
                                   a.destroy()
                                   def bck6():
                                       m.destroy()
                                       nw()
                                   bk6=Button(m,text="BACK",bg="black",fg="yellow",command=bck6)
                                   bk6.place(x=330,y=200)
                                   bk6.config(font=("Helvetica",15)) 




                                       
                           elif (len(h)==len(h1)+1):
                               for i in h:
                                   for j in h1:
                                       ios=j[3]
                                       pop=int(ios)
                                       o=i
                                       oo=int(o[0])
                               try:
                                   if oo==pop:
                                      for ik1 in wit1:
                                          up1=wit1[lk1-1]
                                          var=int(up1[0])-int(w)
                                      if var<1000:
                                         t1()
                                      else:
                                           tr1="insert into {}{}2(SNO,CURDATE,ACCWITHDRAWL,AMOUNTAVAL)values('{}','{}','{}','{}')".format(c7.get(),c5.get(),x,today,w,var)
                                           y=x+1
                                           tr2="insert into {}{}1(ACCBALANCE)values('{}')".format(c7.get(),c5.get(),var)
                                           tr3="insert into {}{}5(AMOUNT)values('{}')".format(c7.get(),c5.get(),var)
                                           tr4="insert into {}{}6(DATE,WITHDRAWL,DEPOSIT,AMOUNTAVAL)values('{}','{}','{}','{}')".format(c7.get(),c5.get(),today,w,0,var)
                                           qa.execute(tr1)
                                           qa.execute(tr2)
                                           qa.execute(tr3)
                                           qa.execute(tr4)
                                           
                                           mycon.commit()
                                           ss=Label(m,text="Rs.{}".format(var),bg="red",fg="white")
                                           ss.place(x=325,y=100)
                                           ss.config(font=("Algerian",20))
                                           a.destroy()
                                           def bck5():
                                               m.destroy()
                                               wd()
                                           bk5=Button(m,text="BACK",bg="black",fg="yellow",command=bck5)
                                           bk5.place(x=330,y=200)
                                           bk5.config(font=("Helvetica",15))                  
                               except:
                                   popup()
             




                       v=Button(d,text="PROCEED",bg="red",fg="black",command=nw11)
                       v.place(x=250,y=140)
                       v.config(font=("Cambridge",15))
                       def bck4():
                           d.destroy()
                       bk4=Button(d,text="BACK",bg="black",fg="yellow",command=bck4)
                       bk4.place(x=10,y=10)
                       bk4.config(font=("Helvetica",15))                       

                       
                       
                      
 

                   k=Label(a,text="AMOUNT TO BE WITHDRAWN:",bg="OrangeRed2",fg="OliveDrab1",width=23)
                   k.place(x=200,y=10)
                   k.config(font=("Lucida Console",20))
                   v=Button(a,text="PROCEED",bg="gray31",fg="yellow",command=nw)
                   v.place(x=200,y=110)
                   v.config(font=("Helvetica",15))
                   def bck3():
                       a.destroy()
                   bk3=Button(a,text="QUIT",bg="black",fg="yellow",command=bck3)
                   bk3.place(x=10,y=10)
                   bk3.config(font=("Cambridge",15))

               f=Button(root,text="WITHDRAWL",bg="red",width=15,command=wd)
               f.place(x=10,y=200)
               f.config(font=("Courier",15))
               g=Button(root,text="DEPOSIT",bg="red",width=15,command=dp)
               g.place(x=10,y=270)
               g.config(font=("Courier",15))
               d=Button(root,text="BALANCE.ENQUIRY",bg="red",width=15,command=bl)
               d.place(x=10,y=330)
               d.config(font=("Courier",15))
               p=Button(root,text="MINI STATEMENT",bg="red",width=15,command=ms)
               p.place(x=10,y=400)
               p.config(font=("Courier",15)) 
               p1=Button(root,text="EDIT INFO",bg="red",width=15,command=ed)
               p1.place(x=10,y=450)
               p1.config(font=("Courier",15)) 












               
           for r in u:
               y=list(r)
               u=y[0]
               io=u.upper()
               pii=c7.get()
               iip=pii.upper()
               w=y[1]
               q=y[2]
               if iip==io and q==c4.get()and w==c5.get():
                  mb9()
                  u=0
               
               
        else:
             nm()
                









    
    root=Tk()
    root.title("ENTER DETAILS: ")
    root.geometry("250x250+1000+250")
    ti=Frame(root,bg="black",width=1366,height=766)
    ti.place(x=0,y=0)
    global c7
    c7=Entry(root,width=20,bg="OliveDrab1")
    c7.place(x=70,y=40)
    global c4
    c4=Entry(root,show="*",bg="OliveDrab1")
    c4.place(x=70,y=120)
    global c5
    c5=Entry(root,bg="OliveDrab1")
    c5.place(x=70,y=170)
 

    s=Label(root,text="USERNAME",bg="black",fg="yellow")
    s.place(x=60,y=10)

    q=Label(root,text="PASSWORD",bg="black",fg="yellow")
    q.place(x=60,y=100)
    k=Label(root,text="PHONE NUMBER",bg="black",fg="yellow")
    k.place(x=60,y=140)
    
    d=Button(root,text="CONFIRM",bg="violet",command=mb8)
    d.place(x=100,y=200)
     
def NU():
    pi=Label(root,text="PLEASE ENTER USERNAME",bg="green yellow",fg="red")
    pp=Label(root,text="WITHOUT SPECIAL CHARACTERS AND SPACE ",bg="green yellow",fg="red")    
    pi.place(x=10,y=80)
    pp.place(x=10,y=120)
    pi.config(font=("helvetica",10))
    pp.config(font=("helvetica",10))
    p=Canvas(root,bg="blue4",width=500,height=500)
    p.place(x=0,y=150)
    b5=p.create_line(0,0,0,500,fill="black",width=15)
    b6=p.create_line(0,0,500,0,fill="black",width=15)
    b7=p.create_line(0,500,500,500,fill="black",width=15)
    b8=p.create_line(500,0,500,500,fill="black",width=15)
    be=p.create_line(0,440,500,440,fill="red",width=10,dash=(4,2))
    
    
    def user():
        global e
        e=Entry(root,width=15,bg="OliveDrab1")
        e.place(x=250,y=160)
        e.config(font=("helvetica",20))
    def con():
        w=p1.get()
        t=p2.get()

        if w!=t:
           mb1()
        else:
           mb2()
                
        
    def user1():
        global p1
        global p2
        global w
        global t
        global f

        def mn(*args):
            value=f.get()
            if len(value)>10:
                f.set(value[:10])

        f=StringVar()
        f.trace('w',mn)
        
        p1=Entry(root,width=15,textvariable=f,bg="OliveDrab1")
        p1.place(x=250,y=200)
        p1.config(font=("helvetica",20))
        def my(*args):
            value=dw.get()
            if len(value)>10:
                dw.set(value[:10])

        dw=StringVar()
        dw.trace('w',my)
        p2=Entry(root,width=15,textvariable=dw,bg="OliveDrab1")
        p2.place(x=250,y=240)
        p2.config(font=("helvetica",20))
        
        w=p1.get()
        t=p2.get()
            
       
        
        def con1():
            w=p1.get()
            l1=len(w)
            if p1.get()!=p2.get():
               mb1()
            elif l1!=10:
                nb()
            elif w.isdigit()==False:
                nb1()
            else:
               mb2()
               ty.destroy()
                
        ty=Button(root,text="CONFIRM 100%",command=con1,bg="orange",fg="blue")
        ty.place(x=505,y=220)#place in canvas
        ty.config(font=("Courier",15))
    def user3():
        global p3
        p3=Entry(root,width=15,bg="OliveDrab1")
        p3.place(x=250,y=280)
        p3.config(font=("helvetica",20))
        
        
    def user4():
        global p4
        def my2(*args):
            value=dw1.get()
            if len(value)>10:
                dw1.set(value[:10])

        dw1=StringVar()
        dw1.trace('w',my2)
        p4=Entry(root,width=15,textvariable=dw1,bg="OliveDrab1")
        p4.place(x=250,y=320)
        p4.config(font=("helvetica",20))
        c=p4.get()
        def ckp():
            global v
            global k
            global m
            c=p4.get()
            v=c.upper()
            try:
               k=v[0]
               u=v[1]
               r=v[2]
               t=v[3]
               w=v[4]
               j=v[9]
               k=v[0]+v[1]+v[2]+v[3]+v[4]+v[9]
               m=v[5]+v[6]+v[7]+v[8]
               if k.isalpha():
                  if u.isalpha():
                     if r.isalpha():
                        if t.isalpha():
                           if w.isalpha():
                              if j.isalpha():
                                 if k.isalpha() and m.isdigit():
                                    mb2()
                                    t5.destroy()
                                 else:
                                     mb0()
                              else:
                                  mb0()
                           else:
                                mb0()
                        else:
                             mb0()
                     else:
                          mb0()
                  else:
                       mb0()
               else:
                     mb0()
            except:
                 mb0()




        t5=Button(root,text="100% CONFIRM",command=ckp,bg="orange",fg="blue")
        t5.place(x=505,y=320)
        t5.config(font=("Courier",15))

        
    def user5():
        global p5
        def my2(*args):
            value=dw2.get()
            if len(value)>12:
                dw2.set(value[:12])

        dw2=StringVar()
        dw2.trace('w',my2)
        p5=Entry(root,width=15,textvariable=dw2,bg="OliveDrab1")
        p5.place(x=250,y=360)
        p5.config(font=("helvetica",20))
        
    def user6():
        global p6
        def my6(*args):
            value=dw6.get()
            if len(value)>2:
                dw6.set(value[:2])

        dw6=StringVar()
        dw6.trace('w',my6)
        p6=Entry(root,width=15,textvariable=dw6,bg="OliveDrab1")
        p6.place(x=250,y=400)
        p6.config(font=("helvetica",20))
    def user7():
        global p7
        def my5(*args):
            value=dw5.get()
            if len(value)>1:
                dw5.set(value[:1])

        dw5=StringVar()
        dw5.trace('w',my5)
        global j
        j=StringVar()
        p7=Radiobutton(root,text="male",value="male",variable=j,bg="blue4",fg="OrangeRed")
        p7.place(x=250,y=440)
        p7.config(font=("helvetica",20))
        p7=Radiobutton(root,text="female",value="female",variable=j,bg="blue4",fg="OrangeRed")
        p7.place(x=350,y=440)
        p7.config(font=("helvetica",20))
        global op
        op=Label(root,text="currently both buttons are selected!!! select any one",bg="red")
        op.place(x=500,y=440)
        op.config(font=("helvetica",20))
        
    def user8():
        op.destroy()
        global p8
        def my9(*args):
            value=dw9.get()
            if len(value)>8:
                dw9.set(value[:8])

        dw9=StringVar()
        dw9.trace('w',my9)
        p8=Entry(root,width=15,textvariable=dw9,bg="OliveDrab1")
        p8.place(x=250,y=480)
        p8.config(font=("helvetica",20))
    def user9():
        global p9
        p9=Entry(root,show="*",width=15,bg="OliveDrab1")
        p9.place(x=250,y=520)
        p9.config(font=("helvetica",20))

    def user10():
        global p10
        p10=Entry(root,width=15,bg="OliveDrab1")
        p10.place(x=250,y=560)
        p10.config(font=("helvetica",20))
        
       
    def user11():
        try:
            ee=e.get()
            p11=p1.get()
            p22=p2.get()
            p33=p3.get()
            p44=p4.get()
            p55=p5.get()
            p66=p6.get()
            p77=j.get()
            p88=p8.get()
            p99=p9.get
            p00=p10.get()
            if ee is not None:
                if p11 is not None:
                   if p22 is not None:
                      if p33 is not None:
                         if p44 is not None:
                            if p55 is not None:
                               if p66 is not None:
                                  if p77 is not None:
                                     if p88 is not None:
                                        if p99 is not None:
                                           if p00 is not None:
                                              if p5.get().isdigit():
                                                 if p1.get()==p2.get():
                                                    if j.get().isalpha():
                                                       if p8.get().isdigit():
                                                          if p10.get().isdigit():
                                                             if p6.get().isdigit():
                                                                if e.get().isalpha():
                                                                   if p3.get().isalpha():
                                                                      mb3()
                                                                   else:
                                                                       nm2()
                                                                else:
                                                                    nm3()
                                                             else:
                                                                 nm4()
                                                          else:
                                                              nm5()
                                                       else:
                                                           nm6()
                                                    else:
                                                        nm7()
                                                 else:
                                                     nm8()
                                              else:
                                                  nm9()
                                           else:
                                               nm1()
                                        else:
                                            nm1()
                                     else:
                                          nm1()
                                  else: 
                                     nm1()
                               else:
                                    nm1()
                            else:
                                 nm1()
                         else:
                              nm1()
                      else: 
                           nm1()
                   else:
                        nm1()
                else:
                    nm1()
            else:
                 nm1()
        except:
              nm1()
        

        
        
      
        
    
        
    s=Button(root,text="USERNAME",width=18,bg="cyan",command=user)
    s.place(x=10,y=160)
    s.config(font=("Courier",15))
    
    q=Button(root,text="PHONE.No ",width=18,bg="cyan",command=user1)
    q.place(x=10,y=200)
    q.config(font=("Courier",15))

    q1=Button(root,text="CONFIRM PHONE NO ",width=18,bg="cyan")
    q1.place(x=10,y=240)
    q1.config(font=("Courier",15))

    q2=Button(root,text="ADDRESS: ",width=18,bg="cyan",command=user3)
    q2.place(x=10,y=280)
    q2.config(font=("Courier",15))

    q3=Button(root,text="PAN.NO: ",width=18,bg="cyan",command=user4)
    q3.place(x=10,y=320)
    q3.config(font=("Courier",15))

    q4=Button(root,text="AADHAR.NO: ",width=18,bg="cyan",command=user5)
    q4.place(x=10,y=360)
    q4.config(font=("Courier",15))

    q5=Button(root,text="AGE: ",width=18,bg="cyan",command=user6)
    q5.place(x=10,y=400)
    q5.config(font=("Courier",15))  
  
    q6=Button(root,text="SEX/GENDER: ",width=18,bg="cyan",command=user7)
    q6.place(x=10,y=440)
    q6.config(font=("Courier",15)) 

    q7=Button(root,text="D.O.B: ",width=18,bg="cyan",command=user8)
    q7.place(x=10,y=480)
    q7.config(font=("Courier",15)) 

    q8=Button(root,text="SET PIN:- ",width=18,bg="cyan",command=user9)
    q8.place(x=10,y=520)
    q8.config(font=("Courier",15)) 

    q10=Button(root,text="INITIAL DEPOSIT ",bg="cyan",width=18,command=user10)
    q10.place(x=10,y=560)
    q10.config(font=("Courier",15))           

    
    q11=Button(root,text="SAVE",width=20,bg="cyan",command=user11)
    q11.place(x=250,y=600)
    q11.config(font=("Helvetica",15)) 


    


r=Canvas(root,bg="saddle brown",width=1366,height=768)
r.place(x=0,y=0)
image=my_image=PhotoImage(file='C:\\Users\\M PARTH\\Desktop\\code-wallpaper-11.gif')
r.create_image(0, 0, anchor = NW, image=my_image)



q=Canvas(root,bg="black",width=900,height=150)
q.place(x=230,y=0)
a1=q.create_line(0,0,0,75,fill="green4",width=35)
a2=q.create_line(0,75,320,75,fill="black",width=15)
a3=q.create_line(313,75,313,152,fill="black",width=15)
a4=q.create_line(307,145,658,145,fill="green2",width=5,dash=(4,2))
a4=q.create_line(307,135,658,135,fill="green2",width=5,dash=(4,2))
a5=q.create_line(658,152,658,50,fill="black",width=25)
a6=q.create_line(658,72,900,72,fill="black",width=15)
a7=q.create_line(880,72,880,0,fill="green4",width=50)
a8=q.create_line(20,95,885,95,fill="maroon",width=10,dash=(2,2,2))
a9=q.create_line(20,80,885,80,fill="NavajoWhite4",width=5,dash=(4,2))
a0=q.create_line(20,70,885,70,fill="lawn green",width=5,dash=(4,2))





d=Label(root,text="WELCOME TO CODER'S BANK",bg="black",fg="green yellow")
d.config(font=("Helvetica",44))
d.place(x=250,y=0)
l=Button(root,text="EXISTING CUSTOMER:-",bg="cyan2",width=30,command=EU,fg="deep pink")
l.place(x=775,y=110)
l.config(font=("helvetica",15))
u=Button(root,text="NEW CUSTOMER:-",bg="cyan2",width=30,command=NU,fg="deep pink")
u.place(x=250,y=110)
u.config(font=("helvetica",15))


root.mainloop()
