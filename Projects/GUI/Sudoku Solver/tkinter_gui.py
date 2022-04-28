from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Sudoku Solver and Player")
# Window parameters
root.geometry("750x600")  # width x height
root.minsize(500, 500)  # width,height
root.maxsize(1080, 1080)  # width,height
###################################################################################################################

# Important Label options
# text - adds text
# bd-background
# fg-foreground
# font - sets the font
# font=("comicsans 10 bold")
# padx,pady - padding for x and y
# relief- border styling - SUNKEN,RAISED,GROOVE,RIDGE
title_label = Label(text="Solve or Play the mindful game of SUDOKU", bg="grey", fg="yellow",
                    padx=10, pady=10, font="comicsansms 15 bold", borderwidth=5, relief=RAISED)
###################################################################################################################

# Important Pack options
# anchor = nw
# side= top,bottom,left,right
# Need to pack after adding any widget
title_label.pack(side=TOP, anchor="sw", fill=X, padx=5, pady=5)
###################################################################################################################

# Frames-kinda like boxes where we draw our widgets separetly
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
Label(f1, text="Sudoku solve left side").pack(pady=100,padx=150)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
Label(f2, text="Sudoku solve top side").pack(pady=20)
f2.pack(side=TOP, fill=X)

# Photo Loading
# photo = PhotoImage(file="image.png")
# photo_label = Label(image=photo)
# photo_label.pack()

root.mainloop()
