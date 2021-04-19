from tkinter import StringVar
from tkinter import IntVar
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import xml.etree.ElementTree as ET
import xml.dom.minidom as  minidom
from io import BytesIO
from tkinter import *
import enttypeselector
import tooltip
import help_window
import framer



#-----------------------------------------------MANDATORY-LISTS--------------------------------------------------

componentlist = []
intrinsiclist = []
intrinsicvaluelist = []
extrinsiclist = []
extrinsicvaluelist = []
affordanceformulalist = []



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
    
def addtotree(list1, vallist, tagname, tag):
    counter = 0
    for j in list1:
        if j[:2] == "UP":
            new_intr = ET.SubElement(tag, tagname, Name = j, Value = "align(" + vallist[counter] + ")")
            counter = counter + 1
        elif j[:3] == "TOP":
            new_intr = ET.SubElement(tag, tagname, Name = j, Value = "top(" + vallist[counter] + ")")
            counter = counter + 1
        elif j[:4] == "NEAR":
            new_intr = ET.SubElement(tag, tagname, Name = j, Value = "align(" + vallist[counter] + ")")
            counter = counter + 1
        elif j[:5] == "FRONT":
            new_intr = ET.SubElement(tag, tagname, Name = j, Value = "front(" + vallist[counter] + ")")
            counter = counter + 1


def addrotsymtotree(rotx, roty, rotz, tag):
    if rotx == 0:
        if roty == 0:
            if rotz == 0:
                rotatsymstr = ""
            elif rotz == 1:
                rotatsymstr = "Z"
        elif roty == 1:
            if rotz == 0:
                rotatsymstr = "Y"
            elif rotz == 1:
                rotatsymstr = "Y,Z"
    elif rotx == 1:
        if roty == 0:
            if rotz == 0:
                rotatsymstr = "X"
            elif rotz == 1:
                rotatsymstr = "X,Z"
        elif roty == 1:
            if rotz == 0:
                rotatsymstr = "X,Y"
            elif rotz == 1:
                rotatsymstr = "X,Y,Z"
    tag.text = rotatsymstr


def addreflsymtotree(reflxy, reflxz, reflyz, tag):
    if reflxy == 0:
        if reflxz == 0:
            if reflyz == 0:
                reflsymstr = ""
            elif reflyz == 1:
                reflsymstr = "YZ"
        elif reflxz == 1:
            if reflyz == 0:
                reflsymstr = "XZ"
            elif reflyz == 1:
                reflsymstr = "XZ,YZ"
    elif reflxy == 1:
        if reflxz == 0:
            if reflyz == 0:
                reflsymstr = "XY"
            elif reflyz == 1:
                reflsymstr = "XY,YZ"
        elif reflxz == 1:
            if reflyz == 0:
                reflsymstr = "XY,XZ"
            elif reflyz == 1:
                reflsymstr = "XY,XZ,YZ"
    tag.text = reflsymstr


def addheadtotree(headv, headg, tag):
    if headg != "":
        tag.text = headv + "[" + headg + "]"
    elif headg == "":
        tag.text = headv


def addafftotree(list1, tagname, tag):
    for j in list1:
        new_aff = ET.SubElement(tag, tagname, Formula = j)


#-----------------------------------------------CREATE-XML-TREE-------------------------------------------------
        
