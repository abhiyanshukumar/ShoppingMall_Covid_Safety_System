from re import L
from tkinter import *
import tkinter as tk
import glob
import os
import sys
from register import Register
from login import Login
from PIL import ImageTk, Image


class App:
    def __init__(self, root):
        self.root = root
        self.hidden = 0
        self.root.geometry("1200x600")
        self.root.title("Shopping Mall Covid Safety System")
        # self.root.resizable(False, False)
        self.path1 = os.path.normpath("images//bg1.png")
        self.image2 = Image.open(self.path1)
        self.image1 = ImageTk.PhotoImage(self.image2)
        self.panel1 = Label(self.root, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')
        self.panel1.image = self.image1

        self.f1 = Frame(self.panel1, width="1000", height='100')
        # ======= shopping mall label====
        self.l1 = Label(self.f1, font='arial 40 bold', text="Shopping Mall Covid Safety System ", bd=10)
        self.l1.pack()
        self.f1.pack(side=TOP)
        self.reglogin()
        # self.delay()

    def reglogin(self):
        self.l2 = Label(self.panel1, text="welcome", fg="red", font="lucid 30 bold")
        self.l2.place(x=600, y=200)
        self.f = Frame(self.panel1, width="300", height="100")

        self.l3 = Label(self.f, text="New Here...??", fg="black", font="lucid 10", bd=10)
        self.l3.pack()
        self.btn1 = Button(self.f, text="Register", bg="#b85b56", font="lucid 30 bold", relief=RAISED, bd=10,
                           command=self.funreg)
        self.btn1.pack()
        self.f.place(x=350, y=300)
        self.ff = Frame(self.panel1, width=300, height=100)
        self.l4 = Label(self.ff, text="Already Registered??", fg="black", font="lucid 10", bd=10)
        self.l4.pack()
        self.btn2 = Button(self.ff, text="  Login  ", bg="#b85b56", font="lucid 30 bold", relief=RAISED, bd=10, command=self.funlogin)
        self.btn2.pack()
        self.ff.place(x=820, y=300)

    def delay(self):
        self.root.after(1500, self.reglogin)

    def funreg(self):
        root1 = Tk()
        Register(root1, self.root)
        root1.mainloop()
        quit()

    def funlogin(self):
        Login(self.root)



if __name__ == '__main__':
    mall = Tk()
    app = App(mall)
    mall.mainloop()
