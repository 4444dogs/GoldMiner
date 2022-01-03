##Installing Tkinter
from tkinter import *

##What Happens When You Mine Gold
def mined():
    lbl.configure(text="You have mined gold!")


##Window Settings
window = Tk()
window.title("Gold Miner")
window.state('zoomed')

##The 'Mine Gold' Button
btn = Button(window, text="Mine Gold", command=mined)
btn.grid(column=0, row=0)

##The Text
lbl = Label(window, text="You have not mined gold.")
lbl.grid(column=1, row=0)

##The Window
window.mainloop()

##NOTES
##This app was made as a joke but I continue to update anyways. Anyone can use the code above.