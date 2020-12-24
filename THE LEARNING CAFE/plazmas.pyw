from tkinter import *
from tkinter.ttk import Progressbar
import time
import os
from tkinter import messagebox as m
global a1
global e1
################################################SINGN UP   TEACHER    START#####################################################################################################################################################################################################################
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
    k5=m.showwarning("WARNING!!!!!","E-MAIL REQUIRED")
def pw():
    k6=m.showwarning("WARNING!!!!!","PASSWORD REQUIRED")
def cpw():
    k7=m.showwarning("WARNING!!!!!","MUST CONFIRM PASSWORD")
def qw():
    k8=m.showwarning("WARNING!!!!!","PLEASE GIVE YOUR QUALIFICATION")
def agw():
    k8=m.showwarning("WARNING!!!!!","PLEASE GIVE YOUR AGE")
###########################################################



root=Tk()
root.title("PLASMA'Z")
root.geometry("1366x768")
root.title("PLASMA ZONE")
s=Canvas(root,bg="white",width=1366,height=690)
s.place(x=0,y=0)

def pro(x=0):
    def details(name,age,sub,mobno,passwd,add,date,month,year,qual):
        p=open("DOC\\plasma.txt",'a')    
        p.write('\n--------------------------------------------------------------\n')
        p.write('NAME:-'+ name.upper()+'\n')  
        p.write('AGE:-'+ age.upper()+'\n')
        p.write('SUBJECT:-'+ sub.upper()+'\n')
        p.write('MOB.NO:-'+ mobno.upper()+'\n')
        p.write('PASSWORD:-'+ passwd.upper()+'\n')
        p.write('ADDRESS:-'+ add.upper()+'\n')
        p.write('D.O.B:-'+ date.upper()+month.upper()+year.upper()+'\n')
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
    my=PhotoImage(file='IMG\\pad1.gif')
    mc.create_image(0, 0, anchor = NW, image=my)
    

    
    sc1=Canvas(mc,bg="blue",width=200,height=200)
    sc1.place(x=250,y=100)
    my_image1=PhotoImage(file='IMG\\as3.png')
    sc1.create_image(0, 0, anchor = NW, image=my_image1)
    sc2=Canvas(mc,bg="red",width=200,height=200)
    sc2.place(x=900,y=100)
    my_image2=PhotoImage(file='IMG\\as2.png')
    sc2.create_image(0, 0, anchor = NW, image=my_image2)
    root2.destroy()
    #functions==========================================
    def snt(x=0):
        pass
    def spt(x=0):
        root1.title("TEACHER'S DETAILS")
        dot=Canvas(root1,bg="white",width=1366,height=690)
        dot.place(x=0,y=0)
        my=PhotoImage(file='IMG\\pad1.gif')
        dot.create_image(0, 0, anchor = NW, image=my)

        
        

        #enter details label======================================================
        lb1=Label(dot,text="*  ENTER YOUR DETAILS  *",width=30,bg="cyan",fg="red")
        lb1.place(x=390,y=0)
        lb1.config(font=("helvetica",25))
        def fd(x=0):
            b1.focus()
        def back(x=0):
            dot.destroy()
            root1.title("PLASMA'Z - THE LEARNING CAFE")
            b123.focus()
        bck=Button(dot,text='BACK',command=back,bg='cyan',width=10,fg='red')
        bck.place(x=40,y=30)
        bck.config(font=('Courier',15))
        bck.focus()
        bck.bind("<BackSpace>",back)
        bck.bind("<Down>",fd)
        
        
        #-----------------------------
        global b_1
        def b__1(x=0):
            bck.focus()
        def b___1(x=0):
            b2.focus()
        def b____1(x=0):
            b5.focus()

        def b_1(x=0):
            def mb(*args):
                value=a1.get()
                if len(value)>10:
                    a1.set(value[:10])
                if value.isdigit()==False and value!='':
                    ans3=m.showwarning("WARNING","WRONG INPUT")
                if value=='':
                    e1.destroy()
                    
            global a1
            a1=StringVar()
            a1.trace("w",mb)
            global e1
            bck.focus()
            e1=Entry(dot,width=15,textvariable=a1,bg="OliveDrab1")
            e1.bind("<Return>",b_2)
            e1.place(x=335,y=140)
            e1.config(font=("helvetica",28))
            e1.focus()
            
        b1=Button(dot,text='MOBILE.NO',command=b_1,bg='cyan',width=17,fg='red')
        b1.place(x=60,y=140)
        b1.config(font=('Courier',18))
        b1.focus()
        b1.bind("<Return>",b_1)
        b1.bind("<Up>",b__1)
        b1.bind("<Down>",b___1)
        b1.bind("<Right>",b____1)
        
        
        #-----------------------------
        def b__2(x=0):
            b1.focus()
        def b___2(x=0):
            b3.focus()
        def b____2(x=0):
            b6.focus()

        global b_2
        def b_2(x=0):
            bck.focus()
            global b
            def ad(*args):
                value=b.get()
                if len(value)>50:
                    b.set(value[:50])                
                if value.isalnum()==False and value.isspace()==True and value!='':
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
        b2.focus()
        b2.bind("<Return>",b_2)
        b2.bind("<Up>",b__2)
        b2.bind("<Down>",b___2)
        b2.bind("<Right>",b____2)        
        #------------------------------
        def b__3(x=0):
            b2.focus()
        def b___3(x=0):
            b4.focus()
        def b____3(x=0):
            b7.focus()

        global b_3
        def b_3(x=0):
            bck.focus()
            global c
            c1=StringVar()         
            def c_2(*args):
                value=c2.get()
                if len(value)>2:
                    c2.set(value[:2])
                if value.isdigit()==False and value!='':
                    ans=m.showwarning("WARNING","WRONG INPUT")
                
            def month(x=0):
                def c_4(*args):
                    value=c11.get()
                    if len(value)>2:
                        c11.set(value[:2])
                    if value.isdigit()==False and value!='':
                        ans=m.showwarning("WARNING","WRONG INPUT")
                def year(x=0):
                    def c_5(*args):
                         value=c12.get()
                         if len(value)>4:
                            c12.set(value[:4])
                         if value.isdigit()==False and value!='':
                            ans=m.showwarning("WARNING","WRONG INPUT")
                    b4.destroy()
                    e11.destroy()
                    b5=Label(dot,text='YEAR',bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
                    b5.place(x=60,y=320)
                    b5.config(font=('Courier',18))
                    global c12
                    c12=StringVar()
                    c12.trace('w',c_5)
                    global e12
                    e12=Entry(dot,width=15,textvariable=c12,bg="OliveDrab1")
                    e12.place(x=335,y=320)
                    e12.config(font=("helvetica",28))
                    e12.focus()
                    e12.bind("<Return>",b_4)
                b2.destroy()
                e3.destroy()
                b4=Label(dot,text='MONTH',bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
                b4.place(x=60,y=320)
                b4.config(font=('Courier',18))
                global c11
                c11=StringVar()
                c11.trace('w',c_4)
                global e11
                e11=Entry(dot,width=15,textvariable=c11,bg="OliveDrab1")
                e11.place(x=335,y=320)
                e11.config(font=("helvetica",28))
                e11.focus()
                e11.bind("<Return>",year)
            b2=Label(dot,text='DATE',bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
            b2.place(x=60,y=320)
            b2.config(font=('Courier',18))
            global c2
            c2=StringVar()
            c2.trace('w',c_2)
            global e3
            e3=Entry(dot,width=15,textvariable=c2,bg="OliveDrab1")
            e3.place(x=335,y=320)
            e3.config(font=("helvetica",28))
            e3.focus()
            e3.bind("<Return>",month)
        b3=Button(dot,text='D.O.B',command=b_3,bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
        b3.place(x=60,y=320)
        b3.config(font=('Courier',18))
        b3.focus()
        b3.bind("<Return>",b_3)
        b3.bind("<Up>",b__3)
        b3.bind("<Down>",b___3)
        b3.bind("<Right>",b____3)
        #-------------==========


        
        #-------------------------------
        def b__4(x=0):
            b3.focus()
        def b___4(x=0):
            b9.focus()
        def b____4(x=0):
            b8.focus()

        global b_4
        def b_4(x=0):
            bck.focus()
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
        b4.focus()
        b4.bind("<Return>",b_4)
        b4.bind("<Up>",b__4)
        b4.bind("<Down>",b___4)
        b4.bind("<Right>",b____4)        
        #-------------------------------

        def b___5(x=0):
            b6.focus()
        def b____5(x=0):
            b1.focus()

        global b_5
        def b_5(x=0):
            bck.focus()
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
        b5.focus()
        b5.bind("<Return>",b_5)
        b5.bind("<Down>",b___5)
        b5.bind("<Left>",b____5)        
        #-------------------------------
        def b__6(x=0):
            b5.focus()
        def b___6(x=0):
            b7.focus()
        def b____6(x=0):
            b2.focus()

        global b_6
        def b_6(x=0):
            bck.focus()
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
        b6.focus()
        b6.bind("<Return>",b_6)
        b6.bind("<Up>",b__6)
        b6.bind("<Down>",b___6)
        b6.bind("<Left>",b____6)        
        #-------------------------------
        def b__7(x=0):
            b6.focus()
        def b___7(x=0):
            b8.focus()
        def b____7(x=0):
            b3.focus()

        global b_7
        def b_7(x=0):
            bck.focus()
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
        b1.focus()
        b7.bind("<Return>",b_7)
        b7.bind("<Up>",b__7)
        b7.bind("<Down>",b___7)
        b7.bind("<Left>",b____7)        
        #------------------------------
        def b__8(x=0):
            b7.focus()
        def b___8(x=0):
            b10.focus()
        def b____8(x=0):
            b4.focus()

        global b_8
        def b_8(x=0):
            bck.focus()
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
        b8.focus()
        b8.bind("<Return>",b_8)
        b8.bind("<Up>",b__8)
        b8.bind("<Down>",b___8)
        b8.bind("<Left>",b____8)
        ################################
        def b__9(x=0):
            b4.focus()
        def b___9(x=0):
            b11.focus()
        def b____9(x=0):
            b10.focus()

        global b_9
        def b_9(x=0):
             bck.focus()
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
        b9.focus()
        b9.bind("<Return>",b_9)
        b9.bind("<Up>",b__9)
        b9.bind("<Down>",b___9)
        b9.bind("<Right>",b____9)
        #=========================-=-=-=-=-=-=-
        def b__10(x=0):
            b8.focus()
        def b___10(x=0):
            b11.focus()
        def b____10(x=0):
            b9.focus()

        global b_10
        def b_10(x=0):
            bck.focus()
            def age(*args):
                value=k.get()
                if len(value)>2:
                    k.set(value[:2])
                if value.isdigit()==False and value!='':
                    ans4=m.showwarning("WARNING","WRONG INPUT")
                    
            global k
            k=StringVar()
            k.trace('w',age)
            global e10
            e10=Entry(dot,width=15,textvariable=k,bg="OliveDrab1")
            e10.place(x=970,y=500)
            e10.config(font=("helvetica",28))
            e10.focus()
    
        b10=Button(dot,text="AGE",command=b_10,bg='cyan',width=17,fg='red')
        b10.place(x=700,y=500)
        b10.config(font=('Courier',18))
        b10.focus()
        b10.bind("<Return>",b_10)
        b10.bind("<Up>",b__10)
        b10.bind("<Down>",b___10)
        b10.bind("<Left>",b____10)
        #=====-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=--==-=SAVE BUTTON
        global b_11
        def b_11():
            try:
                d1=e1.get()
                d2=e2.get()
                d3=c2.get()+c11.get()+c12.get()
                print(d3)
                d4=e4.get()
                d5=e5.get()
                d6=e6.get()
                d7=e7.get()
                d8=e8.get(1.0,END)
                d9=e9.get()
                d10="0"
                
                if d1 is not None:
                   if d2 is not None:
                      if d3 is not None:
                         if d4 is not None:
                            if d5 is not None:
                               if d6 is not None:
                                  if d7 is not None:
                                    if d8 is  not None:
                                       if d9 is not None:
                                          if d10 is not None:
                                              if d1.isdigit()==True:
                                                 if d2.isalnum()==True:
                                                    if d3.isdigit()==True:
                                                       if d4.isalpha()==True:
                                                          if d5.isalnum()==True:
                                                             if d6.isalnum()==True:
                                                                if d7.isalnum()==True:
                                                                   if d9.isalpha()==True:
                                                                      if d10.isdigit()==True:
                                                                         k=m.showinfo("CREATED SUCCESSFULLY","PROCEED")
                                                                         details(d9,d10,d4,d1,d6,d2,c2.get(),c11.get(),c12.get(),d8)
                                                                         ans=m.askquestion("PHOTO","DO YOU WANT TO UPLOAD YOUR PHOTO")
                                                                         if ans=='yes':
                                                                            dot2=Canvas(root1,bg="white",width=1366,height=690)
                                                                            dot2.place(x=0,y=0)
                                                                            my1=PhotoImage(file='IMG\\pad1.gif')
                                                                            dot2.create_image(0, 0, anchor = NW, image=my1)
                                                                        #========================================                
                                                                            dot1=Canvas(dot2,bg="blue",width=250,height=250)
                                                                            dot1.place(x=35,y=400)
                                                                            dot3=Canvas(dot2,bg="brown",width=250,height=250)
                                                                            dot3.place(x=35,y=50)
                                                                            my2=PhotoImage(file='IMG\\uy.gif')
                                                                            dot3.create_image(16, 10, anchor = NW, image=my2)
                                                                            def corona():  
                                                                                global g1
                                                                                g1=StringVar()
                                                                                global a2
                                                                                a2=Entry(dot2,width=15,textvariable=g1,bg="OliveDrab1")
                                                                                a2.bind("<Return>",r)
                                                                                a2.place(x=40,y=370)
                                                                                a2.config(font=('Courier',15))
                                                                                a2.focus()
                    
                                                                                global ab
                                                                                ab=Label(dot2,width=15,text='PHOTO NAME',bg="OliveDrab1")
                                                                                ab.place(x=40,y=340)
                                                                                ab.config(font=('Courier',15))
                                                                                root1.mainloop()
                                                                            def r(x=0):
                                                                                def bacteria():
                                                                                    ans6=m.showinfo("SUCCESS","ACCOUNT SUCCESSFULLY CREATED")
                                                                                    k=open("DOC\\plasma.txt",'a')
                                                                                    k.write("\n============================================\n")
                                                                                    k.write("IMAGE LINK OF "+d9)
                                                                                    k.write('IMG\\'+rt+'.gif')
                                                                                    k.write('\n--------------------------------------\n')
                                                                                    k.close()
                                                                                    corona()
                                                                                def virus():
                                                                                    bc6.destroy()
                                                                                    dot1.delete("all")
                                                                                    bc2.destroy()
                                                                                    corona()    
                                                                                bc2=Button(dot2,text='CHANGE PHOTO',command=virus,bg='cyan',width=15,fg='red')
                                                                                bc2.place(x=300,y=500)
                                                                                bc2.config(font=('Courier',15))
                                                                                bc6=Button(dot2,text='SAVE PHOTO',command=bacteria,bg='cyan',width=15,fg='red')
                                                                                bc6.place(x=300,y=600)
                                                                                bc6.config(font=('Courier',15))
                                                                                rt=g1.get()
                                                                                root1.update_idletasks()
                                                                                global my_image1
                                                                                my_image1=PhotoImage(file='IMG\\'+rt+'.gif')#NEEDS TO BE CHANGED
                                                                                dot1.create_image(13, 10, anchor = NW, image=my_image1)
                                                                                a2.destroy()
                                                                                ab.destroy()
                                                                                root1.mainloop()
                                                                            corona()
                                                                         elif ans=='no':
                                                                             ask1=m.showinfo("SUCCESS","ACCOUNT CREATED SUCCESSFULLY!!!")
                                                                             ask2=m.showinfo("LOGIN","MOVE BACK TO TEACHER LOGIN CORNER")
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
               pass


                
        def b__11(x=0):
            b9.focus()
        def b___11(x=0):
            b10.focus()
        b11=Button(dot,text="SAVE",command=b_11,bg='cyan',width=14,fg='red')
        b11.place(x=450,y=600)
        b11.config(font=('Courier',18))
        b11.focus()
        b11.bind("<Return>",b_11)
        b11.bind("<Right>",b___11)
        b11.bind("<Left>",b__11)
        root1.mainloop()
        
        
            
        

        
    def sns(x=0):
        pass
    def sps(x=0):
        
        s1=Canvas(root1,bg="white",width=1366,height=690)
        s1.place(x=0,y=0)
        my_image4=PhotoImage(file='IMG\\sc6.png')
        s1.create_image(650, 0, anchor = N, image=my_image4)
        my_image5=PhotoImage(file='IMG\\bb4.png')
        s1.create_image(500, 180, anchor = N, image=my_image5)
        my_image6=PhotoImage(file='IMG\\bb5.png')
        s1.create_image(180, 135, anchor = N, image=my_image6)
        my_image7=PhotoImage(file='IMG\\bb6.png')
        s1.create_image(170, 280, anchor = N, image=my_image7)
        my_image8=PhotoImage(file='IMG\\bb12.png')
        s1.create_image(820, 330, anchor = N, image=my_image8)
        my_image9=PhotoImage(file='IMG\\bb11.png')
        s1.create_image(1170, 320, anchor = N, image=my_image9)
        my_image10=PhotoImage(file='IMG\\bb13.png')
        s1.create_image(680,0, anchor = N, image=my_image10)
        image=PhotoImage(file='IMG\\mbsa5.png')
        image1=image.subsample(2,2)
        image2=PhotoImage(file='IMG\\mbsa6.png')
        image3=image2.subsample(4,4)
        image4=image2.subsample(6,6)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44
        def dt():
            s3=Canvas(root1,bg="white",width=1366,height=690)
            s3.place(x=0,y=0)
            my_image11=PhotoImage(file='IMG\\sc6.png')
            s3.create_image(650, 0, anchor = CENTER, image=my_image11)
            #enter details label======================================================
            Lb1=Label(s3,text="*  ENTER YOUR DETAILS  *",width=30,bg="cyan",fg="red")
            Lb1.place(x=390,y=0)
            Lb1.config(font=("helvetica",25))
           
           
           
        #-----------------------------
            global B_1
            def B_1():
                def MB(*args):
                    value=A1.get()
                    if len(value)>10:
                        A1.set(value[:10])
                    if value.isdigit()==False and value!='':
                        ans3=m.showwarning("WARNING","WRONG INPUT")
                    
                global A1
                A1=StringVar()
                A1.trace("w",MB)
                global E1
                E1=Entry(s3,width=15,textvariable=A1,bg="OliveDrab1")
                E1.bind("<Return>",B_2)
                E1.place(x=335,y=140)
                E1.config(font=("helvetica",28))
                E1.focus()
            B1=Button(s3,text='MOBILE.NO',command=B_1,bg='cyan',width=17,fg='red')
            B1.place(x=60,y=140)
            B1.config(font=('Courier',18))
        
        
        #-----------------------------
            global B_2
            def B_2(x=0):
                global B
                def ad(*args):
                    value=B.get()
                    if len(value)>50:
                        B.set(value[:50])                
                    if value.isalnum()==False and value.isspace()==True and value!='':
                        ans3=m.showwarning("WARNING","WRONG INPUT")
                    
                
                
                
                B=StringVar()
                B.trace('w',ad)
                global E2
                E2=Entry(s3,width=15,textvariable=B,bg="OliveDrab1")
                E2.bind("<Return>",B_3)
                E2.place(x=335,y=230)
                E2.config(font=("helvetica",28))
                E2.focus()
            B2=Button(s3,text='ADDRESS',command=B_2,bg='cyan',width=17,fg='red')
            B2.place(x=60,y=230)
            B2.config(font=('Courier',18))
        
        #------------------------------
            global B_3
            def B_3(x=0):
                global C
                C1=StringVar()         
                def C_2(*args):
                    value=C2.get()
                    if len(value)>2:
                        C2.set(value[:2])
                    if value.isdigit()==False and value!='':
                        ans=m.showwarning("WARNING","WRONG INPUT")
                
                def MONTH(x=0):
                    def C_4(*args):
                        value=C11.get()
                        if len(value)>2:
                            C11.set(value[:2])
                        if value.isdigit()==False and value!='':
                            ans=m.showwarning("WARNING","WRONG INPUT")
                    def YEAR(x=0):
                        def C_5(*args):
                             value=C12.get()
                             if len(value)>4:
                                C12.set(value[:4])
                             if value.isdigit()==False and value!='':
                                ans=m.showwarning("WARNING","WRONG INPUT")
                        B4.destroy()
                        E11.destroy()
                        B5=Label(s3,text='YEAR',bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
                        B5.place(x=60,y=320)
                        B5.config(font=('Courier',18))
                        global C12
                        C12=StringVar()
                        C12.trace('w',C_5)
                        global E12
                        E12=Entry(s3,width=15,textvariable=C12,bg="OliveDrab1")
                        E12.place(x=335,y=320)
                        E12.config(font=("helvetica",28))
                        E12.focus()
                        E12.bind("<Return>",B_4)
                    B2.destroy()
                    E3.destroy()
                    B4=Label(s3,text='MONTH',bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
                    B4.place(x=60,y=320)
                    B4.config(font=('Courier',18))
                    global C11
                    C11=StringVar()
                    C11.trace('w',C_4)
                    global E11
                    E11=Entry(s3,width=15,textvariable=C11,bg="OliveDrab1")
                    E11.place(x=335,y=320)
                    E11.config(font=("helvetica",28))
                    E11.focus()
                    E11.bind("<Return>",YEAR)
                B2=Label(s3,text='DATE',bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
                B2.place(x=60,y=320)
                B2.config(font=('Courier',18))
                global C2
                C2=StringVar()
                C2.trace('w',C_2)
                global E3
                E3=Entry(s3,width=15,textvariable=C2,bg="OliveDrab1")
                E3.place(x=335,y=320)
                E3.config(font=("helvetica",28))
                E3.focus()
                E3.bind("<Return>",MONTH)
            B3=Button(s3,text='D.O.B',command=B_3,bg='cyan',width=17,fg='red')    #FORMAT IS OF IMPORTANCE
            B3.place(x=60,y=320)
            B3.config(font=('Courier',18))
        #-------------==========


        
        #-------------------------------
            global B_4
            def B_4(x=0):
                global D
                D=StringVar()
                global E4
                E4=Entry(s3,width=15,textvariable=D,bg="OliveDrab1")
                E4.bind("<Return>",B_9)
                E4.place(x=335,y=410)
                E4.config(font=("helvetica",28))
                E4.focus()
            
            B4=Button(s3,text='SUBJECT',command=B_4,bg='cyan',width=17,fg='red')
            B4.place(x=60,y=410)
            B4.config(font=('Courier',18))
        
        #-------------------------------
            global B_5
            def B_5(x=0):
                def EMAIL(*args):
                    value=E.get()
                    if len(value)>30:
                        E.set(value[:30])
                global E
                E=StringVar()
                E.trace('w',EMAIL)
                global E5
                E5=Entry(s3,width=15,textvariable=E,bg="Olivedrab1")
                E5.bind("<Return>",B_6)
                E5.place(x=970,y=140)
                E5.config(font=("helvetica",28))
                E5.focus()
            B5=Button(s3,text='E-MAIL',command=B_5,bg='cyan',width=17,fg='red')
            B5.place(x=700,y=140)
            B5.config(font=('Courier',18)) 
        
        #-------------------------------
            global B_6
            def B_6(x=0): 
                global F
                F=StringVar()
                global E6
                E6=Entry(s3,width=15,textvariable=F,bg="OliveDrab1",show='*')
                E6.bind("<Return>",B_7)
                E6.place(x=970,y=230)
                E6.config(font=("helvetica",28))
                E6.focus()
            B6=Button(s3,text='PASSWORD',command=B_6,bg='cyan',width=17,fg='red')
            B6.place(x=700,y=230)
            B6.config(font=('Courier',18))
        
        #-------------------------------
            global B_7
            def B_7(x=0):
                value=F.get()
                if len(value)<8:
                   ans3=m.showwarning("WARNING","LESS THAN 8 CHARATERS\n NOT ACCEPTED")
                else:
                   global G
                   G=StringVar()
                   global E7
                   E7=Entry(s3,width=15,textvariable=G,bg="OliveDrab1",show='*')
                   E7.bind("<Return>",B_8)
                   E7.place(x=970,y=320)
                   E7.config(font=("helvetica",28))
                   E7.focus()
            def AD():
                pass
            B7=Button(s3,text='CONFIRM PASSWORD',command=AD,bg='cyan',width=17,fg='red')
            B7.place(x=700,y=320)
            B7.config(font=('Courier',18))
        
        #-------------------------------
            global B_8
            def B_8(x=0):
                global H
                H=StringVar()
                global E8
                E8=Entry(s3,width=15,textvariable=H,bg="OliveDrab1")
                E8.bind("<Return>",B_10)
                E8.place(x=970,y=410)
                E8.config(font=("Helvetica",28))
                E8.focus()
    
            B8=Button(s3,text="NAME OF\n THE SCHOOL",command=B_8,bg='cyan',width=17,fg='red')
            B8.place(x=700,y=410)
            B8.config(font=('Courier',18))
        ################################
            global B_9
            def B_9(x=0):
                 global J
                 J=StringVar()
                 global E9
                 E9=Entry(s3,width=15,textvariable=J,bg="OliveDrab1")
                 E9.bind("<Return>",B_5)
                 E9.place(x=335,y=500)
                 E9.config(font=("helvetica",28))
                 E9.focus()
            
            
            B9=Button(s3,text="NAME",command=B_9,bg='cyan',width=17,fg='red')
            B9.place(x=60,y=500)
            B9.config(font=('Courier',18))
        #=========================-=-=-=-=-=-=-
            global B_10
            def B_10(x=0):
                def age(*args):
                    value=K.get()
                    if len(value)>2:
                        K.set(value[:2])
                    if value.isdigit()==False and value!='':
                        ans4=m.showwarning("WARNING","WRONG INPUT")
                    
                global K
                K=StringVar()
                K.trace('w',age)
                global E10
                E10=Entry(s3,width=15,textvariable=K,bg="OliveDrab1")
                E10.place(x=970,y=500)
                E10.config(font=("helvetica",28))
                E10.focus()
    
            B10=Button(s3,text="AGE",command=B_10,bg='cyan',width=17,fg='red')
            B10.place(x=700,y=500)
            B10.config(font=('Courier',18))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        
            def back3(x=0):
                s3.destroy()
                b123.focus()
            bck3=Button(s3,command=back3)
            bck3.place(x=0,y=0)
            bck3.config(image=image4,font=('Courier',15))
            bck3.focus()
            bck3.bind("<BackSpace>",back3)
            
            root1.mainloop()
        global w_1
        def w_1():
            if i.get()==11:
               def cs(*args):
                   root1.update_idletasks()
                   if z.get()=="MATHEMATICS":
                      z1=StringVar()
                      z1.set("SELECT EXAM")
                      s11=OptionMenu(s1,z1,"JEE MAINS","JEE ADVANCED","JEE MAINS AND ADV.","CBSE BOARDS","ICSE BOARDS","PET")
                      s11.place(x=740,y=250)
                      s11.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z.get()=="BIOLOGY":
                      z2=StringVar()
                      z2.set("SELECT EXAM")
                      s22=OptionMenu(s1,z2,"NEET","AIMS","ZIPMER","AIMPMT","CBSE BOARDS","ICSE BOARDS")
                      s22.place(x=740,y=250)
                      s22.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z.get()=="COMMERCE":
                      z3=StringVar()
                      z3.set("SELECT EXAM")
                      s33=OptionMenu(s1,z3,"CBSE BOARDS","ICSE BOARDS","CFA","CA","CS","MBA","CMA")
                      s33.place(x=740,y=250)
                      s33.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z.get()=="ARTS":
                      z4=StringVar()
                      z4.set("SELECT EXAM")
                      s44=OptionMenu(s1,z4,"CBSE BOARDS","ICSE BOARDS","JNUEE","XAT","SUAT")
                      s44.place(x=740,y=250)
                      s44.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z.get()=="COMPUTER SCIENCE":
                      z5=StringVar()
                      z5.set("SELECT EXAM")
                      s55=OptionMenu(s1,z5,"CBSE BOARDS","ICSE BOARDS","JAVA TUT.","C TUT.","C++ TUT.")
                      s55.place(x=740,y=250)
                      s55.config(font=("Algerian",14))
                      root1.update_idletasks()
                      
               w1.destroy()
               z=StringVar()
               z.trace('w',cs)
               z.set("SUBJECT")
               s=OptionMenu(s1,z,"MATHEMATICS","BIOLOGY","COMMERCE","ARTS","COMPUTER SCIENCE")
               s.place(x=740,y=160)
               s.config(font=("Algerian",14))

               
                
        global w_2
        def w_2():
            if i.get()==12:
               def cs1(*args):
                   root1.update_idletasks()
                   if z6.get()=="MATHEMATICS":
                      z1=StringVar()
                      z1.set("SELECT EXAM")
                      s11=OptionMenu(s1,z1,"JEE MAINS","JEE ADVANCED","JEE MAINS AND ADV.","CBSE BOARDS","ICSE BOARDS","PET")
                      s11.place(x=1030,y=250)
                      s11.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z6.get()=="BIOLOGY":
                      z2=StringVar()
                      z2.set("SELECT EXAM")
                      s22=OptionMenu(s1,z2,"NEET","AIMS","ZIPMER","AIMPMT","CBSE BOARDS","ICSE BOARDS")
                      s22.place(x=1030,y=250)
                      s22.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z6.get()=="COMMERCE":
                      z3=StringVar()
                      z3.set("SELECT EXAM")
                      s33=OptionMenu(s1,z3,"CBSE BOARDS","ICSE BOARDS","CFA","CA","CS","MBA","CMA")
                      s33.place(x=1030,y=250)
                      s33.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z6.get()=="ARTS":
                      z4=StringVar()
                      z4.set("SELECT EXAM")
                      s44=OptionMenu(s1,z4,"CBSE BOARDS","ICSE BOARDS","JNUEE","XAT","SUAT")
                      s44.place(x=1030,y=250)
                      s44.config(font=("Algerian",14))
                      root1.update_idletasks()
                   elif z6.get()=="COMPUTER SCIENCE":
                      z5=StringVar()
                      z5.set("SELECT EXAM")
                      
                      s55=OptionMenu(s1,z5,"CBSE BOARDS","ICSE BOARDS","JAVA TUT.","C TUT.","C++ TUT.")
                      s55.place(x=1030,y=250)
                      s55.config(font=("Algerian",14))
                      root1.update_idletasks()
                                           
                      
               
                      
               
               w2.destroy()
               z6=StringVar()
               z6.set("SUBJECT")
               z6.trace('w',cs1)
               global s2
               s2=OptionMenu(s1,z6,"MATHEMATICS","BIOLOGY","COMMERCE","ARTS","COMPUTER SCIENCE")
               s2.place(x=1030,y=160)
               s2.config(font=("Algerian",14))
               root1.update_idletasks()

              


               
        def back1(x=0):
            s1.destroy()
            b123.focus()
        bck1=Button(s1,command=back1)
        bck1.place(x=0,y=0)
        bck1.config(image=image4,font=('Courier',15))
        bck1.focus()
        bck1.bind("<BackSpace>",back1)
        def cure(*args):
            value=i.get()
            
        ######################################RADIO BUTTON############
        i=IntVar()
        i.trace('w',cure)
        rb1=Radiobutton(s1,text="CLASS 6",variable=i,value=6,width=15)
        rb1.place(x=60,y=100)
        rb1.config(font=("Algerian",15))
        rb2=Radiobutton(s1,text="CLASS 7",variable=i,value=7,width=15)
        rb2.place(x=60,y=220)
        rb2.config(font=("Algerian",15))
        rb3=Radiobutton(s1,text="CLASS 8",variable=i,value=8,width=15)
        rb3.place(x=60,y=340)
        rb3.config(font=("Algerian",15))
        rb4=Radiobutton(s1,text="CLASS 9",variable=i,value=9,width=15)
        rb4.place(x=350,y=100)
        rb4.config(font=("Algerian",15))
        rb4=Radiobutton(s1,text="CLASS 10",variable=i,value=10,width=15)
        rb4.place(x=350,y=340)
        rb4.config(font=("Algerian",15))
        rb4=Radiobutton(s1,text="CLASS 11",variable=i,value=11,width=15)
        rb4.place(x=740,y=100)
        rb4.config(font=("Algerian",15))
        rb4=Radiobutton(s1,text="CLASS 12",variable=i,value=12,width=15)
        rb4.place(x=1030,y=100)
        rb4.config(font=("Algerian",15))
        ##################################################################33

        w1=Button(s1,text="CHOOSE\nYOUR\nSTREAM",command=w_1,bg='white',width=10,fg='black')
        w1.place(x=843,y=150)
        w1.config(font=('Courier',12))
        w2=Button(s1,text="CHOOSE\nYOUR\nSTREAM",command=w_2,bg='white',width=10,fg='black')
        w2.place(x=1133,y=150)
        w2.config(font=('Courier',12))
        w3=Button(s1,command=dt)
        w3.place(x=650,y=420)
        w3.config(image=image1) 


            
           
            
        s1.create_line(680,80,680,400,fill='white',width=1)
        s1.create_line(310,80,310,400,fill='white',width=1)
        s1.create_line(990,80,990,400,fill='white',width=1)
        
        root1.mainloop()
        
        



    #functions-----------------------------------------
    #label=======================================
    lb1=Label(root1,text="* TEACHER'S CORNER * ",width=30,bg="cyan",fg="red")
    lb1.place(x=65,y=20)
    lb1.config(font=("helvetica",25))
    lb2=Label(root1,text="* STUDENT'S CORNER * ",width=30,bg="cyan",fg="red")
    lb2.place(x=720,y=20)
    lb2.config(font=("helvetica",25))
    #label-------------------------------------------
    #######KEYBOARD-FUNCTIONS##########################
    def u(x=0):
        b3.focus()
    def u1(x=0):
        b2.focus()
    def u2(x=0):
        b4.focus()
    def u3(x=0):
        b123.focus()
    def u4(x=0):
        b123.focus()
    def u5(x=0):
        b4.focus()
    def u6(x=0):
        b2.focus()
    def u7(x=0):
        b3.focus()
    
    #button=========================================
    global b123
    b123=Button(mc,text='LOG IN',command=snt,bg='cyan',fg='red',width=20)
    b123.place(x=235,y=335)
    b123.config(font=('Helvetica',15))
    b123.focus()
    b123.bind("<Return>",snt)
    b123.bind("<Down>",u6)
    b123.bind("<Right>",u7)
    
#------------------------------------------------------------
    b2=Button(mc,text='SIGN UP',command=spt,bg='cyan',fg='red',width=20)
    b2.place(x=235,y=380)
    b2.config(font=('Helvetica',15))
    b2.focus()
    b2.bind("<Return>",spt)
    b2.bind("<Up>",u4)
    b2.bind("<Right>",u5)
    
#---------------------------------------------------
    b3=Button(mc,text='LOG IN',command=sns,bg='cyan',fg='red',width=20)
    b3.place(x=890,y=335)
    b3.config(font=('Helvetica',15))
    b3.focus()
    b3.bind("<Return>",sns)
    b3.bind("<Down>",u2)
    b3.bind("<Left>",u3)
    
#-----------------------------------------------------------------------    
    b4=Button(mc,text='SIGN UP',command=sps,bg='cyan',fg='red',width=20)
    b4.place(x=890,y=380)
    b4.config(font=('Helvetica',15))
    b4.focus()
    b4.bind("<Return>",sps)
    b4.bind("<Up>",u)
    b4.bind("<Left>",u1)
    
    
    root1.focus_force()
    root1.mainloop()
    
s=Button(s,text='CLICK HERE',command=pro,bg='green')
s.place(x=600,y=250)
s.config(font=('Helvetica',15))
s.bind("<Return>",pro)
s.focus()
#############################################################SIGN UP TAECHER   END##########################################################################################################################################################################
#############################################################STUDEN SING IN BEGIN################################################################################
root.mainloop()

