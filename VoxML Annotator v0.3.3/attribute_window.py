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
        
def createtree(pred, argtyp, argvar, scale, arity):
    global arglist
    global subeventlist
    VoxML = ET.Element("VoxML")
    VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
    VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")
    
    Entity = ET.SubElement(VoxML, "Entity", Type = "Attribute")

    Lex = ET.SubElement(VoxML, "Lex")
    Pred = ET.SubElement(Lex, "Pred")
    Pred.text = pred

    Type = ET.SubElement(VoxML, "Type")
    Args = ET.SubElement(Type, "Args")
    for i in arglist:
        new_arg = ET.SubElement(Args, "Arg", Value = i)
    Scale = ET.SubElement(Type, "Scale")
    Scale.text = scale
    Arity = ET.SubElement(Type, "Arity")
    Arity.text = arity
    
    prettify(VoxML, pred)



#-----------------------------------------------BUTTON-FUNCTIONS------------------------------------------------
    
def addargument(vartyp, varname, window):
    global arglist
    fullarg = varname.get() + ":" + vartyp.get()
    arglist.append(fullarg)
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, "Argument has been added!")
   
    
def getvals(pred, argtyp, argvar, scale, arity):
    predstring = pred.get()
    argtypstring = argtyp.get()
    argvarstring = argvar.get()
    scalestring = scale.get()
    aritystring = arity.get()
    
    createtree(predstring, argtypstring, argvarstring, scalestring, aritystring)


def clearlists(argl):
    argl.clear()
    createwindow()

    




#-----------------------------------------------CREATE-MAIN-WINDOW------------------------------------------------
    
def createwindow():
    global arglist

    clearall_button = Button(framer.Attrframe, text="clear", command = lambda: clearlists(arglist))
    clearall_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    clearall_button.place ( x = 560, y = 590 )
    tooltip.CreateToolTip(clearall_button, text = 'Tooltip:\n\n'
                 'Klick this button to discard your modifications\n'
                 'and clear all checkboxes, option menus and text fields')

    exec_button = Button(framer.Attrframe, text="save", command = lambda: getvals(pred_entry, optionVarArgtype, argvar_entry,
                                                                      optionVarScale, optionVarArity))
    exec_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    exec_button.place ( x = 560, y = 636 )
    tooltip.CreateToolTip(exec_button, text = 'Tooltip:\n\n'
                 'Klick this button to save your modifications\n'
                 'to a VoxML conform XML document')

    debug_textfield = tk.Text(framer.Attrframe, height=4, width=48)
    debug_textfield.configure(relief = RIDGE, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    debug_textfield.place ( x = 100, y = 590 )

    lex_label = Label(framer.Attrframe, text = "<Lex>", foreground = "white", background = "#404040", font=(None, 14))
    lex_label.place (x = 50, y = 50)

    pred_label = Label(framer.Attrframe, text = "Predicate:", foreground = "white", background = "#404040", font=(None, 12))
    pred_label.place (x = 100, y = 80)

    pred_entry = Entry(framer.Attrframe)
    pred_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    pred_entry.place (x = 190, y = 80)

    type_label = Label(framer.Attrframe, text = "<Type>", foreground = "white", background = "#404040", font=(None, 14))
    type_label.place (x = 50, y = 140)

    arguments_label = Label(framer.Attrframe, text = "Argument:", foreground = "white", background = "#404040", font=(None, 12))
    arguments_label.place (x = 100, y = 200)

    optionVarArgtype = StringVar()
    optionVarArgtype.set("agent")

    optionmenuargtype = OptionMenu(framer.Attrframe, optionVarArgtype, "agent", "agent", "location", "physobj")
    optionmenuargtype.place(x = 190, y = 200)
    optionmenuargtype.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    argvar_entry = Entry(framer.Attrframe, width = 4)
    argvar_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    argvar_entry.place (x = 370, y = 200)

    add_argument_button = Button(framer.Attrframe, text="add", command = lambda: addargument(optionVarArgtype, argvar_entry, debug_textfield))
    add_argument_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_argument_button.place ( x = 480, y = 198 )
    tooltip.CreateToolTip(add_argument_button, text = 'Tooltip:\n\n'
                 'Klick this button to add a component\n'
                 'to the componentlist of the current object')



    scale_label = Label(framer.Attrframe, text="Scale:", foreground = "white", background = "#404040", font=(None, 12))
    scale_label.place (x = 100, y = 230)

    optionVarScale = StringVar()
    optionVarScale.set("binary")

    optionmenuscale = OptionMenu(framer.Attrframe, optionVarScale, "binary", "binary", "nominal", "ordinal", "intervall", "rational")
    optionmenuscale.place(x = 190, y = 230)
    optionmenuscale.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    arity_label = Label(framer.Attrframe, text = "Arity:", foreground = "white", background = "#404040", font=(None, 12))
    arity_label.place (x = 100, y = 260)

    optionVarArity = StringVar()
    optionVarArity.set("intransitive")

    optionmenuarity = OptionMenu(framer.Attrframe, optionVarArity, "intransitive", "intransitive", "transitive")
    optionmenuarity.place(x = 190, y = 260)
    optionmenuarity.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    drdwnlist = [optionmenuargtype, optionmenuscale, optionmenuarity]
    for drdwn in drdwnlist:
        i = 0
        while i < drdwn['menu'].index('end') + 1:
            drdwn['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#a3ff8f")
            i += 1

















