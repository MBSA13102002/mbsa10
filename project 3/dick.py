from tkinter import *
from tkinter.ttk import Progressbar
import time
import os
from tkinter import messagebox as m



root=Tk()
root.geometry("1366x768")
root.title("PLASMA ZONE")
s=Canvas(root,bg="white",width=1366,height=690)
s.place(x=0,y=0)
global a1
global e1
######################################################### MESSAGE BOX
def ee():
    k=m.showwarning("WARNING","PLEASE FILL THE REQUIRED DETAILS")
def mw():
    k1=m.showwarning("WARNING!!!!!","MOBILE NUMBER REQUIRED")
def adw():
    k2=m.showwarning("WARNING!!!!!","PLEASE GIVE YOUR ADDRESS")
def dobw():
    k3=m.showwarning("WARNING!!!!!","D.O.B...MISSING")
def suw():
    k4=m.showwarning("WARNING!!!!!","PLEASE ENTER YOUR SUBJECT TO TEACH")
def emw():
    k5=m.showwaning("WARNING!!!!!","E-MAIL REQUIRED")
def pw():
    k6=m.showwarning("WARNING!!!!!","PASSWORD REQUIRED")
def cpw():
    k7=m.showwarning("WARNING!!!!!","MUST CONFIRM PASSWORD")
def qw():
    k8=m.showwarning("WARNING!!!!!","PLEASE GIVE YOUR QUALIFICATION")
def agw():
    k8=m.showwarning("WARNING!!!!!","PLEASE GIVE YOUR AGE")
