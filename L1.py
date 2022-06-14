import numpy as np
from tkinter import *
root=Tk()
root.geometry("600x400")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Defining the slicing function
def sl_ar():
        i = int(input1.get())
        j = int(input2.get())
        newarr1 = arr[i:j]
        label.config(text=newarr1)
        
#display the array numbers
Message(root, text= arr,bg='light blue', font = 50).pack()

#display the the heading as slicing ration
Label(root, text = "Enter Slicing ratio: ", font = 30).pack()

#Get the start point for slice
input1 = Entry(root,width = 15,bg = "light yellow")
input1.pack()

#Display the colon(:) in between start and end point
Message(root, text= ":", bg='light blue', font = 100).pack()

#Get the end point for slice
input2 = Entry(root,width = 15,bg = "light yellow")
input2.pack()

#call the slice function when button is clicked
Button(root, text="Slice Array", command=sl_ar).pack()

#output is displayed using the label
label = Label(root,bg='light blue', font = 50)
label.pack()

root.mainloop()