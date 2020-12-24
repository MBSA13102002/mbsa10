import mysql.connector as sql
from tkinter import*
from PIL import ImageTk,Image
import math
from time import ctime
t=ctime()
root=Tk()
root.title("CALCULATOR")
root.geometry("500x450+500+120")
root.iconbitmap("C:/Users/HOME/Desktop/logo.ico")
operator=""
global output1
root.resizable(0,0)
r1=Canvas(root,bg="gray73",width=500,height=450)
r1.place(x=0,y=0)
r=Canvas(root,bg="green",width=500,height=450)
r.place(x=0,y=150)
calm=PhotoImage(file='C:\\Users\\HOME\\Desktop\\CALCULATORIMAGE.gif')
r.create_image(0,0,anchor=NW,image=calm)
history=[]
li=[]
def opens():
    s.destroy()
    #time====================================================================
    t2=Label(r,text="'{}'".format(t),bg="gold2",fg="blue")
    t2.place(x=10,y=270)
    def show1():
        #NAME BUTTON1=======================================================
        name1=Button(r,text="MADE BY:",bg="gray25",fg="yellow")
        name1.place(x=6,y=150)
        name1.config(font=("Algerian",25)) 
        #NAME BUTTON2======================================================
        def desname():
            name1.destroy()
            name2.destroy()
            name3.destroy()
        name2=Button(r,text="OM KUMAR",bg="gray25",fg="yellow")
        name2.place(x=300,y=156)
        name2.config(font=("Algerian",23))
        #destroy===========================================================
        name3=Button(r,text="^",bg="gray25",fg="yellow",command=desname)
        name3.place(x=225,y=220)
        name3.config(font=("Algerian",23))
    #NAME============================================================================================================
    show=Button(r,text="SHOW",width=30,bg="gray25",fg="yellow",command=show1)
    show.place(x=6,y=80)
    show.config(font=("HELVETICA",21))
    #square root block================================================================================================================
    def sqrt():
        r2=Canvas(r,bg="black",width=500,height=450)
        r2.place(x=0,y=0)
        def result1():
            if operator=="":
                return 0
            else:
                 global output
                 global sqr
                 sqr=math.sqrt(float(operator))
                 output=Label(r1,bg="gray73",text="{}".format(sqr))
                 output.place(x=5,y=100)
                 output.config(font=("Algerian",25))
                 history.append(operator)
                 li.append(sqr)
                
        #scroll function==================================================================================================
        def sc():
            global txt
            txt=Tk()
            txt.title("STORE")
            txt.iconbitmap("C:\\Users\\HOME\\Desktop\\logo.ico")
            txt.resizable(0,0)
            scroll=Scrollbar(txt)
            scroll.pack(side=RIGHT,fill=Y)
            txt.geometry("500x450+500+120")
            txt1=Text(txt,width=500,height=450,bg="navy",fg="yellow",font="courier",selectbackground="red",yscrollcommand=scroll.set)
            scroll.config(command=txt1.yview)
            txt1.insert(INSERT,"###############################################\n")
            txt1.insert(INSERT,"=========WELCOME TO SQUARE ROOT WINDOW========================================================\n")
            try:
                for i in range(0,len(history)):
                    txt1.insert(INSERT,"{}\n".format(history[i]))
                    txt1.insert(INSERT,"{}\n".format(li[i]))
                    txt1.insert(INSERT,"=============================================={}".format(i))
            except:
                txt1.insert(INSERT,"{}".format("NONE"))
            
            txt1.pack()
            txt.mainloop()
        #==scroll=========================================================================================================
        scr=Button(r2,text="STORE RESULT",bg="gray25",fg="red",width=12,command=sc)
        scr.place(x=300,y=80)
        scr.config(font=("algerian",19))
                 
        def buttonin(number):
            global operator
            operator=operator + str(number)
            var.set(operator)
        def mc():
            try:
               output=Label(r1,bg="gray73",text="                                                        ")#illusion
               output.place(x=5,y=100)
               output.config(font=("Algerian",25))  
            except:
                print("")
        def clear1():
            try:
                output.destroy()
            except:
                print("")
            global operator
            
            operator=""
            var.set("")
            
        var=StringVar()
        entry=Entry(r1,bg="gray73",textvariable=var,width=40)
        entry.place(x=5,y=50)
        entry.config(font=("Algerian",25))
        #button 1
        
        one=Button(r2,text="  1   ",bg="gray25",fg="white",command=lambda:buttonin(1))
        one.place(x=5,y=5)
        one.config(font=("Algerian",25))
        #button 2
            
        two=Button(r2,text="  2   ",bg="gray25",fg="white",command=lambda:buttonin(2))
        two.place(x=102,y=5)
        two.config(font=("Algerian",25))        
        #button 3
        
        three=Button(r2,text="  3   ",bg="gray25",fg="white",command=lambda:buttonin(3))
        three.place(x=200,y=5)
        three.config(font=("Algerian",25))
        #button 4
        
        four=Button(r2,text="  4   ",bg="gray25",fg="white",command=lambda:buttonin(4))
        four.place(x=5,y=80)
        four.config(font=("Algerian",25))
        #button 5
        
        five=Button(r2,text="  5   ",bg="gray25",fg="white",command=lambda:buttonin(5))
        five.place(x=102,y=80)
        five.config(font=("Algerian",25))
        #button 5
        
        six=Button(r2,text="  6   ",bg="gray25",fg="white",command=lambda:buttonin(6))
        six.place(x=200,y=80)
        six.config(font=("Algerian",25))
        #button 7
        
        seven=Button(r2,text="  7   ",bg="gray25",fg="white",command=lambda:buttonin(7))
        seven.place(x=5,y=155)
        seven.config(font=("Algerian",25))
        #button 8
        eight=Button(r2,text="  8   ",bg="gray25",fg="white",command=lambda:buttonin(8))
        eight.place(x=102,y=155)
        eight.config(font=("Algerian",25))
        #button 9
        
        nine=Button(r2,text="  9   ",bg="gray25",fg="white",command=lambda:buttonin(9))
        nine.place(x=200,y=155)
        nine.config(font=("Algerian",25))
        #button 0
        
        zero=Button(r2,text="  0   ",bg="gray25",fg="white",command=lambda:buttonin(0))
        zero.place(x=105,y=230)
        zero.config(font=("Algerian",25))
        #button clear

        clear=Button(r2,text="  C  ",bg="gray25",fg="white",command=clear1)
        clear.place(x=200,y=230)
        clear.config(font=("Algerian",25))
        #button =

        result=Button(r2,text="  =  ",bg="gray25",fg="white",command=result1)
        result.place(x=295,y=230)
        result.config(font=("Algerian",25))
        #DECIMAL BUTTON========================================================
        dec=Button(r2,text="  .  ",bg="gray25",fg="white",command=lambda:buttonin("."))
        dec.place(x=300,y=5)
        dec.config(font=("Algerian",25))
        #master clear=====================================================================================================
        cm=Button(r2,text=" AC ",bg="gray25",fg="white",command=mc)
        cm.place(x=390,y=5)
        cm.config(font=("Algerian",25))

        #back button destroys button canvas.
        def bback():
            r2.destroy()
            entry.destroy()
            try:
                output.destroy()
            except:
                print("")
            
            
            
        back=Button(r2,text="back",bg="gray25",fg="white",command=bback)
        back.place(x=5,y=230)
        back.config(font=("Algerian",25))
        

