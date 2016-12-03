#Composite Color Designer
#(c) 2016 John A. Oakey
#Permission is given to use for any non-commercial purpose

import tkinter
from tkinter import *
tk=tkinter

master=Tk()
#create a control value to hold composite color code
compcode=StringVar()
compcode.set("#000000")
global redval, greenval, blueval, mixcolor
redval, greenval, blueval, mixcolor = "00","00","00","#000000"
#take a truncated value from a scale and get the hex digits
def newval(scaleval):
    scalehex=hex(int(scaleval,10))[2:]
    if len(scalehex)==1:
        scalehex = "0"+scalehex
    return scalehex
#construct a hexidecimal string that will work setting colors
def fixmix():
    global mixcolor
    mixcolor = "#"+redval+greenval+blueval
    mixframe["bg"]=mixcolor
#get red scale value, show value, update scale color, update mixed color code
def redchg(scaleval):
    global redval
    redvaluelabel["text"]= scaleval
    scalehex=newval(scaleval)
    redval=scalehex
    tempcode = compcode.get()
    compcode.set("#"+ scalehex + tempcode[3:7])
    scalehex = "#"+scalehex+"0000"
    redscale["bg"] = scalehex
    fixmix()
#get green scale value, show value, update scale color, update mixed color code
def greenchg(scaleval):
    global greenval
    greenvaluelabel["text"]=scaleval
    scalehex=newval(scaleval)
    greenval=scalehex
    tempcode = compcode.get()
    compcode.set(tempcode[0:3] + scalehex + tempcode[5:8])
    scalehex = "#00" + scalehex+"00"
    greenscale["bg"] = scalehex
    fixmix()
#get blue scale value, show value, update scale color, update mixed color code
def bluechg(scaleval):
    global blueval
    bluevaluelabel["text"]=scaleval
    scalehex=newval(scaleval)
    blueval=scalehex
    tempcode = compcode.get()
    compcode.set(tempcode[0:5]+scalehex)
    scalehex = "#0000"+scalehex
    bluescale["bg"] = scalehex
    fixmix()
#create toplevel frame to work in
bigframe = Frame(master,padx=20, pady=20)
bigframe.grid()
#row 0 col 0 create app label
applabel = Label(bigframe,text="Composite Color Scale Designer", font=("Arial",22), fg="blue")
applabel.grid(column=0, row=0, columnspan = 6,ipadx=3,ipady=3)

#label for red slider
redlabel = Label(bigframe,text="Red Scale", font = ("Arial",18))
redlabel.grid(column =0, row=2, columnspan=2, sticky=tk.W)
#red slider
redscale = Scale(bigframe,from_=0,to=255, orient=HORIZONTAL, length=255, bg= "#880000",command=redchg, digits=0, sliderlength= 20, troughcolor="white", label = "Red Select Scale",bd=8,relief="sunken")
redscale.grid(column = 0, row = 3,ipady=10, ipadx=10, columnspan=5, sticky=tk.W)
#redvalue frame
redvalueframe = LabelFrame(bigframe, height=15, width=30, text="red value", relief="raised", bd=10)
redvalueframe.grid(column=4,row=3, columnspan=2,rowspan=2, ipady=10, ipadx=10, sticky=tk.NE)
#red value label to go in redvalueframe
redvaluelabel = Label(redvalueframe,text="000",font=("Arial",20), justify="right")
redvaluelabel.grid(ipadx= 10)

#label for green slider
greenlabel = Label(bigframe,text="Green Scale", font = ("Arial",18))
greenlabel.grid(column =0, row=4, columnspan=2, sticky=tk.W)
#green slider
greenscale = Scale(bigframe, from_=0,to=255, orient=HORIZONTAL, length=255, bg= "#008800",command=greenchg, digits=0, sliderlength= 20, troughcolor="white", label = "Green Select Scale",bd=8,relief="sunken")
greenscale.grid(column = 0, row = 5,ipady=10, ipadx=10, columnspan=5, sticky=tk.W)
#redvalue frame
greenvalueframe = LabelFrame(bigframe, height=15, width=30, text="green value", relief="raised", bd=10)
greenvalueframe.grid(column=4,row=5, columnspan=2,rowspan=2, ipady=10, ipadx=10, sticky=tk.NE)
#red value label to go in redvalueframe
greenvaluelabel = Label(greenvalueframe,text="000",font=("Arial",20), justify="right")
greenvaluelabel.grid(ipadx= 10)

#label for blue slider
bluelabel = Label(bigframe,text="Blue Scale", font = ("Arial",18))
bluelabel.grid(column =0, row=6, columnspan=2, sticky=tk.W)
#blue slider
bluescale = Scale(bigframe, from_=0,to=255, orient=HORIZONTAL, length=255, bg= "#000088",command=bluechg, digits=0, sliderlength= 20, troughcolor="white", label = "Blue Select Scale",bd=8,relief="sunken")
bluescale.grid(column = 0, row = 7,ipady=10, ipadx=10, columnspan=5, sticky=tk.W)
#redvalue frame
bluevalueframe = LabelFrame(bigframe, height=15, width=30, text="blue value", relief="raised", bd=10)
bluevalueframe.grid(column=4,row=7, columnspan=2,rowspan=2, ipady=10, ipadx=10, sticky=tk.NE)
#red value label to go in redvalueframe
bluevaluelabel = Label(bluevalueframe,text="000",font=("Arial",20), justify="right")
bluevaluelabel.grid(ipadx= 10)

# label for composit display
complabel = Label(bigframe,text="Composite Color", font = ("Arial",18))
complabel.grid(column=0, row=10, columnspan=2, sticky=tk.W)
#frame for composite color display
mixframe = Frame(bigframe, bg=mixcolor, height=50, width = 255,bd=8,relief="sunken")
mixframe.grid(column = 0, row =11, ipady=10, ipadx=10, stick=tk.W)
#frame to hold composite value
compvalueframe = LabelFrame(bigframe, height=25, width=30, text="composite hex value", relief="raised", bd=10)
compvalueframe.grid(column=4,row=11, columnspan=2,rowspan=2, ipady=10, ipadx=10)
#composite value label to go in compvalueframe
compvaluelabel = Label(compvalueframe,textvariable=compcode,font=("Arial",18), justify="right")
compvaluelabel.grid(ipadx= 2,sticky=N)

#footer label
footlabel=Label(bigframe, text = "(c) 2017 John A. Oakey: john@johnoakey.com")
footlabel.grid(column = 0, row=14, ipady=10, ipadx=10, columnspan=6)

mainloop()

