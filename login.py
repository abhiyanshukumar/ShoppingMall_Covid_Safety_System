from tkinter import *
from tkinter import messagebox
import tkinter as tk
import glob
import os
from PIL import ImageTk, Image
import pyrebase
from tkinter import simpledialog
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, firestore
from getpass import getpass
from shopping_mall import Shopping


class Login:
    def __init__(self, root3):
        self.root3 = root3
        self.root3.destroy()
        root=Tk()
        self.root = root
        self.root.title("Registration ")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#5bb562')
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
        frame1 = Frame(self.root, bg='white')
        frame1.place(x=100, y=50, width=400, height=400)
        frame2 = Frame(frame1, width=400, height=80, bg="#48944e")
        frame2.place(x=0, y=0)
        # ============= Photo Icon ==================
        self.path2 = os.path.normpath("images//i1.png")
        self.path3 = os.path.normpath("images//i2.png")
        load1 = Image.open(self.path2)
        load2 = Image.open(self.path3)
        render1 = ImageTk.PhotoImage(load1)
        render2 = ImageTk.PhotoImage(load2)

        title1 = Label(frame2, text="Login", font="Lucid 30 bold", fg='green', bg='white')
        title1.place(x=120, y=15)

        frame3 = Frame(frame1, width=50, height=50, bd=0)
        frame3.place(x=50, y=120)
        l1 = Label(frame3, image=render1)
        l1.image = render1
        l1.place(x=0, y=0)

        frame4 = Frame(frame1, width=50, height=50, bd=0)
        frame4.place(x=50, y=200)
        l2 = Label(frame4, image=render2)
        l2.image = render2
        l2.place(x=0, y=0)

        # ============= input for email and password ===============
        self.e1 = Entry(frame1, font="lucid 15 normal")
        self.e1.place(x=110, y=120, height=50)
        self.e2 = Entry(frame1, font="lucid 15 normal", show="*")
        self.e2.place(x=110, y=200, height=50)

        # ====== Forgot Password Button ===================
        btnf = Button(frame1, text='Forgot password?? click here..', font="lucid 6", bd=0, command=self.forgotp)
        btnf.place(x=115, y=260)

        # ======== getting email and password and authenticating =====
        btns = Button(frame1, text='Authenticate', font="lucid 20", bg='green', fg='white', command=self.authL)
        btns.place(x=130, y=290)

        self.root.mainloop()

    def authL(self):
        userL = self.auth.sign_in_with_email_and_password(self.e1.get(), self.e2.get())
        exist = self.auth.current_user
        x = 0
        if exist:
            self.funshop()
        else:
            self.auth.send_email_verification(userL['idToken'])
            print("check your mail")

    def forgotp(self):
        self.p = simpledialog.askstring("password reset", prompt="Enter your emailId")
        self.auth.send_password_reset_email(self.p)
        messagebox.showinfo('Password', "Mail has been sent for password reset.", parent=self.root)



    def funshop(self):
        Shopping(self.root,self.e1.get(),self.e2.get())