#sqrt button=========================================================================                   
    sq=Button(r,text="Sqrt",bg="OrangeRed2",command=sqrt)
    sq.place(x=15,y=5)
    sq.config(font=("Algerian",25))
#addition block======================================================================================================
    def addition():
        r2=Canvas(r,bg="brown4",width=500,height=450)
        r2.place(x=0,y=0)
        def result2():
            global sum
            le=len(str(operator))
            q=entry.get()
            w=eval(q)
            entry.delete(0,'end')
            entry.insert(0,str(q))
                      
        #scroll function==================================================================================================
        def sc():
            global txt
            txt=Tk()
            txt.title("STORE")
            txt.iconbitmap("C:\\Users\\HOME\\Desktop\\logo.ico")
            txt.resizable(0,0)
            scroll=Scrollbar(txt)
            scroll.pack(side=RIGHT,fill=Y)
            txt.geometry("500x450+500+120")
            txt1=Text(txt,width=500,height=450,bg="navy",fg="yellow",font="courier",selectbackground="red",yscrollcommand=scroll.set)
            scroll.config(command=txt1.yview)
            txt1.insert(INSERT,"###############################################\n")
            txt1.insert(INSERT,"============WELCOME TO ADDITION WINDOW========================================================\n")
            try:
                txt1.insert(INSERT,"{}\n".format(operator))
                txt1.insert(INSERT,"{}".format(sum))
            except:
                txt1.insert(INSERT,"{}".format("NONE"))
            txt1.config(state="disabled")
            txt1.pack()
            txt.mainloop()
        #==scroll=========================================================================================================
        scr=Button(r2,text="STORE RESULT",bg="gray25",width=12,command=sc)
        scr.place(x=300,y=80)
        scr.config(font=("courier",19))

        def buttonin(number):
            global operator
            operator=operator + str(number)
            var.set(operator)
        def mc():
            try:
               output=Label(r1,bg="green",text="                                                        ")
               output.place(x=5,y=100)
               output.config(font=("Algerian",25))  
            except:
                print("")    
        def clear2():
            global operator
            try:
                output2.destroy()
            except:
                print("")                           
            operator=""
            var.set("")
                
       #1st Entry==============================================     
        var=StringVar()
        entry=Entry(r1,bg="green",textvariable=var,width=40)
        entry.place(x=5,y=50)
        entry.config(font=("Algerian",25))
        #button 1
        
        one=Button(r2,text="  1   ",bg="gray25",fg="yellow",command=lambda:buttonin(1))
        one.place(x=5,y=5)
        one.config(font=("Algerian",25))
        #button 2
            
        two=Button(r2,text="  2   ",bg="gray25",fg="yellow",command=lambda:buttonin(2))
        two.place(x=102,y=5)
        two.config(font=("Algerian",25))        
        #button 3
        
        three=Button(r2,text="  3   ",bg="gray25",fg="yellow",command=lambda:buttonin(3))
        three.place(x=200,y=5)
        three.config(font=("Algerian",25))
        #button 4
        
        four=Button(r2,text="  4   ",bg="gray25",fg="yellow",command=lambda:buttonin(4))
        four.place(x=5,y=80)
        four.config(font=("Algerian",25))
        #button 5
        
        five=Button(r2,text="  5   ",bg="gray25",fg="yellow",command=lambda:buttonin(5))
        five.place(x=102,y=80)
        five.config(font=("Algerian",25))
        #button 5
        
        six=Button(r2,text="  6   ",bg="gray25",fg="yellow",command=lambda:buttonin(6))
        six.place(x=200,y=80)
        six.config(font=("Algerian",25))
        #button 7
        
        seven=Button(r2,text="  7   ",bg="gray25",fg="yellow",command=lambda:buttonin(7))
        seven.place(x=5,y=155)
        seven.config(font=("Algerian",25))
        #button 8
        eight=Button(r2,text="  8   ",bg="gray25",fg="yellow",command=lambda:buttonin(8))
        eight.place(x=102,y=155)
        eight.config(font=("Algerian",25))
        #button 9
        
        nine=Button(r2,text="  9   ",bg="gray25",fg="yellow",command=lambda:buttonin(9))
        nine.place(x=200,y=155)
        nine.config(font=("Algerian",25))
        #button 0
        
        zero=Button(r2,text="  0   ",bg="gray25",fg="yellow",command=lambda:buttonin(0))
        zero.place(x=105,y=230)
        zero.config(font=("Algerian",25))
        #button clear

        clear=Button(r2,text="  C  ",bg="gray25",fg="yellow",command=clear2)
        clear.place(x=200,y=230)
        clear.config(font=("Algerian",25))
        #master clear=====================================================================================================
        cm=Button(r2,text="AC",bg="gray25",fg="yellow",command=mc)
        cm.place(x=390,y=5)
        cm.config(font=("Algerian",23))
        #button =

        result=Button(r2,text="  =  ",bg="gray25",fg="yellow",command=result2)
        result.place(x=300,y=230)
        result.config(font=("Algerian",25))
        #back button destroys button canvas.
        def bback():
            r2.destroy()
            entry.destroy()       
            try:
                output.destroy()
            except:
                print("")
                
        back=Button(r2,text="back",bg="gray25",fg="yellow",command=bback)
        back.place(x=5,y=230)
        back.config(font=("Algerian",25))
        #DECIMAL BUTTON========================================================
        dec=Button(r2,text="  .  ",bg="gray25",fg="yellow",command=lambda:buttonin("."))
        dec.place(x=300,y=5)
        dec.config(font=("Algerian",23)) 
        #+++++++ BUTTON=======================
        plus=Button(r2,text="  +  ",bg="gray25",fg="yellow",command=lambda:buttonin("+"))
        plus.place(x=395,y=230)
        plus.config(font=("Algerian",25))        
