from tkinter import StringVar
from tkinter import IntVar
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import xml.etree.ElementTree as ET
import xml.dom.minidom as  minidom
from io import BytesIO
import enttypeselector
import tooltip
import framer
from tkinter import *


#-----------------------------------------------MANDATORY-LISTS--------------------------------------------------

arglist = []


#-----------------------------------------------PRETTIFY-AND-SAVE-------------------------------------------------

def prettify(elem, filename):
    rough_string = ET.tostring(elem, 'us-ascii')
    reparsed = minidom.parseString(rough_string)
    rep = reparsed.toprettyxml(encoding='us-ascii', indent="\t").decode()
    print (rep)
    text_file = open(filename + ".xml", "w")
    text_file.truncate()
    n = text_file.write(rep)
    text_file.close()


#-----------------------------------------------ADD-TO-XML-TREE-----------------------------------------------
   


#-----------------------------------------------CREATE-XML-TREE-------------------------------------------------
        
def createtree(pred, argtyp, argvar, ref, mapp, space, axis, arity):
    global arglist
    VoxML = ET.Element("VoxML")
    VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
    VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")
    
    Entity = ET.SubElement(VoxML, "Entity", Type = "Function")

    Lex = ET.SubElement(VoxML, "Lex")
    Pred = ET.SubElement(Lex, "Pred")
    Pred.text = pred

    Type = ET.SubElement(VoxML, "Type")
    Args = ET.SubElement(Type, "Args")
    for i in arglist:
        new_arg = ET.SubElement(Args, "Arg", Value = i)
    Referent = ET.SubElement(Type, "Referent")
    Referent.text = ref
    Mapping = ET.SubElement(Type, "Mapping")
    Mapping.text = mapp
    Orientation = ET.SubElement(Type, "Orientation")
    Space = ET.SubElement(Orientation, "Space")
    Space.text = space
    Axis = ET.SubElement(Orientation, "Axis")
    Axis.text = axis
    Arity = ET.SubElement(Orientation, "Arity")
    Arity.text = arity
    
    prettify(VoxML, pred)


#-----------------------------------------------BUTTON-FUNCTIONS------------------------------------------------
    
def addargument(vartyp, varname, window):
    global arglist
    fullarg = varname.get() + ":" + vartyp.get()
    arglist.append(fullarg)
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, "Argument has been added!")
   
    
def getvals(pred, argtyp, argvar, ref, mapp, space, axis, arity):
    predstring = pred.get()
    argtypstring = argtyp.get()
    argvarstring = argvar.get()
    refstring = ref.get()
    mapstring = mapp.get()
    spacestring = space.get()
    axisstring = axis.get()
    aritystring = arity.get()
    
    createtree(predstring, argtypstring, argvarstring, refstring, mapstring,
               spacestring, axisstring, aritystring)


def clearlists(argl, window):
    argl.clear()
    window.destroy()
    createwindow()


#-----------------------------------------------CREATE-MAIN-WINDOW------------------------------------------------
    
