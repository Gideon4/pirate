import random
from tkinter import *

class Piratename () :
    
    originalfirst = " "
    originallast = " "

    firstlist = ["Two-Toes","Scallywag","Dead-Man"]
    lastlist = [" Chumbucket"," of Atlantis"," Kidd"]

    def __init__(self,firstname,lastname) :
        self.originalfirst = firstname
        self.originallast = lastname

    def createname (self) :
        x = random.randint(0,len(self.firstlist)-1)
        y = random.randint(0,len(self.lastlist)-1)
        return self.firstlist[x] + self.lastlist[y]

def buttonclick():
    
    #get the info out of the boxes
    first = firsttext.get()
    last = lasttext.get()
    
    #create instance of our generator class
    mygen = Piratename(first, last)
    
    #run the generator
    pname = mygen.createname()
    
    #show it on the screen
    output.config(text = pname, font = ft, image = banner, compound = CENTER)

root = Tk()

ft ="Impact 20"

title = Label(root, text = "What's your Pirate Name?", font = "Impact 40")
firstlabel = Label(root, text = "First Name", font = ft)
firsttext = Entry(root, font = ft)
lastlabel = Label(root, text = "Last Name", font = ft)
lasttext = Entry(root, font = ft)
btn = Button(root, font = ft, text = "What's my Pirate Name?", command = buttonclick)
banner = PhotoImage(file = "pirate-banner.gif")
banner = banner.zoom(2,2)
banner = banner.subsample(3,3)
output = Label(root)

title.grid(row = 0, column = 0, columnspan = 2)
firstlabel.grid(row = 1, column = 0)
firsttext.grid(row = 1, column = 1)
lastlabel.grid(row = 2, column = 0)
lasttext.grid(row = 2, column = 1)
btn.grid(row = 3, column = 0, columnspan = 2)
output.grid(row = 4, column = 0, columnspan = 2)




root.mainloop()