#ADD BUTTON======================================================================================
    add=Button(r,text="  +  ",bg="OrangeRed2",command=addition)
    add.place(x=110,y=5)
    add.config(font=("Algerian",25))
#subtraction================================================================================================================
    def subtraction():
        r2=Canvas(r,bg="brown4",width=500,height=450)
        r2.place(x=0,y=0)
        def result3():
            global sum
            le=len(str(operator))
            for i in range(0,le):
                if operator[i]=="-":
                    m=operator[:i] #for taking the values of before + sign
                    n=operator[i+1:] #for taking the values of after + sign
                    r=len(m)
                    tr=len(n)
                    global w
                    global u
                    for y in range(0,r):
                        if m[y]==".":
                           k=m[:y]   #slicing m before .
                           f=m[y+1:] #slicing m after .
                           re=len(f) 
                           try:
                              u=int(k+f)/math.pow(10,re) #using the concept that 44.55 is the answer from 4455/100(where denominator is power of 10 raised to the no after decimal
                           except:
                               print("..")
                    for q in range(0,tr):
                        if n[q]==".":
                           k=n[:q]   #slicing m before .
                           f=n[q+1:] #slicing m after .
                           re1=len(f)
                           try:
                               w=int(k+f)/math.pow(10,re1)
                           except:
                               print("..")
                    try:
                        sum=int(m)-int(n)
                        global output2
                        output2=Label(r1,bg="green",text="{}".format(sum))
                        output2.place(x=5,y=100)
                        output2.config(font=("Algerian",25))

                    except:
                        try:
                          sum=u-w
                          output2=Label(r1,bg="green",text="{}".format(sum))
                          output2.place(x=5,y=100)
                          output2.config(font=("Algerian",25)) 
                        except:
                            try:
                               sum=u-int(n)
                               output2=Label(r1,bg="green",text="{}".format(sum))
                               output2.place(x=5,y=100)
                               output2.config(font=("Algerian",25))
                            except:
                                sum=int(m)-w
                                output2=Label(r1,bg="green",text="{}".format(sum))
                                output2.place(x=5,y=100)
                                output2.config(font=("Algerian",25)) 
        #scroll function==================================================================================================
        def sc():
            global txt
            txt=Tk()
            txt.title("STORE")
            txt.iconbitmap("C:\\Users\\HOME\\Desktop\\logo.ico")
            txt.resizable(0,0)
            scroll=Scrollbar(txt)
            scroll.pack(side=RIGHT,fill=Y)
            txt.geometry("500x450+500+120")
            txt1=Text(txt,width=500,height=450,bg="navy",fg="yellow",font="courier",selectbackground="red",yscrollcommand=scroll.set)
            scroll.config(command=txt1.yview)
            txt1.insert(INSERT,"###############################################\n")
            txt1.insert(INSERT,"=========WELCOME TO SUBTRACTION WINDOW========================================================\n")
            try:
                txt1.insert(INSERT,"{}\n".format(operator))
                txt1.insert(INSERT,"{}".format(sum))
            except:
                txt1.insert(INSERT,"{}".format("NONE"))
            txt1.config(state="disabled")
            txt1.pack()
            txt.mainloop()
        #==scroll=========================================================================================================
        scr=Button(r2,text="STORE RESULT",bg="gray25",width=12,command=sc)
        scr.place(x=300,y=80)
        scr.config(font=("courier",19))



        def buttonin(number):
            global operator
            operator=operator + str(number)
            var.set(operator)
        def mc():
            try:
               output=Label(r1,bg="green",text="                                                        ")
               output.place(x=5,y=100)
               output.config(font=("Algerian",25))  
            except:
                print("")     
        def clear2():
            try:
                output2.destroy()
            except:
                print("")
            global operator
            
            operator=""
            var.set("")
       #1st Entry==============================================     
        var=StringVar()
        entry=Entry(r1,bg="green",textvariable=var,width=40)
        entry.place(x=5,y=50)
        entry.config(font=("Algerian",25))
        #button 1
        
        one=Button(r2,text="  1   ",bg="gray25",fg="yellow",command=lambda:buttonin(1))
        one.place(x=5,y=5)
        one.config(font=("Algerian",25))
        #button 2
            
        two=Button(r2,text="  2   ",bg="gray25",fg="yellow",command=lambda:buttonin(2))
        two.place(x=102,y=5)
        two.config(font=("Algerian",25))        
        #button 3
        
        three=Button(r2,text="  3   ",bg="gray25",fg="yellow",command=lambda:buttonin(3))
        three.place(x=200,y=5)
        three.config(font=("Algerian",25))
        #button 4
        
        four=Button(r2,text="  4   ",bg="gray25",fg="yellow",command=lambda:buttonin(4))
        four.place(x=5,y=80)
        four.config(font=("Algerian",25))
        #button 5
        
        five=Button(r2,text="  5   ",bg="gray25",fg="yellow",command=lambda:buttonin(5))
        five.place(x=102,y=80)
        five.config(font=("Algerian",25))
        #button 5
        
        six=Button(r2,text="  6   ",bg="gray25",fg="yellow",command=lambda:buttonin(6))
        six.place(x=200,y=80)
        six.config(font=("Algerian",25))
        #button 7
        
        seven=Button(r2,text="  7   ",bg="gray25",fg="yellow",command=lambda:buttonin(7))
        seven.place(x=5,y=155)
        seven.config(font=("Algerian",25))
        #button 8
        eight=Button(r2,text="  8   ",bg="gray25",fg="yellow",command=lambda:buttonin(8))
        eight.place(x=102,y=155)
        eight.config(font=("Algerian",25))
        #button 9
        
        nine=Button(r2,text="  9   ",bg="gray25",fg="yellow",command=lambda:buttonin(9))
        nine.place(x=200,y=155)
        nine.config(font=("Algerian",25))
        #button 0
        
        zero=Button(r2,text="  0   ",bg="gray25",fg="yellow",command=lambda:buttonin(0))
        zero.place(x=105,y=230)
        zero.config(font=("Algerian",25))
        #button clear

        clear=Button(r2,text="  C  ",bg="gray25",fg="yellow",command=clear2)
        clear.place(x=200,y=230)
        clear.config(font=("Algerian",25))
        #button =

        result=Button(r2,text="  =  ",bg="gray25",fg="yellow",command=result3)
        result.place(x=300,y=230)
        result.config(font=("Algerian",25))
        #master clear=====================================================================================================
        cm=Button(r2,text="AC",bg="gray25",fg="yellow",command=mc)
        cm.place(x=390,y=5)
        cm.config(font=("Algerian",23))
        #DECIMAL BUTTON========================================================
        dec=Button(r2,text="  .  ",bg="gray25",fg="yellow",command=lambda:buttonin("."))
        dec.place(x=300,y=5)
        dec.config(font=("Algerian",23)) 
        #back button destroys button canvas.
        def bback():
            r2.destroy()
            entry.destroy()       
            try:
                output.destroy()
            except:
                print("")
                
        back=Button(r2,text="back",bg="gray25",fg="yellow",command=bback)
        back.place(x=5,y=230)
        back.config(font=("Algerian",25))
        #+++++++ BUTTON=======================
        plus=Button(r2,text=" - ",bg="gray25",fg="yellow",command=lambda:buttonin("-"))
        plus.place(x=395,y=230)
        plus.config(font=("Algerian",25))        
