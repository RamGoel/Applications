

            #**** Made by RamGoel / Instagram @its_ramgoel / GitHub @RamGoel *****      






#**** Here are the Imports  *****

from genericpath import isfile               #**** For Checking File Availiblity  *****
from tkinter import *                        #**** For GUI   *****
from tkinter import messagebox               #**** For Errors and Warnings in POPUPS *****
import random                                #**** For generating a Unique ID *****






#**** Creating the App Window *****

root = Tk()
root.title("Student Managenent System - StudMG")
root.geometry("500x290")




#**** Callback Functions *****

def submit(): #**** Calls When Someone Clicks on Submit*****
    d = random.randrange(1, 1000)
    e = str(d)
    a = inp_2.get()
    b = inp_1.get()
    c = inp_3.get()

    if a == '' or b == '' or c == '':
        messagebox.showwarning("Empty Field", "fields cannot be Empty")
    else:
        f = open((e+'.txt'), 'w')
        f.write("{ ID : " + e + "}" + " { Enrollment No." + a + "}" +
                "{ Name :" + b + "}" + "{ Percentage :" + c + "}")
        f.close()
        inp_1.delete(0, END)
        inp_2.delete(0, END)
        inp_3.delete(0, END)
        messagebox.showinfo("Submitted", "Data Submitted!!")
        ida.config(text="Your ID is "+e)
        ida.after(5000, get1)


def get1():
    ida.destroy()


def view(): #**** Calls when Somone clicks on View Records*****

    top = Tk()
    top.geometry("500x260")
    top.title("ID Form")
    ip1 = Entry(top, font="lucida 20 ")
    ip1.insert(0, "Enter your ID :")
    ip1.pack()

    def click(*args):
        ip1.delete(0, END)

    def ViewData():
        a = ip1.get()

        try:  #**** Try catch to Handle String Input in ID Entry *****
            if int(a) < 1000:
                if isfile(a+".txt") == True:
                    f = open((a+".txt"), "r")
                    data = f.read()
                    label1 = Label(top, text=data, font="lucida 10 ").pack()
                else:
                    messagebox.showerror("Error", "No File Found")

            else:
                messagebox.showerror("Error", "Enter a Number ID")
        except:
            messagebox.showerror("Error", "Only Number Allowed")

    bt1 = Button(top, text="View my Data",
                 font="lucida 15 bold", command=ViewData)
    bt1.pack()
    label2 = Label(top, text=" Your Data is Here :",
                   font="lucida 10 bold").pack()
    ip1.bind("<Button-1>", click)


def Clear():  #**** Calls When Someone Clicks on Clear  *****
    inp_1.delete(0, END)
    inp_2.delete(0, END)
    inp_3.delete(0, END)



    #**** Callback Functions End Here *****







    #**** UI of the App Starts Here *****


frame_top = Frame(root, width=700, height=200,  #**** Title and Tagline Frame & Widgets  *****
                  background="gray", padx=10, pady=10)
frame_top.pack()

head = Label(frame_top, text="Welcome to StudMG",
             background="orange", font="lucida 30 bold", padx=500)
head.pack()
tagline = Label(frame_top, text="A Student Management System for Government Polytechnic Rampur",
                background="skyblue", font="lucida 10 bold", padx=500)
tagline.pack()


#**** Frame and Widgets for  Input Form   *****

frame_2 = Frame(root, bg="green", width=1500, height=200,).pack(ipady=30)
form_1 = Label(frame_2, text="Enter Enrollment Number :", bg="green",
               fg="white",  font="lucida 10 bold").place(x=40, y=110)
inp_2 = Entry(frame_2)
inp_2.place(x=240, y=110)

form_1 = Label(frame_2, text="Enter Student Name :", bg="green",
               fg="white",  font="lucida 10 bold").place(x=40, y=150)
inp_1 = Entry(frame_2)
inp_1.place(x=240, y=150)

form_1 = Label(frame_2, text="Enter Student Percentage :", bg="green",
               fg="white",  font="lucida 10 bold").place(x=40, y=190)
inp_3 = Entry(frame_2)
inp_3.place(x=240, y=190)

btn_1 = Button(frame_2, text="SUBMIT", bg="black", fg="white",
               font="lucida 10 bold", command=submit)
btn_1.place(x=40, y=220)


btn_2 = Button(frame_2, text="CLEAR", bg="black", fg="white",
               font="lucida 10 bold", command=Clear)
btn_2.place(x=140, y=220)


btn_3 = Button(frame_2, text="EXIT", bg="black", fg="white",
               font="lucida 10 bold", command=exit)
btn_3.place(x=240, y=220)


btn_4 = Button(frame_2, text="VIEW RECORDS", bg="black",
               fg="white", font="lucida 10 bold", command=view)
btn_4.place(x=340, y=220)

ida = Label(
    frame_2, text='         Your ID Comes Here(Copy Before it Disappears)          ')
ida.place(x=140, y=260)


root.mainloop() #**** This Line Starts the App Window *****



#**** UI of the app Ends Here *****



#**** Made by RamGoel / Instagram @its_ramgoel / GitHub @RamGoel *****