from tkinter import *

root = Tk()

# using grid
# Label
label = Label(root, text="Hello World")
label.grid(row=0, column=0, padx=10, pady=10)  # Place the label in the first row and first column with padding

# Button
button = Button(root, text="Click Me")
button.grid(row=0, column=1, sticky=W+E)  # Place the button in the first row and second column, stretching horizontally

# Entry
entry = Entry(root)
entry.grid(row=1, column=0, columnspan=2, ipadx=50, ipady=50)  # Place the entry in the second row, spanning two columns with internal padding

# Checkbutton
checkbutton = Checkbutton(root, text="Check Me")
checkbutton.grid(row=2, column=0, columnspan=2, sticky=W)  # Place the checkbox in the third row, spanning two columns, aligned to the left

# Using place geometry manager
# Radiobutton
radiobutton1 = Radiobutton(root, text="Option 1", value=1)
radiobutton2 = Radiobutton(root, text="Option 2", value=2)
radiobutton1.place(x=10, y=100)  # Place the first radio button at absolute position (10, 100)
radiobutton2.place(x=10, y=130)  # Place the second radio button at absolute position (10, 130)

# Listbox
listbox = Listbox(root)
listbox.insert(1, "Item 1")  # Insert first item into the listbox
listbox.insert(2, "Item 2")  # Insert second item into the listbox
listbox.place(x=150, y=100, width=100, height=50)  # Place the listbox at absolute position (150, 100) with specified width and height


#  event loop continuously checks for events and processes them, ensuring that the application remains responsive.
root.mainloop()  # Start the Tkinter event loop