def createtree(pred, typ, headv, headg, concstr, concgrp, rotx, roty, rotz, reflxy, reflxz, reflyz, scalestr, movablestr):
    global componentlist
    global intrinsiclist
    global intrinsicvaluelist
    global extrinsiclist
    global affordanceformulalist
    
    VoxML = ET.Element("VoxML")
    VoxML.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
    VoxML.set('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")
    
    Entity = ET.SubElement(VoxML, "Entity", Type = "Object")

    Lex = ET.SubElement(VoxML, "Lex")
    Pred = ET.SubElement(Lex, "Pred")
    Pred.text = pred
    SubType = ET.SubElement(Lex, "Type")
    SubType.text = typ

    Type = ET.SubElement(VoxML, "Type")
    Head = ET.SubElement(Type, "Head")
    addheadtotree(headv, headg, Head)
    Components = ET.SubElement(Type, "Components")
    for i in componentlist:
        new_comp = ET.SubElement(Components, "Component", Value = i)
    Concavity = ET.SubElement(Type, "Concavity")
    if concgrp != "":
        Concavity.text = concstr + "[" + concgrp + "]"
    elif concgrp == "":
        Concavity.text = concstr
    else:
        pass
    RotatSym = ET.SubElement(Type, "RotatSym")
    addrotsymtotree(rotx, roty, rotz, RotatSym)
    
    ReflSym = ET.SubElement(Type, "ReflSym")
    addreflsymtotree(reflxy, reflxz, reflyz, ReflSym)

    Habitat = ET.SubElement(VoxML, "Habitat")
    Intrinsic = ET.SubElement(Habitat, "Intrinsic")
    addtotree(intrinsiclist, intrinsicvaluelist, "Intr", Intrinsic)
    Extrinsic = ET.SubElement(Habitat, "Extrinsic")
    addtotree(extrinsiclist, extrinsicvaluelist, "Extr", Extrinsic)

    Afford_Str = ET.SubElement(VoxML, "Afford_Str")
    Affordances = ET.SubElement(Afford_Str, "Affordances")
    addafftotree(affordanceformulalist, "Affordance", Affordances)
    
    Embodiement = ET.SubElement(VoxML, "Embodiement")
    Scale = ET.SubElement(Embodiement, "Scale")
    Scale.text = scalestr
    Movable = ET.SubElement(Embodiement, "Movable")
    Movable.text = movablestr
    
    prettify(VoxML, pred)



#-----------------------------------------------BUTTON-FUNCTIONS------------------------------------------------

def addcomponent(compentry, compgrp, dupevar, debugwindow, componentwindow, complistvar, componentmenu):
    global componentlist
    
    if dupevar.get() == 0:
        newcomponentpre = compentry.get()
    elif dupevar.get() == 1:
        newcomponentpre = compentry.get() + "+"
    else:
        pass

    if compgrp.get() != "":
        newcomponent = newcomponentpre + "[" + compgrp.get() + "]"
    elif compgrp.get() == "":
        newcomponent = newcomponentpre
    else:
        pass

    componentlist.append(newcomponent)
    debugwindow.delete('1.0', tk.END)
    debugwindow.insert(tk.INSERT, "Component has been added!")
    componentmenu['menu'].delete(0, 'end')
    newchoices = componentlist
    i = 0
    for choice in newchoices:
        componentmenu['menu'].add_command(label = choice, command=tk._setit(complistvar, choice))
        componentmenu['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#fa7878")
        i = i + 1
    componentmenu['menu'].add_command(label = "                                                                      ", command=tk._setit(complistvar, "Select Component"))
    componentmenu['menu'].entryconfig(len(componentlist) + 1, background = "#404040" ,activebackground = "#404040", foreground = "white", activeforeground = "white")
    configlistwindow(componentwindow)
    
    
def addhabitat(var, grp, arg1, arg2, list1, vallist, intorext, window, listvar, menu, componentwindow):
    if grp.get() == "":
        window.delete('1.0', tk.END)
        window.insert(tk.INSERT, "Please add an Argument")
    elif grp.get() != "":
        if arg2.get() == "":
            newargstr = arg1.get()
            vallist.append(newargstr)
        elif arg2.get() != "":
            newargstr = arg1.get() + "," + arg2.get()
            vallist.append(newargstr)
            
        newhab = var.get() + "[" + grp.get() + "]"
        list1.append(newhab)
        window.delete('1.0', tk.END)
        if intorext == "intr":
            window.insert(tk.INSERT, "Intrinsic habitat has been added!")
        elif intorext == "extr":
            window.insert(tk.INSERT, "Extrinsic habitat has been added!")
    else:
        pass
    newchoices = list1
    menu['menu'].delete(0, 'end')
    i = 0
    for choice in newchoices:
        menu['menu'].add_command(label = choice, command=tk._setit(listvar, choice))
        menu['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#fa7878")
        i = i + 1
    menu['menu'].add_command(label = "                                                                       ", command=tk._setit(listvar, "Select Entry"))
    menu['menu'].entryconfig(1, background = "#404040" ,activebackground = "#404040", foreground = "white", activeforeground = "#fa7878")
    configlistwindow(componentwindow)

def addformula(formula, formulagroup, arg1, arg2, window, listvar, menu, componentwindow):
    global affordanceformulalist
    prefix = ""
    form = ""
    argu1 = arg1.get()
    argu2 = arg2.get()
    if argu1.isnumeric():
        argu1 = "[" + arg1.get() + "]"
    elif argu2.isnumeric():
        argu2 = "[" + arg2.get() + "]"

    if formulagroup.get() == "":
        prefix = "H->["
    elif formulagroup.get() != "":
        prefix = "H[" + formulagroup.get() + "]->["
    else:
        pass

    if arg1.get() != "" and arg2.get() != "":
        if formula.get() == "put_on":
            form = "put(" + argu1 + ", on(" + argu2 + "))]support(" + argu2 + ", " + argu1 + ")"
        elif formula.get() == "put_in":
            form = "put(" + argu1 + ", in(" + argu2 + "))]contain(" + argu2 + ", " + argu1 + ")"
        elif formula.get() == "lift":
            form = formula.get() + "(" + argu1 + ", " + argu2 + ")]hold(" + argu1 + ", " + argu2 + ")"
        else:
            form = formula.get() + "(" + argu1 + ", " + argu2 + ")]"
        newformula = prefix + form
        affordanceformulalist.append(newformula)
        window.delete('1.0', tk.END)
        window.insert(tk.INSERT, "Affordance Formula has been added!")
    else:
        window.delete('1.0', tk.END)
        window.insert(tk.INSERT, "Please add more Arguments")
    newchoices = affordanceformulalist
    menu['menu'].delete(0, 'end')
    i = 0
    for choice in newchoices:
        menu['menu'].add_command(label = choice, command=tk._setit(listvar, choice))
        menu['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#fa7878")
        i = i + 1
    menu['menu'].add_command(label = "                                                                       ", command=tk._setit(listvar, "Select Entry"))
    menu['menu'].entryconfig(1, background = "#404040" ,activebackground = "#404040", foreground = "white", activeforeground = "#fa7878")
    configlistwindow(componentwindow)
    
    
def getvals(pred, typ, headv, headg, concstr, concgrp, rotx, roty, rotz, reflxy, reflxz, reflyz, scale, movable):
    predstring = pred.get()
    optVar = typ.get()
    headVar = headv.get()
    headGroup = headg.get()
    concavitystring = concstr.get()
    concavitygrp = concgrp.get()
    rotstrx = rotx.get()
    rotstry = roty.get()
    rotstrz = rotz.get()
    reflxystr = reflxy.get()
    reflxzstr = reflxz.get()
    reflyzstr = reflyz.get()
    scalestr = scale.get()
    movablestr = movable.get()
    
    createtree(predstring, optVar, headVar, headGroup, concavitystring, concavitygrp, rotstrx,
             rotstry, rotstrz, reflxystr, reflxzstr, reflyzstr, scalestr, movablestr)


def clearlists(complist, intrlist, intrvallist, extrlist, extrvallist, affordformlist):
    complist.clear()
    intrlist.clear()
    intrvallist.clear()
    extrlist.clear()
    extrvallist.clear()
    affordformlist.clear()
    createwindow()

def removefromlist(lists, componentwindow, opmenu, opmenuvar, window):
    value = opmenuvar.get()
    if value in lists:
        lists.remove(value)
    else:
        print("no such item in list")
    opmenu['menu'].delete(0, 'end')
    newchoices = lists
    i = 0
    for choice in newchoices:
        opmenu['menu'].add_command(label = choice, command=tk._setit(opmenuvar, choice))
        opmenu['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#fa7878")
        i = i+1
    opmenu['menu'].add_command(label = "                                                                      ", command=tk._setit(opmenuvar, "click to select"))
    opmenu['menu'].entryconfig(len(lists) + 1, background = "#404040" ,activebackground = "#404040", foreground = "white", activeforeground = "white")
    window.delete('1.0', tk.END)
    window.insert(tk.INSERT, value + "  Has been removed!")
    configlistwindow(componentwindow)
    

def configlistwindow(window):
    global componentlist
    global intrinsiclist
    global extrinsiclist
    global affordanceformulalist
    count = 0
    lists = [componentlist, intrinsiclist, extrinsiclist, affordanceformulalist]
    window.delete('1.0', tk.END)
    for j in lists:
        if count == 0:
            window.insert(tk.INSERT, "Components:" + "\n")
        elif count == 1:
            window.insert(tk.INSERT, "Intrinsic Habitats:" + "\n")
        elif count == 2:
            window.insert(tk.INSERT, "Extrinsic Habitats:" + "\n")
        elif count == 3:
            window.insert(tk.INSERT, "Affordance Formulas:" + "\n")
        count = count + 1
        for i in j:
            window.insert(tk.INSERT, i + "\n")

#-----------------------------------------------CREATE-MAIN-WINDOW------------------------------------------------
    
def createwindow():
    global componentlist
    global intrinsiclist
    global intrinsicvaluelist
    global extrinsiclist
    global extrinsicvaluelist
    global affordanceformulalist

    clearall_button = Button(framer.Objframe, text="clear", command = lambda: clearlists(componentlist, intrinsiclist, intrinsicvaluelist,
                                                                              extrinsiclist, extrinsicvaluelist, affordanceformulalist))
    clearall_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    clearall_button.place ( x = 560, y = 590 )
    tooltip.CreateToolTip(clearall_button, text = 'Tooltip:\n\n'
                 'Klick this button to discard your modifications\n'
                 'and clear all checkboxes, option menus and text fields')

    exec_button = Button(framer.Objframe, text="save", command = lambda: getvals(pred_entry, optionVar, optionVarHead, headgroup_entry,
                                                                      optionVarConc, concavitygroup_entry, rotvalx, rotvaly,
                                                                      rotvalz, reflvalxy, reflvalxz, reflvalyz, optionVarScale,
                                                                      optionVarMovable))
    exec_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    exec_button.place ( x = 560, y = 636 )
    tooltip.CreateToolTip(exec_button, text = 'Tooltip:\n\n'
                 'Klick this button to save your modifications\n'
                 'to a VoxML conform XML document')

    debug_textfield = tk.Text(framer.Objframe, height=4, width=48)
    debug_textfield.configure(relief = RIDGE, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    debug_textfield.place ( x = 100, y = 590 )

    group_label = Label(framer.Objframe, text = "Group:", foreground = "white", background = "#404040", font=(None, 14))
    group_label.place (x = 360, y = 50)
    tooltip.CreateToolTip(group_label, text = 'Tooltip:\n\n'
                 'Use Integers to refer to groups of parts,\n'
                 'habitats or affordance formulas')

    args_label = Label(framer.Objframe, text = "Arguments:", foreground = "white", background = "#404040", font=(None, 14))
    args_label.place (x = 440, y = 50)
    tooltip.CreateToolTip(args_label, text = 'Tooltip:\n\n'
                 'Insert functions arguments in entry fields\n'
                 'below')

    lex_label = Label(framer.Objframe, text = "<Lex>", foreground = "white", background = "#404040", font=(None, 14))
    lex_label.place (x = 50, y = 50)

    pred_label = Label(framer.Objframe, text = "Predicate:", foreground = "white", background = "#404040", font=(None, 12))
    pred_label.place (x = 100, y = 80)

    pred_entry = Entry(framer.Objframe)
    pred_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    pred_entry.place (x = 190, y = 80)
    
    typesub_label = Label(framer.Objframe, text = "Type:", foreground = "white", background = "#404040", font=(None, 12))
    typesub_label.place (x = 100, y = 110)

    optionVar = StringVar()
    optionVar.set("physobj")

    option = OptionMenu(framer.Objframe, optionVar, "physobj", "physobj", "physobj*artifact")
    option.place(x = 190, y = 110)
    option.config( width = 145, height = 14, image = framer.menutickpic, anchor = "w", bd = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    type_label = Label(framer.Objframe, text = "<Type>", foreground = "white", background = "#404040", font=(None, 14))
    type_label.place (x = 50, y = 140)

    head_label = Label(framer.Objframe, text = "Head:", foreground = "white", background = "#404040", font=(None, 12))
    head_label.place (x = 100, y = 170)

    headgroup_entry = Entry(framer.Objframe, width = 4)
    headgroup_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    headgroup_entry.place (x = 370, y = 170)
    tooltip.CreateToolTip(headgroup_entry, text = 'Tooltip:\n\n'
                 '*OPTIONAL*')

    optionVarHead = StringVar()
    optionVarHead.set("ellipsoid")

    optionmenuhead = OptionMenu(framer.Objframe, optionVarHead, "ellipsoid", "ellipsoid", "bipyramid", "cylindroid", "cupola", "frustum",
                                "hemiellipsoid", "parallelepiped", "prismatoid", "pyramid", "rectangular_prism", "sheet",
                                "toroid", "wedge")
    optionmenuhead.place(x = 190, y = 170)
    optionmenuhead.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 11))

    component_label = Label(framer.Objframe, text = "Component:", foreground = "white", background = "#404040", font=(None, 12))
    component_label.place (x = 100, y = 200)

    component_entry = Entry(framer.Objframe)
    component_entry.configure(relief = RIDGE, width = 17, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    component_entry.place (x = 190, y = 200)

    componentgroup_entry = Entry(framer.Objframe, width = 4)
    componentgroup_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    componentgroup_entry.place (x = 370, y = 200)
    tooltip.CreateToolTip(componentgroup_entry, text = 'Tooltip:\n\n'
                 '*OPTIONAL*')

    duplicatevar = IntVar()
    duplicatevar.set(0)
    
    dupecheckbutton = Checkbutton(framer.Objframe, text="", variable=duplicatevar)
    dupecheckbutton.var = duplicatevar
    dupecheckbutton.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "#404040", font=(None, 12))
    dupecheckbutton.place ( x = 470, y = 200 )
    tooltip.CreateToolTip(dupecheckbutton, text = 'Tooltip:\n\n'
                 'Check this box if the Object has multiple instances\n'
                 'or copies of that same part\n\n *OPTIONAL*')

    add_component_button = Button(framer.Objframe, text="add", command = lambda: addcomponent(component_entry, componentgroup_entry, duplicatevar,
                                                                                   debug_textfield, componentlist_textfield,optionVarComponentlist, OptionMenuComponentlist))
    add_component_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_component_button.place ( x = 560, y = 198 )
    tooltip.CreateToolTip(add_component_button, text = 'Tooltip:\n\n'
                 'Klick this button to add a component\n'
                 'to the componentlist of the current object')

    concavity_label = Label(framer.Objframe, text = "Concavity:", foreground = "white", background = "#404040", font=(None, 12))
    concavity_label.place (x = 100, y = 230)

    optionVarConc = StringVar()
    optionVarConc.set("Flat")

    optionmenuconc = OptionMenu(framer.Objframe, optionVarConc, "Flat", "Flat", "Concave", "Convex")
    optionmenuconc.place(x = 190, y = 230)
    optionmenuconc.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    concavitygroup_entry = Entry(framer.Objframe, width = 4)
    concavitygroup_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    concavitygroup_entry.place (x = 370, y = 230)
    tooltip.CreateToolTip(concavitygroup_entry, text = 'Tooltip:\n\n'
                 '*OPTIONAL*')

    rotatsym_label = Label(framer.Objframe, text = "Rotatsym:", foreground = "white", background = "#404040", font=(None, 12))
    rotatsym_label.place (x = 100, y = 260)

    rotvalx = IntVar()
    rotvalx.set(0)
    rotvaly = IntVar()
    rotvaly.set(0)
    rotvalz = IntVar()
    rotvalz.set(0)

    rotxcheckbutton = Checkbutton(framer.Objframe, text="X", variable=rotvalx)
    rotxcheckbutton.var = rotvalx
    rotxcheckbutton.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "#404040", activeforeground = "#404040", font=(None, 12))
    rotxcheckbutton.place ( x = 190, y = 260 )

    rotxcheckbuttonlabel = Label(framer.Objframe, text="X")
    rotxcheckbuttonlabel.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "white", font=(None, 12))
    rotxcheckbuttonlabel.place ( x = 210, y = 262 )

    rotycheckbutton = Checkbutton(framer.Objframe, text="Y", variable=rotvaly)
    rotycheckbutton.var = rotvaly
    rotycheckbutton.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "#404040", activeforeground = "#404040", font=(None, 12))
    rotycheckbutton.place ( x = 230, y = 260 )

    rotycheckbuttonlabel = Label(framer.Objframe, text="Y")
    rotycheckbuttonlabel.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "white", font=(None, 12))
    rotycheckbuttonlabel.place ( x = 250, y = 262 )

    rotzcheckbutton = Checkbutton(framer.Objframe, text="Z", variable=rotvalz)
    rotzcheckbutton.var = rotvalz
    rotzcheckbutton.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "#404040", activeforeground = "#404040", font=(None, 12))
    rotzcheckbutton.place ( x = 270, y = 260 )

    rotzcheckbuttonlabel = Label(framer.Objframe, text="Z")
    rotzcheckbuttonlabel.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "white", font=(None, 12))
    rotzcheckbuttonlabel.place ( x = 290, y = 262 )

    reflsym_label = Label(framer.Objframe, text = "Reflsym:", foreground = "white", background = "#404040", font=(None, 12))
    reflsym_label.place (x = 100, y = 290)

    reflvalxy = IntVar()
    reflvalxy.set(0)
    reflvalxz = IntVar()
    reflvalxz.set(0)
    reflvalyz = IntVar()
    reflvalyz.set(0)

    reflxycheckbutton = Checkbutton(framer.Objframe, text="XY", variable=reflvalxy)
    reflxycheckbutton.var = reflvalxy
    reflxycheckbutton.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "#404040", activeforeground = "#404040", font=(None, 12))
    reflxycheckbutton.place ( x = 190, y = 290 )

    reflxycheckbuttonlabel = Label(framer.Objframe, text="XY")
    reflxycheckbuttonlabel.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "white", font=(None, 12))
    reflxycheckbuttonlabel.place ( x = 210, y = 292 )

    reflxzcheckbutton = Checkbutton(framer.Objframe, text="XZ", variable=reflvalxz)
    reflxzcheckbutton.var = reflvalxz
    reflxzcheckbutton.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "#404040", activeforeground = "#404040", font=(None, 12))
    reflxzcheckbutton.place ( x = 240, y = 290 )

    reflxzcheckbuttonlabel = Label(framer.Objframe, text="XZ")
    reflxzcheckbuttonlabel.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "white", font=(None, 12))
    reflxzcheckbuttonlabel.place ( x = 260, y = 292 )

    reflyzcheckbutton = Checkbutton(framer.Objframe, text="YZ", variable=reflvalyz)
    reflyzcheckbutton.var = reflvalyz
    reflyzcheckbutton.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "#404040", activeforeground = "#404040", font=(None, 12))
    reflyzcheckbutton.place ( x = 290, y = 290 )

    reflyzcheckbuttonlabel = Label(framer.Objframe, text="YZ")
    reflyzcheckbuttonlabel.config(borderwidth = 0, background = "#404040", activebackground= "#404040", foreground = "white", font=(None, 12))
    reflyzcheckbuttonlabel.place ( x = 310, y = 292 )

    habitat_label = Label(framer.Objframe, text = "<Habitat>", foreground = "white", background = "#404040", font=(None, 14))
    habitat_label.place (x = 50, y = 320)

    intrinsic_label = Label(framer.Objframe, text = "Intrinsic:", foreground = "white", background = "#404040", font=(None, 12))
    intrinsic_label.place (x = 100, y = 350)

    optionVarIntr = StringVar()
    optionVarIntr.set("UP")

    optionmenuint = OptionMenu(framer.Objframe, optionVarIntr, "UP", "UP", "TOP", "NEAR", "FRONT")
    optionmenuint.place(x = 190, y = 350)
    optionmenuint.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    intrinsicgroup_entry = Entry(framer.Objframe, width = 4)
    intrinsicgroup_entry.place (x = 370, y = 350)
    intrinsicgroup_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    tooltip.CreateToolTip(intrinsicgroup_entry, text = 'Tooltip:\n\n'
                 '*OPTIONAL*')

    intrinsicarg1_entry = Entry(framer.Objframe, width = 4)
    intrinsicarg1_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    intrinsicarg1_entry.place (x = 440, y = 350)

    intrinsicarg2_entry = Entry(framer.Objframe, width = 4)
    intrinsicarg2_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    intrinsicarg2_entry.place (x = 485, y = 350)
    
    add_intrinsic_button = Button(framer.Objframe, text="add", command = lambda: addhabitat(optionVarIntr, intrinsicgroup_entry, intrinsicarg1_entry,
                                                                                 intrinsicarg2_entry, intrinsiclist, intrinsicvaluelist,
                                                                                 "intr", debug_textfield, optionVarIntrinsiclist, OptionMenuIntrinsiclist, componentlist_textfield))
    add_intrinsic_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_intrinsic_button.place ( x = 560, y = 348 )

    tooltip.CreateToolTip(add_intrinsic_button, text = 'Tooltip:\n\n'
                 'Klick this button to add an intrinsic habitat\n'
                 'to the list of intrinsic habitats of the current object')

    extrinsic_label = Label(framer.Objframe, text = "Extrinsic:", foreground = "white", background = "#404040", font=(None, 12))
    extrinsic_label.place (x = 100, y = 380)

    optionVarExtr = StringVar()
    optionVarExtr.set("UP")

    optionmenuext = OptionMenu(framer.Objframe, optionVarExtr, "UP", "UP", "TOP", "NEAR", "FRONT")
    optionmenuext.place(x = 190, y = 380)
    optionmenuext.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    extrinsicgroup_entry = Entry(framer.Objframe, width = 4)
    extrinsicgroup_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    extrinsicgroup_entry.place (x = 370, y = 380)
    tooltip.CreateToolTip(extrinsicgroup_entry, text = 'Tooltip:\n\n'
                 '*OPTIONAL*')

    extrinsicarg1_entry = Entry(framer.Objframe, width = 4)
    extrinsicarg1_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    extrinsicarg1_entry.place (x = 440, y = 380)

    extrinsicarg2_entry = Entry(framer.Objframe, width = 4)
    extrinsicarg2_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    extrinsicarg2_entry.place (x = 485, y = 380)

    add_extrinsic_button = Button(framer.Objframe, text="add", command = lambda: addhabitat(optionVarExtr, extrinsicgroup_entry, extrinsicarg1_entry,
                                                                                 extrinsicarg2_entry, extrinsiclist, extrinsicvaluelist,
                                                                                 "extr", debug_textfield, optionVarExtrinsiclist, OptionMenuExtrinsiclist, componentlist_textfield))
    add_extrinsic_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_extrinsic_button.place ( x = 560, y = 378 )

    tooltip.CreateToolTip(add_extrinsic_button, text = 'Tooltip:\n\n'
                 'Klick this button to add an extrinsic habitat\n'
                 'to the list of extrinsic habitats of the current object')

    affordance_label = Label(framer.Objframe, text = "<Affordances>", foreground = "white", background = "#404040", font=(None, 14))
    affordance_label.place (x = 50, y = 410)

    affordanceformula_label = Label(framer.Objframe, text = "Formula:", foreground = "white", background = "#404040", font=(None, 12))
    affordanceformula_label.place (x = 100, y = 440)

    optionVarAfford = StringVar()
    optionVarAfford.set("grasp")

    optionmenuafford = OptionMenu(framer.Objframe, optionVarAfford, "grasp", "grasp", "lift", "roll", "slide", "put_on", "put_in")
    optionmenuafford.place(x = 190, y = 440)
    optionmenuafford.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    affordanceformulagroup_entry = Entry(framer.Objframe, width = 4)
    affordanceformulagroup_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    affordanceformulagroup_entry.place (x = 370, y = 440)

    affordarg1_entry = Entry(framer.Objframe, width = 4)
    affordarg1_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    affordarg1_entry.place (x = 440, y = 440)

    affordarg2_entry = Entry(framer.Objframe, width = 4)
    affordarg2_entry.configure(relief = RIDGE, width = 3, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    affordarg2_entry.place (x = 485, y = 440)

    add_affordanceformula_button = Button(framer.Objframe, text="add", command = lambda: addformula(optionVarAfford, affordanceformulagroup_entry,
                                                                                         affordarg1_entry, affordarg2_entry, debug_textfield,
                                                                                         optionVarAffordancelist, OptionMenuAffordancelist, componentlist_textfield))
    add_affordanceformula_button.config(image = framer.smallbtnpic, borderwidth = 0, bg = "#a3ff8f", activebackground= "#a3ff8f", compound = CENTER, foreground = "white", activeforeground = "#a3ff8f", font=(None, 13))
    add_affordanceformula_button.place ( x = 560, y = 438 )

    tooltip.CreateToolTip(add_affordanceformula_button, text = 'Tooltip:\n\n'
                 'Klick this button to add an affordance formula\n'
                 'to the list of affordance formulas of the current object')

    embodiement_label = Label(framer.Objframe, text="<Embodiement>", foreground = "white", background = "#404040", font=(None, 14))
    embodiement_label.place (x = 50, y = 470)

    scale_label = Label(framer.Objframe, text = "Scale:", foreground = "white", background = "#404040", font=(None, 12))
    scale_label.place (x = 100, y = 500)

    optionVarScale = StringVar()
    optionVarScale.set("agent")

    OptionMenuScale = OptionMenu(framer.Objframe, optionVarScale, "< agent", "< agent", "agent", "> agent")
    OptionMenuScale.place(x = 190, y = 500)
    OptionMenuScale.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))

    movable_label = Label(framer.Objframe, text = "Movable:", foreground = "white", background = "#404040", font=(None, 12))
    movable_label.place (x = 100, y = 530)

    optionVarMovable = StringVar()
    optionVarMovable.set("True")

    OptionMenuMovable = OptionMenu(framer.Objframe, optionVarMovable, "True", "True", "False")
    OptionMenuMovable.place(x = 190, y = 530)
    OptionMenuMovable.config(width=145, height = 14, image = framer.menutickpic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#a3ff8f", font=(None, 12))
    

    componentlist_label = Label(framer.Objframe, text = "File Preview:", foreground = "white", background = "#404040", font=(None, 14))
    componentlist_label.place (x = 670, y = 50)

    componentlist_textfield = tk.Text(framer.Objframe, height=10, width=40)
    componentlist_textfield.configure(relief = RIDGE, bd = 2, foreground = "white", insertbackground = "white", background = "#505050", font=(None, 12))
    componentlist_textfield.place ( x = 670, y = 80 )

    optionVarComponentlist = StringVar()
    optionVarComponentlist.set("Select Component")

    OptionMenuComponentlist = OptionMenu(framer.Objframe, optionVarComponentlist, "Select Component")
    OptionMenuComponentlist.place(x = 670, y = 300)
    OptionMenuComponentlist.config(width=250, height = 16, image = framer.cancelmenupic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#fa7878", font=(None, 12))
    OptionMenuComponentlist['menu'].entryconfig(1, background = "#404040" ,activebackground = "#404040", foreground = "white", activeforeground = "#fa7878")

    removecompo_button = Button(framer.Objframe, text="remove", command = lambda: removefromlist(componentlist, componentlist_textfield, OptionMenuComponentlist, optionVarComponentlist, debug_textfield))
    removecompo_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    removecompo_button.place ( x = 960, y = 300 )


    optionVarIntrinsiclist = StringVar()
    optionVarIntrinsiclist.set("Select Intrinsic Habitat")
    
    OptionMenuIntrinsiclist = OptionMenu(framer.Objframe, optionVarIntrinsiclist, "Select Intrinsic Habitat")
    OptionMenuIntrinsiclist.place(x = 670, y = 348)
    OptionMenuIntrinsiclist.config(width=250, height = 16, image = framer.cancelmenupic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#fa7878", font=(None, 12))

    removeintr_button = Button(framer.Objframe, text="remove", command = lambda: removefromlist(intrinsiclist, componentlist_textfield, OptionMenuIntrinsiclist, optionVarIntrinsiclist, debug_textfield))
    removeintr_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    removeintr_button.place ( x = 960, y = 348 )

    optionVarExtrinsiclist = StringVar()
    optionVarExtrinsiclist.set("Select Extrinsic Habitat")
    
    OptionMenuExtrinsiclist = OptionMenu(framer.Objframe, optionVarExtrinsiclist, "Select Extrinsic Habitat")
    OptionMenuExtrinsiclist.place(x = 670, y = 380)
    OptionMenuExtrinsiclist.config(width=250, height = 16, image = framer.cancelmenupic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#fa7878", font=(None, 12))

    removeextr_button = Button(framer.Objframe, text="remove", command = lambda: removefromlist(extrinsiclist, componentlist_textfield, OptionMenuExtrinsiclist, optionVarExtrinsiclist, debug_textfield))
    removeextr_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    removeextr_button.place ( x = 960, y = 380 )


    optionVarAffordancelist = StringVar()
    optionVarAffordancelist.set("Select Affordance Formula")
    
    OptionMenuAffordancelist = OptionMenu(framer.Objframe, optionVarAffordancelist, "Select Affordance Formula")
    OptionMenuAffordancelist.place(x = 670, y = 440)
    OptionMenuAffordancelist.config(width=250, height = 16, image = framer.cancelmenupic, anchor = "w", borderwidth = 0,  indicatoron=0, compound = LEFT, bg = "#404040", activebackground= "#404040", foreground = "white", activeforeground = "#fa7878", font=(None, 12))

    removeAffordance_button = Button(framer.Objframe, text="remove", command = lambda: removefromlist(affordanceformulalist, componentlist_textfield, OptionMenuAffordancelist, optionVarAffordancelist, debug_textfield))
    removeAffordance_button.config(image = framer.cancelbtnpic, borderwidth = 0, bg = "#fa7878", activebackground= "#fa7878", compound = CENTER, foreground = "white", activeforeground = "#fa7878", font=(None, 13))
    removeAffordance_button.place ( x = 960, y = 440 )

    drdwnlistgrn = [option, optionmenuhead, optionmenuconc, optionmenuint, optionmenuext, optionmenuafford, OptionMenuScale, OptionMenuMovable]
    drdwnlistred = [OptionMenuComponentlist, OptionMenuIntrinsiclist, OptionMenuExtrinsiclist, OptionMenuAffordancelist]
    for drdwn in drdwnlistgrn:
        i = 0
        while i < drdwn['menu'].index('end') + 1:
            drdwn['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#a3ff8f")
            i += 1

    
    for drdwn in drdwnlistred:
        i = 0
        while i < drdwn['menu'].index('end') + 1:
            drdwn['menu'].entryconfig(i, background = "#404040" ,activebackground = "#505050", foreground = "white", activeforeground = "#fa7878")
            i += 1
        drdwn['menu'].add_command(label = "                                                                       ", command=tk._setit(optionVarComponentlist, "Select Component"))
        drdwn['menu'].entryconfig(1, background = "#404040" ,activebackground = "#404040", foreground = "white", activeforeground = "#fa7878")





        
