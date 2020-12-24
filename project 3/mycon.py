from tkinter import*
def b(x):
    print("sex")
root=Tk()

root.title("MBSA")
root.geometry("1366x768")
q=Entry(root)
q.pack()
q.bind("<Return>",b)
