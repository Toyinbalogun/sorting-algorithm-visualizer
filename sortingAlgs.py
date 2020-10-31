from tkinter import *
from tkinter import ttk
import random 

root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='black')

#frame and base layout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0,padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1,column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0,column=0, padx=10, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, vlues=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0)
#Row[1]


root.mainloop()