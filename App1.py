import tkinter as tk
from tkinter import Label, Button
import time

localtime = time.asctime(time.localtime(time.time()))
class App1:
    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        font10 = "{Courier New} 10 normal"
        font11 = "{U.S. 101} 30 bold"
        font12 = "Al-Aramco 11 bold " 
        font13 = "{Courier New} 10 bold "
        font14 = "{Segoe UI} 15 bold "
        font15 = "Arial 13 bold "
        font16 = "{Segoe UI} 13 bold "

        self.Label1 = tk.Label(master=top, text='Restaurant Management System For Doggos', background="#091833", font=font11, foreground="#f2a343")
        self.Label1.place(relx= 0.150, rely= 0.02, height=51, width=680)
        
        localtime1 = Label(master=top, text=localtime, background="#091833", font=font16, foreground="steel blue")
        localtime1.place(relx= 0.420, rely= 0.12)

        #____________ Label Food ______________
        
        self.Label2 = tk.Label(master=top, text='Order Num :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label2.place(relx=0.079, rely=0.25)
        self.Label2 = tk.Label(master=top, text='Fried Chimken :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label2.place(relx=0.044, rely=0.32)
        self.Label2 = tk.Label(master=top, text='Chimken Burgmer :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label2.place(relx=0.0135, rely=0.4)
        self.Label2 = tk.Label(master=top, text='Big Kimg Burgmer :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label2.place(relx=0.01155, rely=0.48)
        self.Label2 = tk.Label(master=top, text='Chimken Tamdoori :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label2.place(relx=0.00090, rely=0.56)
        self.Label2 = tk.Label(master=top, text='Veg Salaadm :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label2.place(relx=0.046, rely=0.64)
        self.Label2 = tk.Label(master=top, text='Drimks :', foreground="#1812c6", font=font12, background="#091833")
        self.Label2.place(relx=0.105, rely=0.71)
        
        #____________ Entry Food ___________________
        
        self.entry1 = tk.Entry(master=top, textvariable=rand, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.26)
        self.entry1 = tk.Entry(master=top, textvariable=friedchimken, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.34)
        self.entry1 = tk.Entry(master=top, textvariable=chimkenburgmer, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.42)
        self.entry1 = tk.Entry(master=top, textvariable=bigkimgburgmer, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.50)
        self.entry1 = tk.Entry(master=top, textvariable=chimkentamdoori, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.58)
        self.entry1 = tk.Entry(master=top, textvariable=vegsalaadm, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.66)
        self.entry1 = tk.Entry(master=top, textvariable=drimks, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.73)

        #_______________ Calc ________________
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.705, rely= 0.24, height=35, relwidth= 0.267 )

        self.Button1 = tk.Button(master=top, text= '''7''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''8''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.780, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''9''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.856, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''/''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.934, rely=0.34, height=44, width=37)
       
        self.Button1 = tk.Button(master=top, text= '''4''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.705, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''5''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.780, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''6''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.856, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''*''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.934, rely=0.44, height=44, width=37)
      
        self.Button1 = tk.Button(master=top, text= '''1''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.705, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''2''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.780, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''3''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.856, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''-''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.934, rely=0.54, height=44, width=37)

        self.Button1 = tk.Button(master=top, text= '''0''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.705, rely=0.64, height=35, width=146)
        self.Button1 = tk.Button(master=top, text= '''.''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.856, rely=0.64, height=35, width=67)
        self.Button1 = tk.Button(master=top, text= '''+''', background="#122c63", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.934, rely=0.64, height=35, width=37)

        self.Button1 = tk.Button(master=top, text= '''=''', background="#f2a343", font=font14, foreground="#ffffff", borderwidth="0")
        self.Button1.place(relx=0.705, rely=0.72, height=34, width=272)
        
        #__________ Cost _______________

        self.Label12 = tk.Label(master=top, text='Comst :', foreground="#f2a343", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.32)
        self.Label12 = tk.Label(master=top, text='Service Charmge :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.37, rely=0.4)
        self.Label12 = tk.Label(master=top, text='Tamx :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.48)
        self.Label12 = tk.Label(master=top, text='Subtmtal :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.38, rely=0.56)
        self.Label12 = tk.Label(master=top, text='Totmal :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.64)

        #________ Entry Cost ____________
        
        self.entry13 = tk.Entry(master=top, textvariable=comst, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.477, rely= 0.33)
        self.entry13 = tk.Entry(master=top, textvariable=servicecharmge, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.548, rely= 0.41, relwidth=0.087)
        self.entry13 = tk.Entry(master=top, textvariable=tamx, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.471, rely= 0.5, relwidth=0.164)
        self.entry13 = tk.Entry(master=top, textvariable=subtmtal, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.479, rely= 0.57, relwidth=0.1575)
        self.entry13 = tk.Entry(master=top, textvariable=totmal, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.481, rely= 0.65, relwidth=0.155)

        #_______ Control Button __________

        self.Button2 = tk.Button(master=top, text='PRICE', background='#e16740', font=font16, command=list1)
        self.Button2.place(relx=0.039, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='TOTAL', background='#e16740', font=font16)
        self.Button2.place(relx=0.156, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='RESET', background='#e16740', font=font16)
        self.Button2.place(relx=0.272, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='EXIT', background='#e16740', font=font16)
        self.Button2.place(relx=0.389, rely=0.86, height=34, width=107)
        
def list1():
    price = tk.Tk()
    price.geometry("300x250+350+200")
    price.title("Price List")
    price.configure(background="#091833")

    labelInfo = Label(price, text="ITEM", foreground="#bac8bd", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=0, column=0)
    labelInfo = Label(price, text="PRICE", foreground="#f2a343", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=0, column=3)
    labelInfo = Label(price, text="Fried Chimken", foreground="#bac8bd", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=1, column=0)
    labelInfo = Label(price, text="120", foreground="#f2a343", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=1, column=3)
    labelInfo = Label(price, text="Big Kimg Burgmer", foreground="#bac8bd", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=2, column=0)
    labelInfo = Label(price, text="499", foreground="#f2a343", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=2, column=3)
    labelInfo = Label(price, text="Chimken Tamdoori", foreground="#bac8bd", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=3, column=0)
    labelInfo = Label(price, text="350", foreground="#f2a343", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=3, column=3)
    labelInfo = Label(price, text="Veg Salaadm", foreground="#bac8bd", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=4, column=0)
    labelInfo = Label(price, text="220", foreground="#f2a343", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=4, column=3)
    labelInfo = Label(price, text="Drimks", foreground="#bac8bd", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=5, column=0)
    labelInfo = Label(price, text="33", foreground="#f2a343", font="Al-Aramco 12 bold", background="#091833")
    labelInfo.grid(row=5, column=3)
    




root = tk.Tk()

text_input = StringVar()
operator = ""

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)

def btnclr():
    global operator
    operator = ""
    text_input.set("")

def equals():
    global operator
    summ = str(eval(operator))
    text_input.set(summ)
    operator = ""

rand = StringVar()
friedchimken = StringVar()
friedchimken = StringVar()
chimkenbugmer = StringVar()
bigkimgburgmer = StringVar()
chimkentamdoori = StringVar()
vegsalaadm = StringVar()
drimks = StringVar()

comst = StringVar()
servicecharmge = StringVar()
tamx = StringVar()
subtmtal = StringVar()
totmal = StringVar()

my_gui = App1(root)
root.mainloop()

