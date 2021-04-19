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
constraintlist = []
corresplist = []


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
        
def createtree(pred, classent, valent, argtyp, argvar, constr, corresp):
    global arglist
    global constraintlist
    global corresplist
    VoxML = ET.Element("VoxML")
    VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
    VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")
    
    Entity = ET.SubElement(VoxML, "Entity", Type = "Relation")

    Lex = ET.SubElement(VoxML, "Lex")
    Pred = ET.SubElement(Lex, "Pred")
    Pred.text = pred

    Type = ET.SubElement(VoxML, "Type")
    Class = ET.SubElement(Type, "Class")
    Class.text = classent
    Value = ET.SubElement(Type, "Value")
    Value.text = valent
    Args = ET.SubElement(Type, "Args")
    for i in arglist:
        new_arg = ET.SubElement(Args, "Arg", Value = i)
    for i in constraintlist:
        new_constraint = ET.SubElement(Type, "Constr")
        new_constraint.text = i
    Corresps = ET.SubElement(Type, "Corresps")
    for i in corresplist:
        new_corresp = ET.SubElement(Corresps, "Corresp", Value = i)
    
    
    prettify(VoxML, pred)


#-----------------------------------------------BUTTON-FUNCTIONS------------------------------------------------
    
def addargument(vartyp, varname, window):
    global arglist
    fullarg = varname.get() + ":" + vartyp.get()
    arglist.append(fullarg)
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, "Argument has been added!")


def addconstr(constrstr, window):
    global constraintlist
    fullconstr = constrstr.get()
    constraintlist.append(fullconstr)
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, "Constraint has been added!")


def addcorresp(correspstr, window):
    global corresplist
    fullcorresp = correspstr.get()
    corresplist.append(fullcorresp)
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, "Corresp. has been added!")
    
    
def getvals(pred, classent, valent, argtyp, argvar, constr, corresp):
    predstring = pred.get()
    classentstring = classent.get()
    valentstring = valent.get()
    argtypstring = argtyp.get()
    argvarstring = argvar.get()
    conststring = constr.get()
    correspstring = corresp.get()
    
    createtree(predstring, classentstring, valentstring, argtypstring, argvarstring,
               conststring, correspstring)


def clearlists(argl, constrl, correspl):
    argl.clear()
    constrl.clear()
    correspl.clear()
    createwindow()

    

#-----------------------------------------------CREATE-MAIN-WINDOW------------------------------------------------
    
def createwindow():
    global arglist
    global constraintlist
    global corresplist

    clearall_button = Button(framer.Relatframe, text="clear", command = lambda: clearlists(arglist, constraintlist, corresplist))
    clearall_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    clearall_button.place ( x = 560, y = 590 )
    tooltip.CreateToolTip(clearall_button, text = 'Tooltip:\n\n'
                 'Klick this button to discard your modifications\n'
                 'and clear all checkboxes, option menus and text fields')

    exec_button = Button(framer.Relatframe, text="save", command = lambda: getvals(pred_entry, optionVarClass, optionVarValue,
                                                                      optionVarArgtype, argvar_entry, constr_entry,
                                                                      corresps_entry))
    exec_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    exec_button.place ( x = 560, y = 636 )
    tooltip.CreateToolTip(exec_button, text = 'Tooltip:\n\n'
                 'Klick this button to save your modifications\n'
                 'to a VoxML conform XML document')

    debug_textfield = tk.Text(framer.Relatframe, height=4, width=48)
    debug_textfield.configure(relief = RIDGE, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    debug_textfield.place ( x = 100, y = 590 )

    lex_label = Label(framer.Relatframe, text = "<Lex>", foreground = "white", background = "#404040", font=(None, 14))
    lex_label.place (x = 50, y = 50)

    pred_label = Label(framer.Relatframe, text = "Predicate:", foreground = "white", background = "#404040", font=(None, 12))
    pred_label.place (x = 100, y = 80)

    pred_entry = Entry(framer.Relatframe)
    pred_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    pred_entry.place (x = 190, y = 80)

    type_label = Label(framer.Relatframe, text = "<Type>", foreground = "white", background = "#404040", font=(None, 14))
    type_label.place (x = 50, y = 140)

    class_label = Label(framer.Relatframe, text = "Class:", foreground = "white", background = "#404040", font=(None, 12))
    class_label.place (x = 100, y = 170)

    optionVarClass = StringVar()
    optionVarClass.set("config")

    optionmenuclass = OptionMenu(framer.Relatframe, optionVarClass, "config", "config", "force_dynamic")
    optionmenuclass.place(x = 190, y = 170)
    optionmenuclass.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    arguments_label = Label(framer.Relatframe, text = "Value:", foreground = "white", background = "#404040", font=(None, 12))
    arguments_label.place (x = 100, y = 200)

    optionVarValue = StringVar()
    optionVarValue.set("RCC8.EC")

    optionmenuvalue = OptionMenu(framer.Relatframe, optionVarValue, "RCC8.EC", "RCC8.EC")
    optionmenuvalue.place(x = 190, y = 200)
    optionmenuvalue.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    arguments_label = Label(framer.Relatframe, text = "Argument:", foreground = "white", background = "#404040", font=(None, 12))
    arguments_label.place (x = 100, y = 230)

    optionVarArgtype = StringVar()
    optionVarArgtype.set("agent")

    optionmenuargtype = OptionMenu(framer.Relatframe, optionVarArgtype, "agent", "agent", "location", "physobj")
    optionmenuargtype.place(x = 190, y = 230)
    optionmenuargtype.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    argvar_entry = Entry(framer.Relatframe, width = 4)
    argvar_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    argvar_entry.place (x = 370, y = 230)

    add_argument_button = Button(framer.Relatframe, text="add", command = lambda: addargument(optionVarArgtype, argvar_entry, debug_textfield))
    add_argument_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_argument_button.place ( x = 560, y = 228 )
    tooltip.CreateToolTip(add_argument_button, text = 'Tooltip:\n\n'
                 'Klick this button to add a component\n'
                 'to the componentlist of the current object')



    constr_label = Label(framer.Relatframe, text="Constraint:", foreground = "white", background = "#404040", font=(None, 12))
    constr_label.place (x = 100, y = 260)

    constr_entry = Entry(framer.Relatframe)
    constr_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    constr_entry.place (x = 190, y = 260)

    add_constr_button = Button(framer.Relatframe, text="add", command = lambda: addconstr(constr_entry, debug_textfield))
    add_constr_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_constr_button.place ( x = 560, y = 258 )

    corresps_label = Label(framer.Relatframe, text = "Corresps.:", foreground = "white", background = "#404040", font=(None, 12))
    corresps_label.place (x = 100, y = 290)

    corresps_entry = Entry(framer.Relatframe)
    corresps_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    corresps_entry.place (x = 190, y = 290)

    add_corresps_button = Button(framer.Relatframe, text="add", command = lambda: addcorresp(corresps_entry, debug_textfield))
    add_corresps_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_corresps_button.place ( x = 560, y = 288 )
    
    drdwnlist = [optionmenuclass, optionmenuvalue, optionmenuargtype]
    for drdwn in drdwnlist:
        i = 0
        while i < drdwn['menu'].index('end') + 1:
            drdwn['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#a3ff8f")
            i += 1

















