from tkinter import *

def show_entry_content():
    # Get the content of the entry widget
    content = entry.get()
    # Display the content in a label
    label.config(text=f"Entry content: {content}")

root = Tk()

# Create an Entry widget with various options
entry = Entry(
    root,
    width=30,  # Width of the entry widget
    font=("Helvetica", 14),  # Font type and size
    fg="blue",  # Foreground (text) color
    bg="lightgray",  # Background color
    show="*",  # Character to display instead of actual text (useful for passwords)
    justify=CENTER,  # Text alignment (LEFT, CENTER, RIGHT)
    state=NORMAL  # State of the entry widget (NORMAL, DISABLED, READONLY)
)
entry.pack(padx=10, pady=10)

# Create a Button to show the content of the Entry widget
button = Button(
    root,
    text="Show Entry Content",
    command=show_entry_content
)
button.pack(pady=10)

# Create a Label to display the content of the Entry widget
label = Label(root, text="")
label.pack(pady=10)

root.mainloop()