#SUB BUTTON==================================================================================================
    sub=Button(r,text="  -  ",bg="OrangeRed2",command=subtraction)
    sub.place(x=200,y=5)
    sub.config(font=("Algerian",25))
#MULTIPLICATION========================================================================================================
    def multiply():
        r2=Canvas(r,bg="brown4",width=500,height=450)
        r2.place(x=0,y=0)
        def result4():
            global sum
            le=len(str(operator))
            for i in range(0,le):
                if operator[i]=="*":
                    global out
                    m=operator[:i] #for taking the values of before + sign
                    n=operator[i+1:] #for taking the values of after + sign
                    r=len(m)
                    tr=len(n)
                    global w
                    global u
                    for y in range(0,r):
                        if m[y]==".":
                           k=m[:y]   #slicing m before .
                           f=m[y+1:] #slicing m after .
                           re=len(f) 
                           u=int(k+f)/math.pow(10,re) #using the concept that 44.55 is the answer from 4455/100(where denominator is power of 10 raised to the no after decimal
                           
                    for q in range(0,tr):
                        if n[q]==".":
                           k=n[:q]   #slicing m before .
                           f=n[q+1:] #slicing m after .
                           re1=len(f) 
                           w=int(k+f)/math.pow(10,re1)
                    
                    try:
                        sum=int(m)*int(n)
                        global output2
                        output2=Label(r1,bg="green",text="{}".format(sum))
                        output2.place(x=5,y=100)
                        output2.config(font=("Algerian",25))

                    except:
                        try:
                          sum=u*w
                          output2=Label(r1,bg="green",text="{}".format(sum))
                          output2.place(x=5,y=100)
                          output2.config(font=("Algerian",25)) 
                        except:
                            try:
                               sum=u*int(n)
                               output2=Label(r1,bg="green",text="{}".format(sum))
                               output2.place(x=5,y=100)
                               output2.config(font=("Algerian",25))
                            except:
                                sum=int(m)*w
                                output2=Label(r1,bg="green",text="{}".format(sum))
                                output2.place(x=5,y=100)
                                output2.config(font=("Algerian",25))                     
        #scroll function==================================================================================================
        def sc():
            global txt
            txt=Tk()
            txt.title("STORE")
            txt.iconbitmap("C:\\Users\\HOME\\Desktop\\logo.ico")
            txt.resizable(0,0)
            scroll=Scrollbar(txt)
            scroll.pack(side=RIGHT,fill=Y)
            txt.geometry("500x450+500+120")
            txt1=Text(txt,width=500,height=450,bg="navy",fg="yellow",font="courier",selectbackground="red",yscrollcommand=scroll.set)
            scroll.config(command=txt1.yview)
            txt1.insert(INSERT,"###############################################\n")
            txt1.insert(INSERT,"=========WELCOME TO MULTIPLICATION WINDOW=====================================================\n")
            try:
                txt1.insert(INSERT,"{}\n".format(operator))
                txt1.insert(INSERT,"{}".format(sum))
            except:
                txt1.insert(INSERT,"{}".format("NONE"))
            txt1.config(state="disabled")
            txt1.pack()
            txt.mainloop()
        #==scroll=========================================================================================================
        scr=Button(r2,text="STORE RESULT",bg="gray25",width=12,command=sc)
        scr.place(x=300,y=80)
        scr.config(font=("courier",19))

        def buttonin(number):
            global operator
            operator=operator + str(number)
            var.set(operator)
        def mc():
            try:
               output=Label(r1,bg="green",text="                                                        ")
               output.place(x=5,y=100)
               output.config(font=("Algerian",25))  
            except:
                print("")    
        def clear2():
            global operator
            try:
                output2.destroy()
            except:
                print("")              
            if operator!="":
                output2.destroy()
                
                operator=""
                var.set("")
                
       #1st Entry==============================================     
        var=StringVar()
        entry=Entry(r1,bg="green",textvariable=var,width=40)
        entry.place(x=5,y=50)
        entry.config(font=("Algerian",25))
        #button 1
        
        one=Button(r2,text="  1   ",bg="gray25",fg="yellow",command=lambda:buttonin(1))
        one.place(x=5,y=5)
        one.config(font=("Algerian",25))
        #button 2
            
        two=Button(r2,text="  2   ",bg="gray25",fg="yellow",command=lambda:buttonin(2))
        two.place(x=102,y=5)
        two.config(font=("Algerian",25))        
        #button 3
        
        three=Button(r2,text="  3   ",bg="gray25",fg="yellow",command=lambda:buttonin(3))
        three.place(x=200,y=5)
        three.config(font=("Algerian",25))
        #button 4
        
        four=Button(r2,text="  4   ",bg="gray25",fg="yellow",command=lambda:buttonin(4))
        four.place(x=5,y=80)
        four.config(font=("Algerian",25))
        #button 5
        
        five=Button(r2,text="  5   ",bg="gray25",fg="yellow",command=lambda:buttonin(5))
        five.place(x=102,y=80)
        five.config(font=("Algerian",25))
        #button 5
        
        six=Button(r2,text="  6   ",bg="gray25",fg="yellow",command=lambda:buttonin(6))
        six.place(x=200,y=80)
        six.config(font=("Algerian",25))
        #button 7
        
        seven=Button(r2,text="  7   ",bg="gray25",fg="yellow",command=lambda:buttonin(7))
        seven.place(x=5,y=155)
        seven.config(font=("Algerian",25))
        #button 8
        eight=Button(r2,text="  8   ",bg="gray25",fg="yellow",command=lambda:buttonin(8))
        eight.place(x=102,y=155)
        eight.config(font=("Algerian",25))
        #button 9
        
        nine=Button(r2,text="  9   ",bg="gray25",fg="yellow",command=lambda:buttonin(9))
        nine.place(x=200,y=155)
        nine.config(font=("Algerian",25))
        #button 0
        
        zero=Button(r2,text="  0   ",bg="gray25",fg="yellow",command=lambda:buttonin(0))
        zero.place(x=105,y=230)
        zero.config(font=("Algerian",25))
        #button clear

        clear=Button(r2,text="  C  ",bg="gray25",fg="yellow",command=clear2)
        clear.place(x=200,y=230)
        clear.config(font=("Algerian",25))
        #master clear=====================================================================================================
        cm=Button(r2,text="AC",bg="gray25",fg="yellow",command=mc)
        cm.place(x=390,y=5)
        cm.config(font=("Algerian",23))
        #button =

        result=Button(r2,text="  =  ",bg="gray25",fg="yellow",command=result4)
        result.place(x=300,y=230)
        result.config(font=("Algerian",25))
        #back button destroys button canvas.
        def bback():
            r2.destroy()
            entry.destroy()       
            try:
                output.destroy()
            except:
                print("")
                
        back=Button(r2,text="back",bg="gray25",fg="yellow",command=bback)
        back.place(x=5,y=230)
        back.config(font=("Algerian",25))
        #DECIMAL BUTTON========================================================
        dec=Button(r2,text="  .  ",bg="gray25",fg="yellow",command=lambda:buttonin("."))
        dec.place(x=300,y=5)
        dec.config(font=("Algerian",23)) 
        #+++++++ BUTTON=======================
        plus=Button(r2,text="  x  ",bg="gray25",fg="yellow",command=lambda:buttonin("*"))
        plus.place(x=395,y=230)
        plus.config(font=("Algerian",25))        
