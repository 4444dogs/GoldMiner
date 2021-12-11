from tkinter import *

def mined():
    lbl.configure(text="You have mined gold!")

window = Tk()
window.title("Super Cool Random App")
window.state('zoomed')

btn = Button(window, text="Mine Gold", command=mined)
btn.grid(column=0, row=0)

lbl = Label(window, text="You have not mined gold.")
lbl.grid(column=1, row=0)

window.mainloop()
