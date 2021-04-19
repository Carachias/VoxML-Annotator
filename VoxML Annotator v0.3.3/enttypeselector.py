from tkinter import StringVar
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import object_window
import programm_window
import attribute_window
import relation_window
import function_window
import help_window
import changelog_window
import inspector
import componentloader
import framer
from tkinter import PhotoImage
from tkinter import *



def starttheannotator():
    object_window.createwindow()
    programm_window.createwindow()
    attribute_window.createwindow()
    relation_window.createwindow()
    function_window.createwindow()


def quitapplication():
    framer.Window.destroy()


def createwindow():

    entity_types_bg_label = Label(framer.Topframe,image = framer.enttypeslabelpic, bg = "#a3ff8f", width = 557, height = 35)
    entity_types_bg_label.image = framer.enttypeslabelpic
    entity_types_bg_label.place (x = 0, y = 81)

    otherfuns_bg_label = Label(framer.Topframe,image = framer.otherfunslabelpic, bg = "#a3ff8f", width = 222, height = 35)
    otherfuns_bg_label.image = framer.otherfunslabelpic
    otherfuns_bg_label.place (x = 650, y = 81)

    htmlfuns_bg_label = Label(framer.Topframe,image = framer.htmlfunslabelpic, bg = "#a3ff8f", width = 394, height = 35)
    htmlfuns_bg_label.image = framer.htmlfunslabelpic
    htmlfuns_bg_label.place (x = 1150, y = 81)
    
    #entity_types_label = Label(framer.Topframe, text = "Entity Types:", foreground = "white", background = "#393939", font=(None, 14))
    #entity_types_label.place (x = 20, y = 86)

    loadvoxml_button = Button(framer.Topframe, text="Open VoxML", command = lambda: componentloader.loadcomponents())
    loadvoxml_button.config(image = framer.largebtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    loadvoxml_button.place ( x = 1150, y = 118 )
    
    loadhtml_button = Button(framer.Topframe, text="Open HTML", command = lambda: inspector.createwindow())
    loadhtml_button.config(image = framer.largebtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    loadhtml_button.place ( x = 1282, y = 118 )

    converthtml_button = Button(framer.Topframe, text="Convert HTML", command = lambda: componentloader.loadcomponents())
    converthtml_button.config(image = framer.largebtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    converthtml_button.place ( x = 1414, y = 118 )

    openhelp_button = Button(framer.Topframe, text="Help", command = lambda: help_window.createwindow())
    openhelp_button.config(image = framer.btnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    openhelp_button.place ( x = 650, y = 118 )

    openchangelog_button = Button(framer.Topframe, text="Changelog", command = lambda: changelog_window.createwindow())
    openchangelog_button.config(image = framer.btnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    openchangelog_button.place ( x = 762, y = 118 )
    
    quit_button = Button(framer.Topframe, text="exit", command = lambda: quitapplication())
    quit_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 14))
    #quit_button.place ( x = 1520, y = 7 )

    object_button = Button(framer.Topframe, text="Object", command = lambda: framer.Objframe.tkraise())
    object_button.config(image = framer.btnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    object_button.place ( x = 0, y = 118 )

    programm_button = Button(framer.Topframe, text="Programm", command = lambda: framer.Progrframe.tkraise())
    programm_button.config(image = framer.btnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    programm_button.place ( x = 112, y = 118 )

    attribute_button = Button(framer.Topframe, text="Attribute", command = lambda: framer.Attrframe.tkraise())
    attribute_button.config(image = framer.btnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    attribute_button.place ( x = 223, y = 118 )

    relation_button = Button(framer.Topframe, text="Relation", command = lambda: framer.Relatframe.tkraise())
    relation_button.config(image = framer.btnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    relation_button.place ( x = 335, y = 118 )

    function_button = Button(framer.Topframe, text="Function", command = lambda: framer.Funcframe.tkraise())
    function_button.config(image = framer.btnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 14))
    function_button.place ( x = 447, y = 118 )

    starttheannotator()


def main():
    createwindow()
main()