def createwindow():
    global arglist

    clearall_button = Button(framer.Funcframe, text="clear", command = lambda: clearlists(arglist, root))
    clearall_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    clearall_button.place ( x = 560, y = 590 )
    tooltip.CreateToolTip(clearall_button, text = 'Tooltip:\n\n'
                 'Klick this button to discard your modifications\n'
                 'and clear all checkboxes, option menus and text fields')

    exec_button = Button(framer.Funcframe, text="save", command = lambda: getvals(pred_entry, optionVarArgtype, argvar_entry, referent_entry,
                                                                      mapping_entry, optionVarSpace, axis_entry, arity_entry))
    exec_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    exec_button.place ( x = 560, y = 636 )
    tooltip.CreateToolTip(exec_button, text = 'Tooltip:\n\n'
                 'Klick this button to save your modifications\n'
                 'to a VoxML conform XML document')

    debug_textfield = tk.Text(framer.Funcframe, height=4, width=48)
    debug_textfield.configure(relief = RIDGE, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    debug_textfield.place ( x = 100, y = 590 )

    lex_label = Label(framer.Funcframe, text = "<Lex>", foreground = "white", background = "#404040", font=(None, 14))
    lex_label.place (x = 50, y = 50)

    pred_label = Label(framer.Funcframe, text = "Predicate:", foreground = "white", background = "#404040", font=(None, 12))
    pred_label.place (x = 100, y = 80)

    pred_entry = Entry(framer.Funcframe)
    pred_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    pred_entry.place (x = 190, y = 80)

    type_label = Label(framer.Funcframe, text = "<Type>", foreground = "white", background = "#404040", font=(None, 14))
    type_label.place (x = 50, y = 140)

    arguments_label = Label(framer.Funcframe, text = "Argument:", foreground = "white", background = "#404040", font=(None, 12))
    arguments_label.place (x = 100, y = 170)

    optionVarArgtype = StringVar()
    optionVarArgtype.set("agent")

    optionmenuargtype = OptionMenu(framer.Funcframe, optionVarArgtype, "agent", "agent", "location", "physobj")
    optionmenuargtype.place(x = 190, y = 170)
    optionmenuargtype.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))


    argvar_entry = Entry(framer.Funcframe, width = 4)
    argvar_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    argvar_entry.place (x = 370, y = 170)

    add_argument_button = Button(framer.Funcframe, text="add", command = lambda: addargument(optionVarArgtype, argvar_entry, debug_textfield))
    add_argument_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_argument_button.place ( x = 560, y = 168 )
    tooltip.CreateToolTip(add_argument_button, text = 'Tooltip:\n\n'
                 'Klick this button to add an argument\n'
                 'to the current function.')


    referent_label = Label(framer.Funcframe, text="Referent:", foreground = "white", background = "#404040", font=(None, 12))
    referent_label.place (x = 100, y = 200)

    referent_entry = Entry(framer.Funcframe)
    referent_entry.place (x = 190, y = 200)
    referent_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))


    mapping_label = Label(framer.Funcframe, text = "Mapping:", foreground = "white", background = "#404040", font=(None, 12))
    mapping_label.place (x = 100, y = 230)

    mapping_entry = Entry(framer.Funcframe)
    mapping_entry.place (x = 190, y = 230)
    mapping_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))

    orientation_label = Label(framer.Funcframe, text = "<Orientation>", foreground = "white", background = "#404040", font=(None, 14))
    orientation_label.place (x = 50, y = 290)

    space_label = Label(framer.Funcframe, text = "Space:", foreground = "white", background = "#404040", font=(None, 12))
    space_label.place (x = 100, y = 320)

    optionVarSpace = StringVar()
    optionVarSpace.set("world")

    optionmenuspace = OptionMenu(framer.Funcframe, optionVarSpace, "world", "world", "object")
    optionmenuspace.place(x = 190, y = 320)
    optionmenuspace.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))


    axis_label = Label(framer.Funcframe, text = "Axis:", foreground = "white", background = "#404040", font=(None, 12))
    axis_label.place (x = 100, y = 350)
    tooltip.CreateToolTip(add_argument_button, text = 'Tooltip:\n\n'
                 'add a + or - to the axis to specify\n'
                 'a direction')

    axis_entry = Entry(framer.Funcframe)
    axis_entry.place (x = 190, y = 350)
    axis_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))

    arity_label = Label(framer.Funcframe, text = "Arity:", foreground = "white", background = "#404040", font=(None, 12))
    arity_label.place (x = 100, y = 380)

    arity_entry = Entry(framer.Funcframe)
    arity_entry.place (x = 190, y = 380)
    arity_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))


    drdwnlist = [optionmenuargtype, optionmenuspace]
    for drdwn in drdwnlist:
        i = 0
        while i < drdwn['menu'].index('end') + 1:
            drdwn['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#a3ff8f")
            i += 1













