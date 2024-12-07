from tkinter import *

root = Tk()

# Create a button with various options
button1 = Button(
    root,
    text="Button 1",  # Text displayed on the button
    padx=5,  # Horizontal padding inside the button
    pady=10,  # Vertical padding inside the button
    command=lambda: print("Button 1 clicked"),  # Function to call when the button is clicked
    fg="white",  # Foreground (text) color
    bg="blue",  # Background color
    font=("Helvetica", 16),  # Font type and size
    relief=RAISED,  # Type of border (RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID)
    bd=5,  # Border width
    width=20,  # Width of the button
    height=2,  # Height of the button
    activeforeground="yellow",  # Foreground color when the button is pressed
    activebackground="red",  # Background color when the button is pressed
    state=NORMAL,  # State of the button (NORMAL, DISABLED, ACTIVE)
    cursor="hand2"  # Cursor type when hovering over the button
)

# Place the button using grid geometry manager
button1.grid(row=0, column=0, padx=10, pady=10)  # Position the button in the grid with external padding

root.mainloop()  # Start the Tkinter event loop