#MULTIPLY BUTTON======================================================================================
    into=Button(r,text="   x  ",bg="OrangeRed2",command=multiply)
    into.place(x=285,y=5)
    into.config(font=("Algerian",25))
#DIVIDE==========================================================================
    def divide():
        r2=Canvas(r,bg="brown4",width=500,height=450)
        r2.place(x=0,y=0)
        def result5():
            global sum
            le=len(str(operator))
            for i in range(0,le):
                if operator[i]=="/":
                    global out
                    m=operator[:i] #for taking the values of before + sign
                    n=operator[i+1:] #for taking the values of after + sign
                    r=len(m)
                    tr=len(n)
                    global w
                    global u
                    for y in range(0,r):
                        if m[y]==".":
                           k=m[:y]   #slicing m before .
                           f=m[y+1:] #slicing m after .
                           re=len(f) 
                           u=int(k+f)/math.pow(10,re) #using the concept that 44.55 is the answer from 4455/100(where denominator is power of 10 raised to the no after decimal
                           
                    for q in range(0,tr):
                        if n[q]==".":
                           k=n[:q]   #slicing m before .
                           f=n[q+1:] #slicing m after .
                           re1=len(f) 
                           w=int(k+f)/math.pow(10,re1)
                    try:
                        sum=int(m)/int(n)
                        global output2
                        output2=Label(r1,bg="green",text="{}".format(sum))
                        output2.place(x=5,y=100)
                        output2.config(font=("Algerian",25))

                    except:
                        try:
                          sum=u/w
                          output2=Label(r1,bg="green",text="{}".format(sum))
                          output2.place(x=5,y=100)
                          output2.config(font=("Algerian",25)) 
                        except:
                            try:
                               sum=u/int(n)
                               output2=Label(r1,bg="green",text="{}".format(sum))
                               output2.place(x=5,y=100)
                               output2.config(font=("Algerian",25))
                            except:
                                sum=int(m)/w
                                output2=Label(r1,bg="green",text="{}".format(sum))
                                output2.place(x=5,y=100)
                                output2.config(font=("Algerian",25))                     
        #scroll function==================================================================================================
        def sc():
            global txt
            txt=Tk()
            txt.title("STORE")
            txt.iconbitmap("C:\\Users\\HOME\\Desktop\\logo.ico")
            txt.resizable(0,0)
            scroll=Scrollbar(txt)
            scroll.pack(side=RIGHT,fill=Y)
            txt.geometry("500x450+500+120")
            txt1=Text(txt,width=500,height=450,bg="navy",fg="yellow",font="courier",selectbackground="red",yscrollcommand=scroll.set)
            scroll.config(command=txt1.yview)
            txt1.insert(INSERT,"###############################################\n")
            txt1.insert(INSERT,"============WELCOME TO DIVISION WINDOW========================================================\n")
            try:
                txt1.insert(INSERT,"{}\n".format(operator))
                txt1.insert(INSERT,"{}".format(sum))
            except:
                txt1.insert(INSERT,"{}".format("NONE"))
            txt1.config(state="disabled")
            txt1.pack()
            txt.mainloop()
        #==scroll=========================================================================================================
        scr=Button(r2,text="STORE RESULT",bg="gray25",width=12,command=sc)
        scr.place(x=300,y=80)
        scr.config(font=("courier",19))
        def buttonin(number):
            global operator
            operator=operator + str(number)
            var.set(operator)
        def mc():
            try:
               output=Label(r1,bg="green",text="                                                        ")
               output.place(x=5,y=100)
               output.config(font=("Algerian",25))  
            except:
                print("")     
        def clear2():
            global operator
            try:
                output2.destroy()
            except:
                print("")              
            if operator!="":
                output2.destroy()
                
                operator=""
                var.set("")
                
       #1st Entry==============================================     
        var=StringVar()
        entry=Entry(r1,bg="green",textvariable=var,width=40)
        entry.place(x=5,y=50)
        entry.config(font=("Algerian",25))
        #button 1
        
        one=Button(r2,text="  1   ",bg="gray25",fg="yellow",command=lambda:buttonin(1))
        one.place(x=5,y=5)
        one.config(font=("Algerian",25))
        #button 2
            
        two=Button(r2,text="  2   ",bg="gray25",fg="yellow",command=lambda:buttonin(2))
        two.place(x=102,y=5)
        two.config(font=("Algerian",25))        
        #button 3
        
        three=Button(r2,text="  3   ",bg="gray25",fg="yellow",command=lambda:buttonin(3))
        three.place(x=200,y=5)
        three.config(font=("Algerian",25))
        #button 4
        
        four=Button(r2,text="  4   ",bg="gray25",fg="yellow",command=lambda:buttonin(4))
        four.place(x=5,y=80)
        four.config(font=("Algerian",25))
        #button 5
        
        five=Button(r2,text="  5   ",bg="gray25",fg="yellow",command=lambda:buttonin(5))
        five.place(x=102,y=80)
        five.config(font=("Algerian",25))
        #button 5
        
        six=Button(r2,text="  6   ",bg="gray25",fg="yellow",command=lambda:buttonin(6))
        six.place(x=200,y=80)
        six.config(font=("Algerian",25))
        #button 7
        
        seven=Button(r2,text="  7   ",bg="gray25",fg="yellow",command=lambda:buttonin(7))
        seven.place(x=5,y=155)
        seven.config(font=("Algerian",25))
        #button 8
        eight=Button(r2,text="  8   ",bg="gray25",fg="yellow",command=lambda:buttonin(8))
        eight.place(x=102,y=155)
        eight.config(font=("Algerian",25))
        #button 9
        
        nine=Button(r2,text="  9   ",bg="gray25",fg="yellow",command=lambda:buttonin(9))
        nine.place(x=200,y=155)
        nine.config(font=("Algerian",25))
        #button 0
        
        zero=Button(r2,text="  0   ",bg="gray25",fg="yellow",command=lambda:buttonin(0))
        zero.place(x=105,y=230)
        zero.config(font=("Algerian",25))
        #master clear=====================================================================================================
        cm=Button(r2,text="AC",bg="gray25",fg="yellow",command=mc)
        cm.place(x=390,y=5)
        cm.config(font=("Algerian",23))
        #button clear

        clear=Button(r2,text="  C  ",bg="gray25",fg="yellow",command=clear2)
        clear.place(x=200,y=230)
        clear.config(font=("Algerian",25))  
        #DECIMAL BUTTON========================================================
        dec=Button(r2,text="  .  ",bg="gray25",fg="yellow",command=lambda:buttonin("."))
        dec.place(x=300,y=5)
        dec.config(font=("Algerian",23)) 
        #button =

        result=Button(r2,text="  =  ",bg="gray25",fg="yellow",command=result5)
        result.place(x=300,y=230)
        result.config(font=("Algerian",25))
        #back button destroys button canvas.
        def bback():
            r2.destroy()
            entry.destroy()       
            try:
                output.destroy()
            except:
                print("")
                
        back=Button(r2,text="back",bg="gray25",fg="yellow",command=bback)
        back.place(x=5,y=230)
        back.config(font=("Algerian",25))
        #+++++++ BUTTON=======================
        plus=Button(r2,text="  /  ",bg="gray25",fg="yellow",command=lambda:buttonin("/"))
        plus.place(x=395,y=230)
        plus.config(font=("Algerian",25))        
