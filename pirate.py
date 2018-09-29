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

mypirate = Piratename("Landlubber","of Dark Water")
print (mypirate.originalfirst,mypirate.originallast)
print(mypirate.createname())

root = Tk()

ft ="Impact 20"

title = Label(root, text = "What's your Pirate Name?", font = "Impact 40")
firstlabel = Label(root, text = "First Name", font = ft)
firsttext = Entry(root, font = ft)
lastlabel = Label(root, text = "Last Name", font = ft)
lasttext = Entry(root, font = ft)
btn = Button(root, font = ft, text = "What's my Pirate Name?")
banner = PhotoImage(file = "pirate-banner.gif")
banner = banner.subsample(3,3)
banner = banner.zoom(2,2)
output = Label(root, image = banner)

title.grid(row = 0, column = 0, columnspan = 2)
firstlabel.grid(row = 1, column = 0)
firsttext.grid(row = 1, column = 1)
lastlabel.grid(row = 2, column = 0)
lasttext.grid(row = 2, column = 1)
btn.grid(row = 3, column = 0, columnspan = 2)
output.grid(row = 4, column = 0, columnspan = 2)




root.mainloop()
