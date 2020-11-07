from tkinter import *
from tkinter import ttk
import random 

root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='black')

#variables
selected_alg = StringVar()

#functions
def drawData(data):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width/ (len(data) + 1)
    offset = 30
    spacing = 10

    #normalize data
    normalizeData = [i/max(data) for i in data]

    for i, height in enumerate(normalizeData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340

        #bottom right
        x1 = (i + 1) * x_width + offset 
        y1 = c_height 

        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0+2, y0, anchor=SW, text= str(data[i]))



def Generate():
    print("Alg Selected: " + selected_alg.get())

    minVal = int(minEntry.get())
    
    maxVal = int(maxEntry.get())

    size = int(sizeEntry.get())

    data =[]
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1)) #maxVal inclusive
    
    # === TEST ===
    # data = [1, 2, 4, 6]
    drawData(data)

#frame and base layout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0,padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1,column=0, padx=10, pady=5)

#User Interface Area

#Row[0]
Label(UI_frame, text="Algorithm : ", bg='grey').grid(row=0,column=0, padx=10, pady=5, sticky=W)

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(UI_frame, text="Generate", command=Generate, bg='red' ).grid(row=0, column=2, padx=5, pady=5)

#Row[1]
Label(UI_frame, text="Size : ", bg='grey').grid(row=1,column=0, padx=10, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1,column=1, padx=10, pady=5, sticky=W)

Label(UI_frame, text="Min Value : ", bg='grey').grid(row=1,column=2, padx=10, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1,column=3, padx=10, pady=5, sticky=W)

Label(UI_frame, text="Max Value : ", bg='grey').grid(row=1,column=4, padx=10, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1,column=5, padx=10, pady=5, sticky=W)

root.mainloop()