#DIVISION BUTTON======================================================================================
    into=Button(r,text="   /   ",bg="OrangeRed2",command=divide)
    into.place(x=390,y=5)
    into.config(font=("Algerian",25))    
#POWER====================================================================================================================================================
    def pow():
        r2=Canvas(r,bg="brown4",width=500,height=450)
        r2.place(x=0,y=0)
        def result5():
            global sum
            le=len(str(operator))
            for i in range(0,le):
                if operator[i]=="^":
                    global out
                    m=operator[:i] #for taking the values of before + sign
                    n=operator[i+1:] #for taking the values of after + sign
                    r=len(m)
                    tr=len(n)
                    global w
                    global u
                    for y in range(0,r):
                        if m[y]==".":
                           k=m[:y]   #slicing m before .
                           f=m[y+1:] #slicing m after .
                           re=len(f) 
                           u=int(k+f)/math.pow(10,re) #using the concept that 44.55 is the answer from 4455/100(where denominator is power of 10 raised to the no after decimal
                           
                    for q in range(0,tr):
                        if n[q]==".":
                           k=n[:q]   #slicing m before .
                           f=n[q+1:] #slicing m after .
                           re1=len(f) 
                           w=int(k+f)/math.pow(10,re1)
                    try:
                        sum=math.pow(int(m),int(n))
                        global output2
                        output2=Label(r1,bg="green",text="{}".format(sum))
                        output2.place(x=5,y=100)
                        output2.config(font=("Algerian",25))

                    except:
                        try:
                          sum=math.pow(u,w)
                          output2=Label(r1,bg="green",text="{}".format(sum))
                          output2.place(x=5,y=100)
                          output2.config(font=("Algerian",25)) 
                        except:
                            try:
                               sum=math.pow(u,int(n))
                               output2=Label(r1,bg="green",text="{}".format(sum))
                               output2.place(x=5,y=100)
                               output2.config(font=("Algerian",25))
                            except:
                                sum=math.pow(int(m),w)
                                output2=Label(r1,bg="green",text="{}".format(sum))
                                output2.place(x=5,y=100)
                                output2.config(font=("Algerian",25))                     
        #scroll function==================================================================================================
        def sc():
            global txt
            txt=Tk()
            txt.title("STORE")
            txt.iconbitmap("C:\\Users\\HOME\\Desktop\\logo.ico")
            txt.resizable(0,0)
            scroll=Scrollbar(txt)
            scroll.pack(side=RIGHT,fill=Y)
            txt.geometry("500x450+500+120")
            txt1=Text(txt,width=500,height=450,bg="navy",fg="yellow",font="courier",selectbackground="red",yscrollcommand=scroll.set)
            scroll.config(command=txt1.yview)
            txt1.insert(INSERT,"###############################################\n")
            txt1.insert(INSERT,"============WELCOME TO DIVISION WINDOW========================================================\n")
            try:
                txt1.insert(INSERT,"{}\n".format(operator))
                txt1.insert(INSERT,"{}".format(sum))
            except:
                txt1.insert(INSERT,"{}".format("NONE"))
            txt1.config(state="disabled")
            txt1.pack()
            txt.mainloop()
        #==scroll=========================================================================================================
        scr=Button(r2,text="STORE RESULT",bg="gray25",width=12,command=sc)
        scr.place(x=300,y=80)
        scr.config(font=("courier",19))
        def buttonin(number):
            global operator
            operator=operator + str(number)
            var.set(operator)
        def mc():
            try:
               output=Label(r1,bg="green",text="                                                        ")
               output.place(x=5,y=100)
               output.config(font=("Algerian",25))  
            except:
                print("")     
        def clear2():
            global operator
            try:
                output2.destroy()
            except:
                print("")              
            if operator!="":
                output2.destroy()
                
                operator=""
                var.set("")
                
       #1st Entry==============================================     
        var=StringVar()
        entry=Entry(r1,bg="green",textvariable=var,width=40)
        entry.place(x=5,y=50)
        entry.config(font=("Algerian",25))
        #button 1
        
        one=Button(r2,text="  1   ",bg="gray25",fg="yellow",command=lambda:buttonin(1))
        one.place(x=5,y=5)
        one.config(font=("Algerian",25))
        #button 2
            
        two=Button(r2,text="  2   ",bg="gray25",fg="yellow",command=lambda:buttonin(2))
        two.place(x=102,y=5)
        two.config(font=("Algerian",25))        
        #button 3
        
        three=Button(r2,text="  3   ",bg="gray25",fg="yellow",command=lambda:buttonin(3))
        three.place(x=200,y=5)
        three.config(font=("Algerian",25))
        #button 4
        
        four=Button(r2,text="  4   ",bg="gray25",fg="yellow",command=lambda:buttonin(4))
        four.place(x=5,y=80)
        four.config(font=("Algerian",25))
        #button 5
        
        five=Button(r2,text="  5   ",bg="gray25",fg="yellow",command=lambda:buttonin(5))
        five.place(x=102,y=80)
        five.config(font=("Algerian",25))
        #button 5
        
        six=Button(r2,text="  6   ",bg="gray25",fg="yellow",command=lambda:buttonin(6))
        six.place(x=200,y=80)
        six.config(font=("Algerian",25))
        #button 7
        
        seven=Button(r2,text="  7   ",bg="gray25",fg="yellow",command=lambda:buttonin(7))
        seven.place(x=5,y=155)
        seven.config(font=("Algerian",25))
        #button 8
        eight=Button(r2,text="  8   ",bg="gray25",fg="yellow",command=lambda:buttonin(8))
        eight.place(x=102,y=155)
        eight.config(font=("Algerian",25))
        #button 9
        
        nine=Button(r2,text="  9   ",bg="gray25",fg="yellow",command=lambda:buttonin(9))
        nine.place(x=200,y=155)
        nine.config(font=("Algerian",25))
        #button 0
        
        zero=Button(r2,text="  0   ",bg="gray25",fg="yellow",command=lambda:buttonin(0))
        zero.place(x=105,y=230)
        zero.config(font=("Algerian",25))
        #master clear=====================================================================================================
        cm=Button(r2,text="AC",bg="gray25",fg="yellow",command=mc)
        cm.place(x=390,y=5)
        cm.config(font=("Algerian",23))
        #button clear

        clear=Button(r2,text="  C  ",bg="gray25",fg="yellow",command=clear2)
        clear.place(x=200,y=230)
        clear.config(font=("Algerian",25))  
        #DECIMAL BUTTON========================================================
        dec=Button(r2,text="  .  ",bg="gray25",fg="yellow",command=lambda:buttonin("."))
        dec.place(x=300,y=5)
        dec.config(font=("Algerian",23)) 
        #button =

        result=Button(r2,text="  =  ",bg="gray25",fg="yellow",command=result5)
        result.place(x=300,y=230)
        result.config(font=("Algerian",25))
        #back button destroys button canvas.
        def bback():
            r2.destroy()
            entry.destroy()       
            try:
                output.destroy()
            except:
                print("")
                
        back=Button(r2,text="back",bg="gray25",fg="yellow",command=bback)
        back.place(x=5,y=230)
        back.config(font=("Algerian",25))
        #+++++++ BUTTON=======================
        plus=Button(r2,text="  ^  ",bg="gray25",fg="yellow",command=lambda:buttonin("^"))
        plus.place(x=395,y=230)
        plus.config(font=("Algerian",25))        
#POWER BUTTON======================================================================================
    into=Button(r,text="  x^y  ",bg="OrangeRed2",command=pow)
    into.place(x=15,y=150)
    into.config(font=("Algerian",20))   
s=Button(r,text="START",bg="darkblue",fg="yellow",bd=15,width=10,height=5,command=opens)
s.place(x=190,y=70)
s.config(font=("HELVETICA",15))
root.mainloop()
