from tkinter import *
from tkinter import messagebox

def show_info_message():
    messagebox.showinfo("Information", "This is an info message box")

def show_warning_message():
    messagebox.showwarning("Warning", "This is a warning message box")

def show_error_message():
    messagebox.showerror("Error", "This is an error message box")

def show_question_message():
    response = messagebox.askquestion("Question", "Do you like Python?")
    if response == 'yes':
        messagebox.showinfo("Response", "You selected Yes")
    else:
        messagebox.showinfo("Response", "You selected No")

def show_yes_no_message():
    response = messagebox.askyesno("Yes/No", "Do you want to continue?")
    if response:
        messagebox.showinfo("Response", "You selected Yes")
    else:
        messagebox.showinfo("Response", "You selected No")

def show_ok_cancel_message():
    response = messagebox.askokcancel("Ok/Cancel", "Do you want to proceed?")
    if response:
        messagebox.showinfo("Response", "You selected Ok")
    else:
        messagebox.showinfo("Response", "You selected Cancel")

def show_retry_cancel_message():
    response = messagebox.askretrycancel("Retry/Cancel", "Do you want to retry?")
    if response:
        messagebox.showinfo("Response", "You selected Retry")
    else:
        messagebox.showinfo("Response", "You selected Cancel")

root = Tk()
root.title("Message Box Example")

# Create buttons to show different types of message boxes
info_button = Button(root, text="Show Info Message", command=show_info_message)
info_button.pack(pady=5)

warning_button = Button(root, text="Show Warning Message", command=show_warning_message)
warning_button.pack(pady=5)

error_button = Button(root, text="Show Error Message", command=show_error_message)
error_button.pack(pady=5)

question_button = Button(root, text="Show Question Message", command=show_question_message)
question_button.pack(pady=5)

yes_no_button = Button(root, text="Show Yes/No Message", command=show_yes_no_message)
yes_no_button.pack(pady=5)

ok_cancel_button = Button(root, text="Show Ok/Cancel Message", command=show_ok_cancel_message)
ok_cancel_button.pack(pady=5)

retry_cancel_button = Button(root, text="Show Retry/Cancel Message", command=show_retry_cancel_message)
retry_cancel_button.pack(pady=5)

root.mainloop()