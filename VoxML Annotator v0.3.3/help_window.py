from tkinter import StringVar
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import framer
   
    
def createwindow():

    info1_label = Label(framer.Helpframe, text = "Hover over entrys or buttons to view tooltips!", foreground = "white", background = "#404040", font=(None, 12))
                       
    info1_label.place (x = 16, y = 80)

    info2_label = Label(framer.Helpframe, text = "components, habitats, affordance formulas, \n"
                        "constraints and more can be added by filling their \n"
                        "inputs and pressing the corresponding 'add' button", foreground = "white", background = "#404040", font=(None, 12))
    info2_label.place (x = 16, y = 120)

    info3_label = Label(framer.Helpframe, text = "not every entry has to be filled. optional ones \n"
                        "can be found by using the tooltip", foreground = "white", background = "#404040", font=(None, 12))
    info3_label.place (x = 16, y = 190)

    info4_label = Label(framer.Helpframe, text = "Press the 'clear' button to discard all changes \n"
                        "on the current file. this also resets the lists of\n"
                        "added components, habitats and affordance formulas.", foreground = "white", background = "#404040", font=(None, 12))
                        
    info4_label.place (x = 16, y = 240)

    info5_label = Label(framer.Helpframe, text = "Press the 'save' button to save all changes on \n"
                        "the current file to a VoxML conform .xml file", foreground = "white", background = "#404040", font=(None, 12))
                        
    info5_label.place (x = 16, y = 310)


    framer.Helpframe.tkraise()
  

