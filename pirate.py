import random

class piratename () :
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

mypirate = piratename("Landlubber","of Dark Water")
print (mypirate.originalfirst,mypirate.originallast)
print(mypirate.createname())
