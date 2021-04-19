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
subeventlist = []


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
        
def createtree(pred, typ, argtyp, argvar):
    global arglist
    global subeventlist
    VoxML = ET.Element("VoxML")
    VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
    VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")
    
    Entity = ET.SubElement(VoxML, "Entity", Type = "Program")

    Lex = ET.SubElement(VoxML, "Lex")
    Pred = ET.SubElement(Lex, "Pred")
    Pred.text = pred
    SubType = ET.SubElement(Lex, "Type")
    SubType.text = typ

    Type = ET.SubElement(VoxML, "Type")
    Head = ET.SubElement(Type, "Head")
    Head.text = typ
    Args = ET.SubElement(Type, "Args")
    for i in arglist:
        new_arg = ET.SubElement(Args, "Arg", Value = i)
    Body = ET.SubElement(Type, "Body")
    for i in subeventlist:
        new_subevent = ET.SubElement(Body, "Subevent", Value = i)
    
    
    prettify(VoxML, pred)



#-----------------------------------------------BUTTON-FUNCTIONS------------------------------------------------

def addsubevent(window):
    global subeventlist
    subeventlist.append("platzhalter")
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, "Subevent has been added!")
    
def addargument(vartyp, varname, window):
    global arglist
    fullarg = varname.get() + ":" + vartyp.get()
    arglist.append(fullarg)
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, "Argument has been added!")
   
    
def getvals(pred, typ, argtyp, argvar):
    predstring = pred.get()
    optVar = typ.get()
    argtypstring = argtyp.get()
    argvarstring = argvar.get()
    
    createtree(predstring, optVar, argtypstring, argvarstring)


def clearlists(argl, subevl, window):
    argl.clear()
    subevl.clear()
    createwindow()

    

#-----------------------------------------------CREATE-MAIN-WINDOW------------------------------------------------
    
def createwindow():
    global arglist
    global subeventlist

    clearall_button = Button(framer.Progrframe, text="clear", command = lambda: clearlists(arglist, subeventlist))
    clearall_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    clearall_button.place ( x = 560, y = 590 )
    tooltip.CreateToolTip(clearall_button, text = 'Tooltip:\n\n'
                 'Klick this button to discard your modifications\n'
                 'and clear all checkboxes, option menus and text fields')

    exec_button = Button(framer.Progrframe, text="save", command = lambda: getvals(pred_entry, optionVar, optionVarArgtype, argvar_entry,
                                                                      ))
    exec_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    exec_button.place ( x = 560, y = 636 )
    tooltip.CreateToolTip(exec_button, text = 'Tooltip:\n\n'
                 'Klick this button to save your modifications\n'
                 'to a VoxML conform XML document')

    debug_textfield = tk.Text(framer.Progrframe, height=4, width=48)
    debug_textfield.configure(relief = RIDGE, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    debug_textfield.place ( x = 100, y = 590 )

    group_label = Label(framer.Progrframe, text = "Group:", foreground = "white", background = "#404040", font=(None, 14))
    group_label.place (x = 360, y = 50)
    tooltip.CreateToolTip(group_label, text = 'Tooltip:\n\n'
                 'Use Integers to refer to groups of parts,\n'
                 'habitats or affordance formulas')

    lex_label = Label(framer.Progrframe, text = "<Lex>", foreground = "white", background = "#404040", font=(None, 14))
    lex_label.place (x = 50, y = 50)

    pred_label = Label(framer.Progrframe, text = "Predicate:", foreground = "white", background = "#404040", font=(None, 12))
    pred_label.place (x = 100, y = 80)

    pred_entry = Entry(framer.Progrframe)
    pred_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    pred_entry.place (x = 190, y = 80)
    
    typesub_label = Label(framer.Progrframe, text = "Type:", foreground = "white", background = "#404040", font=(None, 12))
    typesub_label.place (x = 100, y = 110)

    optionVar = StringVar()
    optionVar.set("process")

    option = OptionMenu(framer.Progrframe, optionVar, "process", "process", "state", "transition_event")
    option.place(x = 190, y = 110)
    option.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    type_label = Label(framer.Progrframe, text = "<Type>", foreground = "white", background = "#404040", font=(None, 14))
    type_label.place (x = 50, y = 140)

    head_label = Label(framer.Progrframe, text = "Head:", foreground = "white", background = "#404040", font=(None, 12))
    head_label.place (x = 100, y = 170)

    optionmenuhead = OptionMenu(framer.Progrframe, optionVar, "process", "process", "state", "transition_event")
    optionmenuhead.place(x = 190, y = 170)
    optionmenuhead.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 11))

    arguments_label = Label(framer.Progrframe, text = "Argument:", foreground = "white", background = "#404040", font=(None, 12))
    arguments_label.place (x = 100, y = 200)

    optionVarArgtype = StringVar()
    optionVarArgtype.set("agent")

    optionmenuargtype = OptionMenu(framer.Progrframe, optionVarArgtype, "agent", "agent", "location", "physobj")
    optionmenuargtype.place(x = 190, y = 200)
    optionmenuargtype.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 11))

    argvar_entry = Entry(framer.Progrframe, width = 4)
    argvar_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    argvar_entry.place (x = 370, y = 200)

    add_argument_button = Button(framer.Progrframe, text="add", command = lambda: addargument(optionVarArgtype, argvar_entry, debug_textfield))
    add_argument_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_argument_button.place ( x = 560, y = 198 )
    tooltip.CreateToolTip(add_argument_button, text = 'Tooltip:\n\n'
                 'Klick this button to add a component\n'
                 'to the componentlist of the current object')



    body_label = Label(framer.Progrframe, text="<Body>", foreground = "white", background = "#404040", font=(None, 14))
    body_label.place (x = 50, y = 230)

    subevent_label = Label(framer.Progrframe, text = "Subevent:", foreground = "white", background = "#404040", font=(None, 12))
    subevent_label.place (x = 100, y = 260)

    subevent_entry = Entry(framer.Progrframe)
    subevent_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    subevent_entry.place (x = 190, y = 260)

    add_subevent_button = Button(framer.Progrframe, text="add", command = lambda: addsubevent(debug_textfield))
    add_subevent_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_subevent_button.place ( x = 560, y = 258 )
    
    drdwnlist = [option, optionmenuhead, optionmenuargtype]
    for drdwn in drdwnlist:
        i = 0
        while i < drdwn['menu'].index('end') + 1:
            drdwn['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#a3ff8f")
            i += 1















