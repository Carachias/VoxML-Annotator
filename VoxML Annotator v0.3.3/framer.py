from tkinter import *



Window = Tk()
Window.title("VoxML Annotator")
Window.geometry ("1600x900")

topbgpic = PhotoImage(file="ressources/topbg.png")
framebgpic = PhotoImage(file="ressources/framebg.png")
helpbgpic = PhotoImage(file="ressources/helpbg.png")
changelogbgpic = PhotoImage(file="ressources/changelogbg.png")
placeholderbgpicside = PhotoImage(file="ressources/placeholderside.png")
btnpic = PhotoImage(file="ressources/button.png")
smallbtnpic = PhotoImage(file="ressources/smallbutton.png")
cancelbtnpic = PhotoImage(file="ressources/cancelbutton.png")
largebtnpic = PhotoImage(file="ressources/largebutton.png")
enttypeslabelpic = PhotoImage(file="ressources/enttypesbglabel.png")
htmlfunslabelpic = PhotoImage(file="ressources/htmlfunsbglabel.png")
otherfunslabelpic = PhotoImage(file="ressources/otherfunsbglabel.png")
cancelmenupic = PhotoImage(file="ressources/cancelmenu.png")
menutickpic = PhotoImage(file="ressources/menutick.png")
tutbgpic = PhotoImage(file="ressources/tutbg.png")

Topframe = Frame(Window, width = 1600, height = 150)
Topframe.place (x = 0, y = 0)

topbglab = Label(Topframe,image = topbgpic, width = 1600, height = 150)
topbglab.image = topbgpic
topbglab.place (x = -2, y = -2)

Helpframe = Frame(Window, width = 500, height = 750, bg ="#444444")
Helpframe.place (x = 650, y = 150)

helpbglab = Label(Helpframe,image = helpbgpic, width = 500, height = 750)
helpbglab.image = helpbgpic
helpbglab.place (x = -2, y = -2)

Changelogframe = Frame(Window, width = 500, height = 750, bg ="#444444")
Changelogframe.place (x = 650, y = 150)

changelogbglab = Label(Changelogframe,image = changelogbgpic, width = 500, height = 750)
changelogbglab.image = changelogbgpic
changelogbglab.place (x = -2, y = -2)
    
Objframe = Frame(Window, width = 1150, height = 750, bg ="#444444" )
Objframe.place (x = 0, y = 150)

objbglab = Label(Objframe,image = framebgpic, width = 1150, height = 750)
objbglab.image = framebgpic
objbglab.place (x = -2, y = -2)

Progrframe = Frame(Window, width = 1150, height = 750, bg ="#444444" )
Progrframe.place (x = 0, y = 150)

progbglab = Label(Progrframe,image = framebgpic, width = 1150, height = 750)
progbglab.image = framebgpic
progbglab.place (x = -2, y = -2)

Attrframe = Frame(Window, width = 1150, height = 750, bg ="#444444" )
Attrframe.place (x = 0, y = 150)

attrbglab = Label(Attrframe,image = framebgpic, width = 1150, height = 750)
attrbglab.image = framebgpic
attrbglab.place (x = -2, y = -2)

Relatframe = Frame(Window, width = 1150, height = 750, bg ="#444444" )
Relatframe.place (x = 0, y = 150)

relatbglab = Label(Relatframe,image = framebgpic, width = 1150, height = 750)
relatbglab.image = framebgpic
relatbglab.place (x = -2, y = -2)

Funcframe = Frame(Window, width = 1150, height = 750, bg ="#444444" )
Funcframe.place (x = 0, y = 150)

funcbglab = Label(Funcframe,image = framebgpic, width = 1150, height = 750)
funcbglab.image = framebgpic
funcbglab.place (x = -2, y = -2)

Inspectframe = Frame(Window, width = 450, height = 750, bg = "#444444" )
Inspectframe.place (x =1150, y = 150)


Placeholderframeside = Frame(Window, width = 450, height = 750, bg = "#444444" )
Placeholderframeside.place (x =1150, y = 150)

phbglab = Label(Placeholderframeside,image = placeholderbgpicside, width = 450, height = 750)
phbglab.image = placeholderbgpicside
phbglab.place (x = -3, y = -2)

Placeholderframe = Frame(Window, width = 1150, height = 750, bg ="#444444" )
Placeholderframe.place (x = 0, y = 150)

phmbglab = Label(Placeholderframe,image = tutbgpic, width = 1150, height = 750, background = "green")
phmbglab.image = framebgpic
phmbglab.place (x = -2, y = -2)
