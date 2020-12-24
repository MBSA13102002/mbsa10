
details(j.get(),k.get(),d.get(),a1.get(),f.get(),b.get(),c2.get(),c4.get(),c5.get(),e8.get(1.0, END))
            e10.destroy()
            e9.destroy()
            e8.destroy()
            e7.destroy()
            e6.destroy()
            e5.destroy()
            e4.destroy()
            e3.destroy()
            e2.destroy()
            e1.destroy()
            b_1()
            ans=m.askquestion("PHOTO","DO YOU WANT TO UPLOAD YOUR PHOTO")
            if ans=='yes':
                dot2=Canvas(root1,bg="white",width=1366,height=690)
                dot2.place(x=0,y=0)
                my1=PhotoImage(file='C:\\Users\\M PARTH\\Desktop\\pad1.gif')
                dot2.create_image(0, 0, anchor = NW, image=my1)
                #========================================                
                dot1=Canvas(dot2,bg="blue",width=250,height=250)
                dot1.place(x=35,y=400)
                dot3=Canvas(dot2,bg="brown",width=250,height=250)
                dot3.place(x=35,y=50)
                my2=PhotoImage(file='C:\\Users\\M PARTH\\Desktop\\uy.gif')
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
                    b=g1.get()
                    root1.update_idletasks()
                    global my_image1
                    my_image1=PhotoImage(file='C:\\Users\\M PARTH\\Desktop\\'+b+'.gif')
                    dot1.create_image(13, 10, anchor = NW, image=my_image1)
                    a2.destroy()
                    ab.destroy()
                    root1.mainloop()
                corona()
            elif ans=='no':
                ask1=m.showinfo("SUCCESS","ACCOUNT CREATED SUCCESSFULLY!!!")
                ask2=m.showinfo("LOGIN","MOVE BACK TO TEACHER LOGIN CORNER")
