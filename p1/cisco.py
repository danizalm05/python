#https://edube.org/learn/programming-essentials-in-python/how-functions-communicate-with-their-environment-2
#!/usr/bin/env python3

from tkinter import *

root = Tk() 							# Create the root (base) window 

w = Label(root, text="Hello, world!") 	# Create a label with words

w.pack() 								# Put the label into the window

root.mainloop()