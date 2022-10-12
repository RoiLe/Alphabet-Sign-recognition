#Import the required Libraries
from cProfile import label
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import bgcolor
from PIL import ImageTk, Image

from letterPrediction import process_program

#Create an instance of Tkinter frame
win = Tk(className = 'Alphabet sign language recognizer')

#Set the geometry of Tkinter frame
win.geometry("800x500")

#set the background color
win.configure(bg = 'black')

#signs image
def openSignImg():
    sign_image = Image.open('media\American-Sign-Language-alphabet image.png')
    resized_sign_image = sign_image.resize((300,400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_sign_image)
    label3 = tkinter.Label(image=photo)
    label3.image = photo
    label3.place_configure(x = 20, y = 60)

"""
    close the window. 
"""
def Close():
    win.destroy()
    #exit code


def start_program():
    process_program()


#create massages
text_msg1 = "Sign language recognizer"
text_msg2 = "This program recognize only English letters.\n*Please put your hand inside the square\n\t\t\t Enjoy!"

#display massages
L1 = Label(win, text= text_msg1, font=('Helvetica',25, 'bold')).pack(pady=20)
L2 = Label(win, text= text_msg2, font=('Helvetica',15)).place(x = 340, y = 100)

#create All the buttons
start_btn = ttk.Button(win, text= "start", command= start_program) 
exit_btn = ttk.Button(win, text= "exit", command = Close)
sign_button = ttk.Button(win, text = "sign langauage", command=openSignImg, bg = '#A877BA')

#display buttons
start_btn.place(x = 550, y = 380)
exit_btn.place(x = 700, y = 450)
sign_button.place(x = 450, y = 380)

win.mainloop()