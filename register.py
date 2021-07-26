from tkinter import *
from tkinter import messagebox
import tkinter as tk
import glob
import os
from PIL import ImageTk, Image
import pyrebase
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, firestore
from getpass import getpass
from login import Login


class Register:
    def __init__(self, root, root2):
        self.root2 = root2
        self.root2.destroy()
        self.root = root
        self.root.title("Registration ")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#116928')
        self.e = 0
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0

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
        # # =======Bg Image=========
        # self.img = Image.open('bg2.png')
        # self.bg = ImageTk.PhotoImage(self.img)
        # bg = Label(self.root, image=self.bg).place(x=0, y=0)

        # =======Register Frame===========
        frame1 = Frame(self.root, bg='#dbba5e')
        frame1.place(x=150, y=100, width=700, height=400)

        title1 = Label(frame1, text="Register Here", font="Lucid 30 bold", fg='green').place(x=200, y=10)
        first_name = Label(frame1, text="First Name", font="Lucid 10", fg='black').place(x=150, y=90)
        last_name = Label(frame1, text="Last Name", font="Lucid 10", fg='black').place(x=400, y=90)
        email_id = Label(frame1, text="Email Address", font="Lucid 10", fg='black').place(x=150, y=160)
        phone_no = Label(frame1, text="Mobile No.", font="Lucid 10", fg='black').place(x=400, y=160)
        password = Label(frame1, text="Password", font="Lucid 10", fg='black').place(x=150, y=230)
        password = Label(frame1, text="Confirm Password", font="Lucid 10", fg='black').place(x=400, y=230)

        # ===============Input variable declaration===============================
        self.fnameE = Entry(frame1, font=('calibre', 10, 'normal'), relief=GROOVE, bd=2)
        self.fnameE.place(x=150, y=110)
        self.lnameE = Entry(frame1, font=('calibre', 10, 'normal'), relief=GROOVE, bd=2)
        self.lnameE.place(x=400, y=110)

        self.emailE = Entry(frame1, font=('calibre', 10, 'normal'), relief=GROOVE, bd=2)
        self.emailE.place(x=150, y=180)
        self.phoneE = Entry(frame1, font=('calibre', 10, 'normal'), relief=GROOVE, bd=2)
        self.phoneE.place(x=400, y=180)

        self.pwdE = Entry(frame1, show="*", font=('calibre', 10, 'normal'), relief=GROOVE, bd=2)
        self.pwdE.place(x=150, y=250)
        phelp = Button(frame1, text="?", bg='#dbba5e', bd=0, font=('calibre', 10, 'bold'), fg='blue', \
                       command=self.help).place(x=320, y=248)
        self.cnfpwdE = Entry(frame1, show="*", font=('calibre', 10, 'normal'), relief=GROOVE, bd=2)
        self.cnfpwdE.place(x=400, y=250)

        # =========Submit Button====================
        btn1 = Button(frame1, text="Submit", bd=2, relief=RAISED, command=self.regData).place(x=320, y=300)
        btnl = Button(frame1, text='Already have an account?? go to Login Page', font="lucid 10", bd=0, command=self.funlogin)
        btnl.place(x=200, y=350)

    def regData(self):
        if self.fnameE.get() == "" or self.lnameE.get() == "" or self.emailE.get() == "" or self.phoneE.get() == "" \
                or self.pwdE.get() == "" or self.cnfpwdE.get() == "":
            messagebox.showinfo("Error", "All fields are required", parent=self.root)
        else:
            self.emailValidaton()
            self.pwdcnfpwd()
            self.pwdmatch()
            self.phonevalid()
            if self.e == 1 and self.p1 == 1 and self.p2 == 1 and self.p3 == 1:
                self.createUser()
                messagebox.showinfo("congrats", "User Created", parent=self.root)
                self.funlogin()

    # ==========Checking if email is valid =============
    def emailValidaton(self):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(regex, self.emailE.get()):
            self.e = 1
        else:
            messagebox.showwarning("Error", "InValid Email", parent=self.root)

    # ============== checking validity of password ===============
    def pwdcnfpwd(self):
        password = self.pwdE.get()
        flag = 0
        while True:
            if len(password) < 8:
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                self.p1 = 1
                break
        if flag == -1:
            messagebox.showerror("Error in password", "not a valid password", parent=self.root)

    # ======= matching both password ====================
    def pwdmatch(self):
        if self.pwdE.get() == self.cnfpwdE.get():
            self.p2 = 1
        else:
            messagebox.showerror("Password match", "Password & confirm password doesn't match", parent=self.root)

    # ======= show password condition =================
    def help(self):
        messagebox.showinfo("Password", "1.Minimum 8 characters.\n2.The alphabets must be between [a-z]\n3.At least\
         one alphabet should be of Upper Case [A-Z]\n4.At least 1 number or digit between [0-9].\n", parent=self.root)

    # =========checking phone no validity================
    def phonevalid(self):
        if re.match(r'[789]\d{9}$', self.phoneE.get()):
            self.p3 = 1
        else:
            messagebox.showwarning("phone_no", "Phone No is not valid", parent=self.root)

    def createUser(self):
        user = self.auth.create_user_with_email_and_password(self.emailE.get(), self.pwdE.get())
        print("success")

    def funlogin(self):
        Login(self.root)