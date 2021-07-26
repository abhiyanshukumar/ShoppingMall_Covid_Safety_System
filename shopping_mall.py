from re import L
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import glob
import os
import sys
import pyrebase
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, firestore
from PIL import ImageTk, Image
import datetime as dt
import cv2
from myvideocapture import App
from visitor import Visitor


class Shopping:
    def __init__(self, root4, mailid, pwd):
        self.root4 = root4
        self.root4.destroy()
        self.mailid = mailid
        self.pwd = pwd
        root = Tk()
        self.root = root
        self.root.title("Shopping MAll")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#e07285')

        # ==== Firebase =====
        firebaseConfig = {
            "apiKey": "AIzaSyCXM0Y_xEQLP98zt9QClyWVWuFA1UJA6R4",
            "authDomain": "shoppingmall-28b2c.firebaseapp.com",
            "databaseURL": "https://shoppingmall-28b2c-default-rtdb.firebaseio.com",
            "projectId": "shoppingmall-28b2c",
            "storageBucket": "shoppingmall-28b2c.appspot.com",
            "messagingSenderId": "495932885785",
            "appId": "1:495932885785:web:71e597b2d5bdce3e819388"
        }
        # ==========Initialize Firebase================
        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()
        self.db = firebase.database()

        self.user = self.auth.sign_in_with_email_and_password(self.mailid, self.pwd)
        self.store = firebase.storage()

        # ====== Main Background Image =====
        self.path4 = os.path.normpath("images//covid.png")
        bg = Image.open(self.path4)
        self.image1 = ImageTk.PhotoImage(bg)
        canvas1 = Canvas(self.root, width=1200, height=600)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=self.image1, anchor="nw")

        # ========= creating 3 frame top left and right ===========
        self.fs1 = Label(self.root, text="Welcome to Mask detection System", font='lucid 20 bold', bg='blue',
                         fg='white')
        self.fs1.place(x=300, y=10)

        self.fs2 = Frame(self.root, width=400, height=450, bg='black', bd=3)
        self.fs2.place(x=50, y=80)
        self.fs3 = Frame(self.root, width=600, height=450, bg='black')
        self.fs3.place(x=550, y=80)

        # ==== left frame background =====
        bg2 = Image.open('images/tcovid2.png')
        self.image2 = ImageTk.PhotoImage(bg2)
        canvas2 = Canvas(self.fs2, width=400, height=450)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=self.image2, anchor="nw")

        # ===== Creating variable for entry widget =====
        self.n1 = StringVar()
        self.m1 = IntVar()
        self.c1 = StringVar()
        self.g1 = StringVar()
        self.id1 = StringVar()
        self.visit1 = StringVar()
        self.drop1 = StringVar()
        options = ["Aadhaar Card", "Driving License", "Pan Card", "Voter Id"]
        self.drop1.set('select from here..')
        self.n1.set("")
        self.m1.set("")
        self.c1.set("")
        self.g1.set("")
        self.id1.set("")

        # ======= visitors frame =============
        self.lv1 = Label(self.fs2, text="Visitors Entry Form", font='lucid 15 bold', bg='blue', fg='white')
        self.lv1.place(x=80, y=15)

        # ===== Name =====
        self.lv2 = Label(self.fs2, text="Full Name:", font='lucid 15 normal', fg='blue')
        self.lv2.place(x=10, y=80)
        self.lv2e = Entry(self.fs2, textvariable=self.n1, font='lucid 12 normal')
        self.lv2e.place(x=160, y=80, height=28)

        # ===== Mobile =====
        self.lv3 = Label(self.fs2, text="Mobile No:", font='lucid 15 normal', fg='blue')
        self.lv3.place(x=10, y=130)
        self.lv3e = Entry(self.fs2, textvariable=self.m1, font='lucid 12 normal')
        self.lv3e.place(x=160, y=130, height=28)

        # ==== Coming From ====
        self.lv4 = Label(self.fs2, text="Coming From:", font='lucid 15 normal', fg='blue')
        self.lv4.place(x=10, y=180)
        self.lv4e = Entry(self.fs2, textvariable=self.c1, font='lucid 12 normal')
        self.lv4e.place(x=160, y=180, height=28)

        # ==== Where they will go ====
        self.lv5 = Label(self.fs2, text="Will go to:", font='lucid 15 normal', fg='blue')
        self.lv5.place(x=10, y=230)
        self.lv5e = Entry(self.fs2, textvariable=self.g1, font='lucid 12 normal')
        self.lv5e.place(x=160, y=230, height=28)

        # ==== Id card  ====
        self.lv6 = Label(self.fs2, text="Select Id:", font='lucid 15 normal', fg='blue')
        self.lv6.place(x=10, y=280)
        self.drop = OptionMenu(self.fs2, self.drop1, *options, command=self.fun_drop)
        self.drop.configure(width=20)
        self.drop.place(x=160, y=280)
        self.x1 = self.drop1.trace_add('write', lambda *args: self.drop1.set(self.drop1.get()))

        # ==== Id Number  ====
        self.lv7 = Label(self.fs2, text="Enter Id:", font='lucid 15 normal', fg='blue')
        self.lv7.place(x=10, y=315)
        self.lv7e = Entry(self.fs2, textvariable=self.id1, font='lucid 12 normal')
        self.lv7e.place(x=160, y=315, height=25)

        # =========== Current Date time =============
        self.lv7 = Label(self.fs2, text="Visiting on:", font='lucid 15 normal', fg='blue')
        self.lv7.place(x=10, y=350)
        self.now = dt.datetime.now()
        self.d = self.now.strftime("%d-%m-%Y %H:%M")
        self.w = Label(self.fs2, text=f"{self.d}", fg="black", font="lucid 15 normal")
        self.w.place(x=160, y=350)

        # ==== submit data ======
        self.bv1 = Button(self.fs2, text="Add", font='lucid 15 normal', fg='blue', cursor='hand1', command=self.add)
        self.bv1.configure(width=8)
        self.bv1.place(x=40, y=400)
        self.bv2 = Button(self.fs2, text="Clear", font='lucid 15 normal', fg='blue', cursor='hand1', command=self.clear)
        self.bv2.configure(width=8)
        self.bv2.place(x=200, y=400)
        self.bv3 = Button(self.root, text="Search Visitors By name", font='lucid 15 normal', fg='blue', cursor='hand1',
                          bd=3, command=self.fun_search_visitor)
        self.bv3.configure(width=29)
        self.bv3.place(x=50, y=540)

        self.my_user = self.db.child("users").child("Sam")

        # === mask detection frame ==calling my video capture class  ======
        App(self.fs3, 600, 450)
        self.root.mainloop()

    # ==== Get value of drop down button =====
    def fun_drop(self, value):
        print(value)

    # ==== Serch visitors info if they visited before =====   
    def fun_search_visitor(self):
        self.v = simpledialog.askstring("visitor", prompt="Enter your full name")
        # print(self.v)
        # print(self.db.get(self.user['idToken']))
        x = self.my_user.child(self.v).get()
        print(x)
        if x:
            info_ = []
            y = dict(x.val().items())
            print(x)

            name_ = "Name: {}".format(y['name'])
            info_.append(name_)

            visit_ = y['visited on'].split(" ")
            visit_1 = "Visited on: {} at {}".format(visit_[0], visit_[1])
            info_.append(visit_1)

            came_ = "Came from: {}".format(y['coming from'])
            info_.append(came_)

            went_ = "Went to: {}".format(y['going to'])
            info_.append(went_)

            id_ = y['Id no'].split(" ")
            id__ = "{}_{}: {}".format(id_[0], id_[1], id_[2])
            info_.append(id__)

            mobile_ = "Mobile No: {}".format(y['mobile'])
            info_.append(mobile_)

            info_1 = info_[0] + "\n" + info_[1] + "\n" + info_[2] + "\n" + info_[3] + "\n" + info_[4] + "\n" + info_[5]
            self.info_2 = info_
            self.fun_visitor()
        else:
            messagebox.showinfo("visitor", "Visitor not found")


    # ==== Clear data =====
    def clear(self):
        self.n1.set("")
        self.m1.set("")
        self.c1.set("")
        self.g1.set("")
        self.drop1.set('select from here..')

    # ==== Add data to database ====
    def add(self):
        data = {
            "name": self.n1.get(),
            "mobile": self.m1.get(),
            "coming from": self.c1.get(),
            "going to": self.g1.get(),
            "visited on": self.w.cget("text"),
            "Id no": self.drop1.get() + " " + self.id1.get()
        }
        self.my_user.child(self.n1.get()).set(data)

    # === Display visitor information ===
    def fun_visitor(self):
        Visitor(self.info_2)

