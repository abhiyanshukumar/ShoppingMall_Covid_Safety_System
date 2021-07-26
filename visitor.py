from re import L
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import cv2



class Visitor:
    def __init__(self, data):
        self.data = data
        root = Tk()
        self.root = root
        self.root.geometry("450x300")
        self.root.resizable(False, False)
        self.root.title("Visitor Data")
        self.root.configure(bg='#e07285')

        frame1 = Frame(self.root, bg='#48b064')
        frame1.place(x=25, y=25, width=400, height=250)

        title1 = Label(frame1, text=data[0], font="Lucid 16 bold", fg='green', bg='white')
        title1.place(x=5, y=5)

        title2 = Label(frame1, text=data[1], font="Lucid 16 bold", fg='green', bg='white')
        title2.place(x=5, y=50)

        title3 = Label(frame1, text=data[2], font="Lucid 16 bold", fg='green', bg='white')
        title3.place(x=5, y=100)

        title4 = Label(frame1, text=data[3], font="Lucid 16 bold", fg='green', bg='white')
        title4.place(x=5, y=150)

        title5 = Label(frame1, text=data[4], font="Lucid 16 bold", fg='green', bg='white')
        title5.place(x=5, y=200)

        title6 = Label(frame1, text=data[5], font="Lucid 16 bold", fg='green', bg='white')
        title6.place(x=5, y=250)




        self.root.mainloop()

# if __name__ == '__main__':
# 	Visitor()
	
