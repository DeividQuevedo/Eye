import cv2
import tkinter as tk
from PIL import Image, ImageTk

def show_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    label.after(10, show_frame)

cap = cv2.VideoCapture(0)

root = tk.Tk()
label = tk.Label(root)
label.pack()
show_frame()
root.mainloop()

cap.release()
cv2.destroyAllWindows()
