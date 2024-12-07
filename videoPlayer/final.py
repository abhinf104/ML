import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
from threading import Thread
import queue
import time

class VideoPlayer:
    def __init__(self, root, video_path, frame):
        self.root = root
        self.video_path = video_path
        self.frame = frame

        # Open the video file
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            print(f"Error opening video file: {video_path}")

        # Create a label to display the video frames
        self.label = Label(self.frame)
        self.label.pack(expand=True, fill=BOTH)

        self.playing = True
        self.stop_thread = False  # Flag to stop the thread when closing the app

        # Queue to hold frames
        self.frame_queue = queue.Queue(maxsize=10)

        # Start the frame reading thread
        self.thread = Thread(target=self.read_frames)
        self.thread.daemon = True
        self.thread.start()

        # Start updating the frames in the GUI
        self.update_frame()

    def read_frames(self):
        while not self.stop_thread:
            if self.playing and self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    # Convert the frame to RGB
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    # Put the frame into the queue
                    try:
                        self.frame_queue.put(frame, timeout=1/30)
                    except queue.Full:
                        pass  # Skip frame if queue is full
                else:
                    # Restart the video when it ends
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            else:
                # If paused, sleep briefly to reduce CPU usage
                time.sleep(0.1)
        # Release the video capture when the thread is stopped
        self.cap.release()

    def update_frame(self):
        if not self.frame_queue.empty():
            frame = self.frame_queue.get()
            frame_width = self.frame.winfo_width()
            frame_height = self.frame.winfo_height()
            if frame_width > 0 and frame_height > 0:
                frame = cv2.resize(frame, (frame_width, frame_height))
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)
        # Schedule the next frame update
        self.root.after(15, self.update_frame)

    def toggle(self):
        self.playing = not self.playing
        if not self.playing:
            # Clear the frame queue to prevent displaying stale frames
            with self.frame_queue.mutex:
                self.frame_queue.queue.clear()

    def stop(self):
        # Method to stop the thread and release resources
        self.stop_thread = True

# Create the main application window
root = Tk()

# Set the window to full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{400}x{700}")

# Main frame to hold the videos
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

# Configure the grid
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.columnconfigure(0, weight=1)

# Create top and bottom frames
top_frame = Frame(main_frame)
top_frame.grid(row=0, column=0, sticky="nsew")
bottom_frame = Frame(main_frame)
bottom_frame.grid(row=1, column=0, sticky="nsew")

# Initialize the video players
video1 = VideoPlayer(root, "video1.mp4", top_frame)
video2 = VideoPlayer(root, "video2.mp4", bottom_frame)

# Function to toggle play/pause
def toggle_videos(event):
    video1.toggle()
    video2.toggle()

# Bind the toggle function to mouse click event
root.bind("<Button-1>", toggle_videos)

# Handle window close event to clean up resources
def on_closing():
    video1.stop()
    video2.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()