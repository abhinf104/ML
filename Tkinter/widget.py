from tkinter import *

root = Tk()


# Label
label = Label(root, text="Hello World")
label.pack(side=TOP, padx=10, pady=10)  # Pack the label at the top with padding

# Button
button = Button(root, text="Click Me")
button.pack(side=LEFT, fill=Y, expand=True)  # Pack the button on the left, filling vertically and expanding

# Entry
entry = Entry(root)
entry.pack(side=RIGHT, ipadx=5, ipady=5)  # Pack the entry on the right with internal padding

# Checkbutton
checkbutton = Checkbutton(root, text="Check Me")
checkbutton.pack(side=BOTTOM, fill=X)  # Pack the checkbox at the bottom, filling horizontally


# Radiobutton
radiobutton1 = Radiobutton(root, text="Option 1", value=1)
radiobutton2 = Radiobutton(root, text="Option 2", value=2)
radiobutton1.pack()  # Display the first radio button
radiobutton2.pack()  # Display the second radio button

# Listbox
listbox = Listbox(root)
listbox.insert(1, "Item 1")  # Insert first item into the listbox
listbox.insert(2, "Item 2")  # Insert second item into the listbox
listbox.pack()  # Display the listbox

root.mainloop()  # Start the Tkinter event loop

