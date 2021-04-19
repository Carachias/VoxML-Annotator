from tkinter import StringVar
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import framer
    
def createwindow():

    info1_label = Label(framer.Changelogframe, text = "VERSION 0.3.0 IS HERE!", foreground = "white", background = "#404040", font=(None, 12))
                       
    info1_label.place (x = 20, y = 90)

    info2_label = Label(framer.Changelogframe, text = "Reskinned UI, Bugfixes, Componentlist and much more", foreground = "white", background = "#404040", font=(None, 12))
    info2_label.place (x = 30, y = 120)

    info3_label = Label(framer.Changelogframe, text = "NEW IN VERSION 0.2.2:", foreground = "white", background = "#404040", font=(None, 12))
    info3_label.place (x = 20, y = 180)

    info4_label = Label(framer.Changelogframe, text = "completely new UI, \n"
                        "everything is now organized in one window instead of multiple \n"
                        "smaller ones!", foreground = "white", background = "#404040", font=(None, 12))
                        
    info4_label.place (x = 30, y = 210)

    info5_label = Label(framer.Changelogframe, text = "This changelog is also new! \n"
                        "In here you can find all the news about the latest update of the \n"
                        "VoxML Annotator", foreground = "white", background = "#404040", font=(None, 12))
                        
    info5_label.place (x = 30, y = 280)

    framer.Changelogframe.tkraise()
