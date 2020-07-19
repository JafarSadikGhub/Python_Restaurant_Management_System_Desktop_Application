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
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.26)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.34)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.42)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.50)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.58)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.66)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",  selectbackground="#f2a343", font=font13)
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
        self.Label12.place(relx=0.35, rely=0.4)
        self.Label12 = tk.Label(master=top, text='Tamx :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.48)
        self.Label12 = tk.Label(master=top, text='Subtmtal :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.38, rely=0.56)
        self.Label12 = tk.Label(master=top, text='Totmal :', foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.64)

        #________ Entry Cost ____________
        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.467, rely= 0.33)
        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.516, rely= 0.41)
        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.467, rely= 0.5)
        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.479, rely= 0.57)
        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.466, rely= 0.65)


root = tk.Tk()
my_gui = App1(root)
root.mainloop()