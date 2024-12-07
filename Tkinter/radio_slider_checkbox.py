from tkinter import *
from tkinter import messagebox

def show_selected_option():
    selected_option = var.get()
    label.config(text=f"Selected option: {selected_option}")

def show_message():
    messagebox.showinfo("Information", "This is an info message box")

def toggle_checkbox():
    if checkbox_var.get() == 1:
        messagebox.showinfo("Checkbox", "Checkbox is checked")
    else:
        messagebox.showinfo("Checkbox", "Checkbox is unchecked")

def update_slider_label(value):
    slider_label.config(text=f"Slider value: {value}")

root = Tk()
root.title("Tkinter Widgets Example")

# Create an IntVar to store the selected option for radio buttons
var = IntVar()
var.set(1)  # Set the default selected option

# Create radio buttons
radio1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=show_selected_option)
radio2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=show_selected_option)
radio3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=show_selected_option)

# Pack the radio buttons
radio1.pack(anchor=W)
radio2.pack(anchor=W)
radio3.pack(anchor=W)

# Create a label to display the selected option
label = Label(root, text="Selected option: 1")
label.pack(pady=10)

# Create a button to show a message box
message_button = Button(root, text="Show Message", command=show_message)
message_button.pack(pady=10)

# Create a checkbox
checkbox_var = IntVar()
checkbox = Checkbutton(root, text="Check Me", variable=checkbox_var, command=toggle_checkbox)
checkbox.pack(pady=10)

# Create a slider
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=update_slider_label)
slider.pack(pady=10)

# Create a label to display the slider value
slider_label = Label(root, text="Slider value: 0")
slider_label.pack(pady=10)

root.mainloop()