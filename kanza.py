import matplotlib.pyplot as plt
from tkinter import *
# For Opening Plot in the same window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np              

# Function to plot vectors - for the button
def plot_vectors():
    x1 = float(vector_a_x_entry.get())
    y1 = float(vector_a_y_entry.get())
    z1 = float(vector_a_z_entry.get())

    x2 = float(vector_b_x_entry.get())
    y2 = float(vector_b_y_entry.get())
    z2 = float(vector_b_z_entry.get())

    fig = plt.figure(figsize=(50,50),dpi=100)
    plt.style.use('seaborn-v0_8')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    ax.quiver(0, 0, 0, x1, y1, z1,color='purple',linewidth=3,label="vector 1",length=5.1)
    ax.quiver(0, 0, 0, x2, y2, z2, color='red',linewidth=3,label="vector 2",length=5.1)

    cross_product = np.dot([x1, y1, z1], [x2, y2, z2])
    ax.scatter(cross_product,0,0,s=50,color="blue")
    ax.set_xlabel('X-AXIS', color='blue')
    ax.set_ylabel('Y-AXIS', color='blue')
    ax.set_zlabel('Z-AXIS', color='blue')
    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])
    ax.set_zlim([-50, 50])
    ax.set_aspect('equal')
    ax.tick_params(labelsize=9)

    # For opening the graph in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

import tkinter as tk
from PIL import Image, ImageTk


class HoverButton(tk.Button):
    def _init_(self, master, **kw):
        tk.Button._init_(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self, e):
        self["background"] = self.defaultBackground

# Create the tkinter window
root = tk.Tk()
root.title("Image Window")

# Create a frame for the header
header_frame = tk.Frame(root, bg='#EEEEE5', bd=0, highlightthickness=4, highlightbackground='#0000FF')

header_frame.pack(fill='x')

# Create a label for the header text
header_label = tk.Label(header_frame, text='3D Dot Product Visualizer', font=('Times New Roman Bold', 24),
                        fg='#0000FF', bg='#EEEEE5')
header_label.pack(pady=10)

# Set the window size
root.state("zoomed")

# Open the image using the Image module from PIL
#pil_image = Image.open('D:\c1.png')

# Resize the image to the window size
#resized_image = pil_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))

# Create a PhotoImage object from the resized image
#bg_image = ImageTk.PhotoImage(resized_image)

# Create a label widget with the image as the background
#bg_label = tk.Label(root, image=bg_image)

# Add the label to the window
#bg_label.pack(fill="both", expand=True)



# Create a frame for the input vectors
vector_frame = tk.Frame(root, bg='#F5F5F5', bd=0, highlightthickness=4, highlightbackground='#0000FF')
vector_frame.place(relx=0.80, rely=0.45, height=290, anchor=tk.CENTER)

# Create the input vector labels
vector_a_label = tk.Label(vector_frame, text="Vector A", font=("Times New Roman Bold", 20, 'bold'), bg='#F5F5F5',
                          fg='#0000FF')
vector_a_label.grid(row=0, column=0, pady=20)

vector_b_label = tk.Label(vector_frame, text="Vector B", font=("Times New Roman Bold", 20, 'bold'), bg='#F5F5F5',
                          fg='#0000FF')
vector_b_label.grid(row=2, column=0, pady=20)

# Create the entry boxes for Vector A
vector_a_x_label = tk.Label(vector_frame, text="X", font=("Arial", 16), bg='#F5F5F5', fg='#333333')
vector_a_x_label.grid(row=1, column=0)
vector_a_x_entry = tk.Entry(vector_frame, width=7, font=("Arial", 16), justify="center")
vector_a_x_entry.grid(row=1, column=1, padx=10)

vector_a_y_label = tk.Label(vector_frame, text="Y", font=("Arial", 16), bg='#F5F5F5', fg='#333333')
vector_a_y_label.grid(row=1, column=2)
vector_a_y_entry = tk.Entry(vector_frame, width=7, font=("Arial", 16), justify="center")
vector_a_y_entry.grid(row=1, column=3, padx=10)

vector_a_z_label = tk.Label(vector_frame, text="Z", font=("Arial", 16), bg='#F5F5F5', fg='#333333')
vector_a_z_label.grid(row=1, column=4)
vector_a_z_entry = tk.Entry(vector_frame, width=7, font=("Arial", 16), justify="center")
vector_a_z_entry.grid(row=1, column=5, padx=10)

# Create the entry boxes for Vector B
vector_b_x_label = tk.Label(vector_frame, text="X", font=("Arial", 16), bg='#F5F5F5', fg='#333333')
vector_b_x_label.grid(row=3, column=0)
vector_b_x_entry = tk.Entry(vector_frame, width=7, font=("Arial", 16), justify="center")
vector_b_x_entry.grid(row=3, column=1, padx=10)

vector_b_y_label = tk.Label(vector_frame, text="Y", font=("Arial", 16), bg='#F5F5F5', fg='#333333')
vector_b_y_label.grid(row=3, column=2)
vector_b_y_entry = tk.Entry(vector_frame, width=7, font=("Arial", 16), justify="center")
vector_b_y_entry.grid(row=3, column=3, padx=10)

vector_b_z_label = tk.Label(vector_frame, text="Z", font=("Arial", 16), bg='#F5F5F5', fg='#333333')
vector_b_z_label.grid(row=3, column=4)
vector_b_z_entry = tk.Entry(vector_frame, width=7, font=("Arial", 16), justify="center")
vector_b_z_entry.grid(row=3, column=5, padx=10)

# Create a frame for the button
button_frame = tk.Frame(root, bg='#F5F5F5', bd=0, highlightthickness=0)                       
button_frame.place(relx=0.9, rely=0.9, anchor=tk.SE)

button3 = HoverButton(button_frame, font=("Times New Roman Bold", 30), text="Plot", bg='#0000FF', fg='white',
                      activebackground='#7F7FFF', highlightthickness=0, width=10, highlightbackground='black',command=plot_vectors)
button3.pack()

# Creating a frame for the plot
plot_frame = tk.Frame(root, bg='#EEEEE5', highlightthickness=4, highlightbackground='#0000FF')
plot_frame.place(relx=0.31, rely=0.55, height=500, width=800, anchor=tk.CENTER)

root.mainloop()             
