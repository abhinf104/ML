from tkinter import *

# Function to delete the button
def delete_button():
    button1.destroy()
    
def add_title():
    global count
    count+=1
    if(count>0):
        label=Label(frame,text=f"Button is clicked {count}")
        label.pack()
    

root = Tk()
count=0
# Create a frame
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Create a button inside the frame
button1 = Button(frame, text="Click Me", command=add_title)
button1.pack()


# Create another button to delete the first button
delete_button = Button(root, text="Delete Button", command=delete_button)
delete_button.pack(pady=10)

root.mainloop()