###################################################################
def pro():
    def details(name,age,sub,mobno,passwd,add,dob,qual):
        p=open("plasma.txt",'a')    
        p.write('\n--------------------------------------------------------------\n')
        p.write('NAME:-'+ name.upper()+'\n')  
        p.write('AGE:-'+ age.upper()+'\n')
        p.write('SUBJECT:-'+ sub.upper()+'\n')
        p.write('MOB.NO:-'+ mobno.upper()+'\n')
        p.write('PASSWORD:-'+ passwd.upper()+'\n')
        p.write('ADDRESS:-'+ add.upper()+'\n')
        p.write('D.O.B:-'+ dob.upper()+'\n')
        p.write('QUALIFICATIONS:-'+ qual.upper()+'\n')
        p.write('\n--------------------------------------------------------------\n')
        p.close()
    #p=Progressbar(root,orient=HORIZONTAL,length=800,mode='determinate')
    #p.place(x=400,y=600)
    #p['value']=10
    #time.sleep(1)
    #root.update_idletasks()
    #p['value']=30
    #root.update_idletasks()
    #time.sleep(1)
    #p['value']=40
    #root.update_idletasks()
    #time.sleep(1)
    #p['value']=50
    #root.update_idletasks()
    #time.sleep(1)
    #p['value']=100
    #root.update_idletasks()
    #time.sleep(1)
    root.destroy()
    root1=Tk()
    root2=Toplevel(root1)
    root1.title("PLASMA'Z--THE LEARNING CAFE")
    root1.geometry("1366x768")
    mc=Canvas(root1,bg="white",width=1366,height=690)
    mc.place(x=0,y=0)
    my=PhotoImage(file='C:\\Users\\MUSTAFA\\Desktop\\bg.png')
    mc.create_image(0, 0, anchor = NW, image=my)

    
    sc1=Canvas(mc,bg="blue",width=200,height=200)
    sc1.place(x=250,y=100)
    my_image1=PhotoImage(file='C:\\Users\\MUSTAFA\\Desktop\\tc.png')
    sc1.create_image(0, 0, anchor = NW, image=my_image1)
    sc2=Canvas(mc,bg="red",width=200,height=200)
    sc2.place(x=900,y=100)
    my_image2=PhotoImage(file='C:\\Users\\MUSTAFA\\Desktop\\sc.png')
    sc2.create_image(0, 0, anchor = NW, image=my_image2)
    root2.destroy()
    #functions==========================================
    def snt():
        pass
    def spt():
        root1.title("TEACHER'S DETAILS")
        dot=Canvas(root1,bg="white",width=1366,height=690)
        dot.place(x=0,y=0)
        my=PhotoImage(file='C:\\Users\\MUSTAFA\\Desktop\\bg.png')
        dot.create_image(0, 0, anchor = NW, image=my)

        
        

        #enter details label======================================================
        lb1=Label(dot,text="*  ENTER YOUR DETAILS  *",width=30,bg="cyan",fg="red")
        lb1.place(x=390,y=0)
        lb1.config(font=("helvetica",25))
        def back():
            dot.destroy()
            root1.title("win2")
        bck=Button(dot,text='BACK',command=back,bg='cyan',width=10,fg='red')
        bck.place(x=40,y=30)
        bck.config(font=('Courier',15))
        
        #-----------------------------
        global b_1
        def b_1():
            def mb(*args):
                value=a1.get()
                if len(value)>10:
                    a1.set(value[:10])
                if value.isdigit()==False and value!='':
                    ans3=m.showwarning("WARNING","WRONG INPUT")
                    
            global a1
            a1=StringVar()
            a1.trace("w",mb)
            global e1
            e1=Entry(dot,width=15,textvariable=a1,bg="OliveDrab1")
            e1.bind("<Return>",b_2)
            e1.place(x=335,y=140)
            e1.config(font=("helvetica",28))
            e1.focus()
        b1=Button(dot,text='MOBILE.NO',command=b_1,bg='cyan',width=17,fg='red')
        b1.place(x=60,y=140)
        b1.config(font=('Courier',18))
        
        
        #-----------------------------
        global b_2
        def b_2(x=0):
            global b
            def ad(*args):
                value=b.get()
                if len(value)>50:
                    b.set(value[:50])                
                if value.isalnum()==False and value!='' and value.isspace()==True:
                    ans3=m.showwarning("WARNING","WRONG INPUT")
                    
                
                
                
            b=StringVar()
            b.trace('w',ad)
            global e2
            e2=Entry(dot,width=15,textvariable=b,bg="OliveDrab1")
            e2.bind("<Return>",b_3)
            e2.place(x=335,y=230)
            e2.config(font=("helvetica",28))
            e2.focus()
        b2=Button(dot,text='ADDRESS',command=b_2,bg='cyan',width=17,fg='red')
        b2.place(x=60,y=230)
        b2.config(font=('Courier',18))
        
        #------------------------------
        global b_3
        def b_3(x=0):
            def dob(*args):
                value1=c.get()
                if len(value1)>8:
                    c.set(value1[:8])
                if value1.isdigit()==False and value1!='':
                   ans3=m.showwarning("WARNING","WRONG INPUT")
                    
            global c
            c=StringVar()
            c.trace('w',dob)
            global e3
            e3=Entry(dot,width=15,textvariable=c,bg="OliveDrab1")
            e3.bind("<Return>",b_4)
            e3.place(x=335,y=320)
            e3.config(font=("helvetica",28))
            e3.focus()
        b3=Button(dot,text='D.O.B',command=b_3,bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
        b3.place(x=60,y=320)
        b3.config(font=('Courier',18))
        
        #-------------------------------
        global b_4
        def b_4(x=0):
            global d
            d=StringVar()
            global e4
            e4=Entry(dot,width=15,textvariable=d,bg="OliveDrab1")
            e4.bind("<Return>",b_9)
            e4.place(x=335,y=410)
            e4.config(font=("helvetica",28))
            e4.focus()
            
        b4=Button(dot,text='SUBJECT',command=b_4,bg='cyan',width=17,fg='red')
        b4.place(x=60,y=410)
        b4.config(font=('Courier',18))
        
        #-------------------------------
        global b_5
        def b_5(x=0):
            def email(*args):
                value=e.get()
                if len(value)>30:
                    e.set(value[:30])
            global e
            e=StringVar()
            e.trace('w',email)
            global e5
            e5=Entry(dot,width=15,textvariable=e,bg="Olivedrab1")
            e5.bind("<Return>",b_6)
            e5.place(x=970,y=140)
            e5.config(font=("helvetica",28))
            e5.focus()
        b5=Button(dot,text='E-MAIL',command=b_5,bg='cyan',width=17,fg='red')
        b5.place(x=700,y=140)
        b5.config(font=('Courier',18)) 
        
        #-------------------------------
        global b_6
        def b_6(x=0): 
            global f
            f=StringVar()
            global e6
            e6=Entry(dot,width=15,textvariable=f,bg="OliveDrab1",show='*')
            e6.bind("<Return>",b_7)
            e6.place(x=970,y=230)
            e6.config(font=("helvetica",28))
            e6.focus()
        b6=Button(dot,text='PASSWORD',command=b_6,bg='cyan',width=17,fg='red')
        b6.place(x=700,y=230)
        b6.config(font=('Courier',18))
        
        #-------------------------------
        global b_7
        def b_7(x=0):
            value=f.get()
            if len(value)<8:
               ans3=m.showwarning("WARNING","LESS THAN 8 CHARATERS\n NOT ACCEPTED")
            else:
               global g
               g=StringVar()
               global e7
               e7=Entry(dot,width=15,textvariable=g,bg="OliveDrab1",show='*')
               e7.bind("<Return>",b_8)
               e7.place(x=970,y=320)
               e7.config(font=("helvetica",28))
               e7.focus()
        def ad():
            pass
        b7=Button(dot,text='CONFIRM PASSWORD',command=ad,bg='cyan',width=17,fg='red')
        b7.place(x=700,y=320)
        b7.config(font=('Courier',18))
        
        #-------------------------------
        global b_8
        def b_8(x=0):
            global h
            h=StringVar()
            global e8
            e8=Text(dot,width=45,height=4,wrap=WORD,bg="OliveDrab1",selectbackground='red')
            e8.bind("<Return>",b_10)
            e8.place(x=970,y=410)
            e8.focus()
    
        b8=Button(dot,text="QUALIFICATION",command=b_8,bg='cyan',width=17,fg='red')
        b8.place(x=700,y=410)
        b8.config(font=('Courier',18))
        ################################
        global b_9
        def b_9(x=0):
             global j
             j=StringVar()
             global e9
             e9=Entry(dot,width=15,textvariable=j,bg="OliveDrab1")
             e9.bind("<Return>",b_5)
             e9.place(x=335,y=500)
             e9.config(font=("helvetica",28))
             e9.focus()
            
            
        b9=Button(dot,text="NAME",command=b_9,bg='cyan',width=17,fg='red')
        b9.place(x=60,y=500)
        b9.config(font=('Courier',18))
        #=========================-=-=-=-=-=-=-
        global b_10
        def b_10(x=0):
            def ag(*args):
                value=k.get()
                if len(value)>2:
                    k.set(value[:2])
                if value.isdigit==False:
                    ask=m.showwarning("WARNING","INVALID INPUT")
            global k
            k=StringVar()
            k.trace('w',ag)
            global e10
            e10=Entry(dot,width=15,textvariable=k,bg="OliveDrab1")
            e10.place(x=970,y=500)
            e10.config(font=("helvetica",28))
            e10.focus()
    
        b10=Button(dot,text="AGE",command=b_10,bg='cyan',width=17,fg='red')
        b10.place(x=700,y=500)
        b10.config(font=('Courier',18))
        #=====-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=--==-=SAVE BUTTON
        global b_11
        def b_11():
            try:
                c1=e1.get()
                c2=e2.get()
                c3=e3.get()
                c4=e4.get()
                c5=e5.get()
                c6=e6.get()
                c7=e7.get()
                c8=e8.get(1.0,END)
                c9=e9.get()
                c10=e10.get()
                
                if c1 is not None:
                   if c2 is not None:
                      if c3 is not None:
                         if c4 is not None:
                            if c5 is not None:
                               if c6 is not None:
                                  if c7 is not None:
                                    if c8 is  not None:
                                       if c9 is not None:
                                          if c10 is not None:
                                              if c1.isdigit()==True:
                                                 if c2.isalnum()==True:
                                                    if c3.isdigit()==True:
                                                       if c4.isalpha()==True:
                                                          if c5.isalnum()==True:
                                                             if c6.isalnum()==True:
                                                                if c7.isalnum()==True:
                                                                   if c9.isalpha()==True:
                                                                      if c10.isdigit()==True:
                                                                         k=m.showinfo("CREATED SUCCESSFULLY","PROCEED")
                                                                      else:
                                                                         ee()
                                                                   else:
                                                                        agw() 
                                                                else:
                                                                    cpw()
                                                             else:
                                                                 pw()
                                                          else:
                                                              emw()
                                                       else:
                                                          suw()
                                                    else:
                                                        dobw()
                                                 else:
                                                     adw()
                                              else:
                                                  mw()
                                          else:
                                            ee()
                                       else:
                                        ee()
                                    else:
                                        ee()
                                  else:
                                    ee()
                               else:
                                ee()
                            else:
                                ee()
                         else:
                            ee()
                      else:
                        ee()
                   else:
                    ee()
                else:   
                   ee()
            except:
               ee()
                

        b11=Button(dot,text="SAVE",command=b_11,bg='cyan',width=14,fg='red')
        b11.place(x=450,y=600)
        b11.config(font=('Courier',18))
        root1.mainloop()
        
        
            
        

        
    def sns():
        pass
    def sps():
        pass
    #functions-----------------------------------------
    #label=======================================
    lb1=Label(root1,text="* TEACHER'S CORNER * ",width=30,bg="cyan",fg="red")
    lb1.place(x=65,y=20)
    lb1.config(font=("helvetica",25))
    lb2=Label(root1,text="* STUDENT'S CORNER * ",width=30,bg="cyan",fg="red")
    lb2.place(x=720,y=20)
    lb2.config(font=("helvetica",25))
    #label-------------------------------------------
    
    #button=========================================
    b1=Button(mc,text='LOG IN',command=snt,bg='cyan',fg='red',width=20)
    b1.place(x=235,y=335)
    b1.config(font=('Helvetica',15))
    b2=Button(mc,text='SIGN UP',command=spt,bg='cyan',fg='red',width=20)
    b2.place(x=235,y=380)
    b2.config(font=('Helvetica',15))
    b3=Button(mc,text='LOG IN',command=sns,bg='cyan',fg='red',width=20)
    b3.place(x=890,y=335)
    b3.config(font=('Helvetica',15))
    b4=Button(mc,text='SIGN UP',command=sps,bg='cyan',fg='red',width=20)
    b4.place(x=890,y=380)
    b4.config(font=('Helvetica',15))
   
    root1.mainloop()
    
s=Button(s,text='CLICK HERE',command=pro,bg='green')
s.place(x=600,y=250)
s.config(font=('Helvetica',15))
