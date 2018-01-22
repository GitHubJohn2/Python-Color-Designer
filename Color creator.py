# Composite Color Designer
# (c) 2018 John A. Oakey
# Permission is given to use for any non-commercial purpose

from tkinter import *

root = Tk()
# create a control value to hold composite color code
compcode = StringVar()
compcode.set("#000000")
mixcolor=StringVar()
mixcolor.set("#000000")  # will need this when we go to color our frame
redval=IntVar(0)
blueval=IntVar(0)
greenval=IntVar(0)

# take a truncated value from a scale widget and get the hex digits for its value
def newval(scaleval):
    scalehex = str(hex(scaleval)[2:])
    if len(scalehex) == 1:
        scalehex = "0" + scalehex
    return scalehex


# construct a hexidecimal string that will work setting colors
def fixmix(*args):
    mixcolor.set("#" + str(newval(redval.get())) + str(newval(greenval.get())) + str(newval(blueval.get())))
    mixframe["bg"] = mixcolor.get()
    return()


# get red scale value, show value, update scale color, update mixed color code
def redchg(self):
    redvaluelabel["text"] = str(redval.get())
    scalehex = newval(redval.get())
    tempcode = compcode.get()
    compcode.set("#" + scalehex + tempcode[3:7])
    scalehex = "#" + scalehex + "0000"
    redscale["bg"] = scalehex
    fixmix()


# get green scale value, show value, update scale color, update mixed color code
def greenchg(self):
    greenvaluelabel["text"] = str(greenval.get())
    scalehex = newval(greenval.get())
    tempcode = compcode.get()
    compcode.set(tempcode[0:3] + scalehex + tempcode[5:8])
    scalehex = "#00" + scalehex + "00"
    greenscale["bg"] = scalehex
    fixmix()


# get blue scale value, show value, update scale color, update mixed color code
def bluechg(self):
    bluevaluelabel["text"] = str(blueval.get())
    scalehex = newval(blueval.get())
    tempcode = compcode.get()
    compcode.set(tempcode[0:5] + scalehex)
    scalehex = "#0000" + scalehex
    bluescale["bg"] = scalehex
    fixmix()


# create toplevel frame to work in
bigframe = Frame(root, padx=20, pady=20)
bigframe.grid()

# row 0 col 0 create app label
applabel = Label(bigframe, text="Composite Color Scale Designer", font=("Arial", 22), fg="blue")
applabel.grid(column=0, row=0, columnspan=6, ipadx=3, ipady=3)

# label for red slider
redlabel = Label(bigframe, text="Red Scale", font=("Arial", 18))
redlabel.grid(column=0, row=2, columnspan=2, sticky=W)

# red slider
redscale = Scale(bigframe, from_=0, to=255, orient=HORIZONTAL, length=255, bg="#880000", command=redchg, digits=0,
                 sliderlength=20, troughcolor="white", label="Red Select Scale", bd=8, relief="sunken", variable=redval)
redscale.grid(column=0, row=3, ipady=10, ipadx=10, columnspan=5, sticky=W)

# redvalue frame
redvalueframe = LabelFrame(bigframe, height=15, width=30, text="red value", relief="raised", bd=10)
redvalueframe.grid(column=4, row=3, columnspan=2, rowspan=2, ipady=10, ipadx=10, sticky=NE)

# red value label to go in redvalueframe
redvaluelabel = Label(redvalueframe, text="000", font=("Arial", 20), justify="right")
redvaluelabel.grid(ipadx=10)

# label for green slider
greenlabel = Label(bigframe, text="Green Scale", font=("Arial", 18))
greenlabel.grid(column=0, row=4, columnspan=2, sticky=W)

# green slider
greenscale = Scale(bigframe, from_=0, to=255, orient=HORIZONTAL, length=255, bg="#008800", command=greenchg, digits=0,
                   sliderlength=20, troughcolor="white", label="Green Select Scale", bd=8, relief="sunken", variable=greenval)
greenscale.grid(column=0, row=5, ipady=10, ipadx=10, columnspan=5, sticky=W)

# green value frame
greenvalueframe = LabelFrame(bigframe, height=15, width=30, text="green value", relief="raised", bd=10)
greenvalueframe.grid(column=4, row=5, columnspan=2, rowspan=2, ipady=10, ipadx=10, sticky=NE)

# green value label to go in greenvalueframe
greenvaluelabel = Label(greenvalueframe, text="000", font=("Arial", 20), justify="right")
greenvaluelabel.grid(ipadx=10)

# label for blue slider
bluelabel = Label(bigframe, text="Blue Scale", font=("Arial", 18))
bluelabel.grid(column=0, row=6, columnspan=2, sticky=W)

# blue slider
bluescale = Scale(bigframe, from_=0, to=255, orient=HORIZONTAL, length=255, bg="#000088", command=bluechg, digits=0,
                  sliderlength=20, troughcolor="white", label="Blue Select Scale", bd=8, relief="sunken", variable=blueval)
bluescale.grid(column=0, row=7, ipady=10, ipadx=10, columnspan=5, sticky=W)

# blue value frame
bluevalueframe = LabelFrame(bigframe, height=15, width=30, text="blue value", relief="raised", bd=10)
bluevalueframe.grid(column=4, row=7, columnspan=2, rowspan=2, ipady=10, ipadx=10, sticky=NE)

# blue value label to go in bluevalueframe
bluevaluelabel = Label(bluevalueframe, text="000", font=("Arial", 20), justify="right")
bluevaluelabel.grid(ipadx=10)

# label for composit display
complabel = Label(bigframe, text="Composite Color", font=("Arial", 18))
complabel.grid(column=0, row=10, columnspan=2, sticky=W)

# frame for composite color display
mixframe = Frame(bigframe, bg=mixcolor.get(), height=50, width=255, bd=8, relief="sunken")
mixframe.grid(column=0, row=11, ipady=10, ipadx=10, stick=W)

# frame to hold composite value
compvalueframe = LabelFrame(bigframe, height=25, width=30, text="composite hex value", relief="raised", bd=10)
compvalueframe.grid(column=4, row=11, columnspan=2, rowspan=2, ipady=10, ipadx=10)

# composite value label to go in compvalueframe
compvaluelabel = Label(compvalueframe, textvariable=compcode, font=("Arial", 18), justify="right")
compvaluelabel.grid(ipadx=2, sticky=N)

# footer label
footlabel = Label(bigframe, text="(c) 2017 John A. Oakey: john@johnoakey.com")
footlabel.grid(column=0, row=14, ipady=10, ipadx=10, columnspan=6)

root.mainloop()


