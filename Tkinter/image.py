from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def load_image():
    # Get the image path from the entry widget
    image_path = entry.get()
    try:
        # Open the image file
        img = Image.open(image_path)
        # Resize the image to fit the label
        img = img.resize((300, 300), Image.LANCZOS)
        # Convert the image to a Tkinter-compatible format
        img_tk = ImageTk.PhotoImage(img)
        # Update the label with the new image
        label.config(image=img_tk)
        label.image = img_tk  # Keep a reference to avoid garbage collection
    except Exception as e:
        label.config(text=f"Error loading image: {e}")

def browse_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        entry.delete(0, END)
        entry.insert(0, file_path)

root = Tk()
root.title("Image Viewer")

# Set the window icon
root.iconbitmap('icon_512.ico')  

# Create an Entry widget to input the image path
entry = Entry(root, width=50)
entry.pack(padx=10, pady=10)

# Create a Button to browse for an image file
browse_button = Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=5)

# Create a Button to load the image
load_button = Button(root, text="Load Image", command=load_image)
load_button.pack(pady=5)

# Create a Label to display the image
label = Label(root, text="No image loaded")
label.pack(padx=10, pady=10)

root.mainloop()