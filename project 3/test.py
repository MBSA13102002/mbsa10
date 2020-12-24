def details(name,age,sub,mobno,passwd,confrm,add,dob):
    p=open("plasma.txt",'a')    
    p.write('\n--------------------------------------------------------------\n')
    p.write('NAME:-'+ name.upper()+'\n')  
    p.write('AGE:-'+ age.upper()+'\n')
    p.write('SUBJECT:-'+ sub.upper()+'\n')
    p.write('MOB.NO:-'+ mobno.upper()+'\n')
    p.write('PASSWORD:-'+ passwd.upper()+'\n')
    p.write('CONFIRM PASSWORD:-'+ confrm.upper()+'\n')
    p.write('ADDRESS:-'+ add.upper()+'\n')
    p.write('D.O.B:-'+ dob.upper()+'\n')
    p.write('\n--------------------------------------------------------------\n')
    p.close()

def find():
    w=open("bob.txt",'r')
    q=w.readlines()
    a=input("ENTER THE NAME OF THE STUDENT TO BE FOUND")
    for i in range(0,len(q)):
        if q[i]=='NAME:-'+a.upper()+'\n':
            print(q[i])
            print(q[i+1])
            print(q[i+2])
        else:
            print("not found")
       

