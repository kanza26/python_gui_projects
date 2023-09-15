from tkinter import *
import tkinter as tk
import customtkinter
import tkinter.messagebox as msgbox

customtkinter.set_appearance_mode("light")  # Default
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("To do List")
window.geometry("700x400")

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        save_task()

def save_task():
    tasks = listbox.get(0, tk.END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def delete_item():
    selected_indices = listbox.curselection()
    for index in (selected_indices):
        task = listbox.get(index)
        listbox.delete(index)
    with open("tasks.txt", "r+") as filee:
        lines_from_to_do_task_file = filee.readlines()
        modified_lines = [line for line in lines_from_to_do_task_file  if task not in line]
    # Open the same file in write mode to overwrite its contents
    with open("tasks.txt", "w") as file:
        file.writelines(modified_lines)




def save_in_completed_file():
    complted_task=listbox2.get(0,tk.END)
    with open("compltedFile.txt","w") as myfile:
        for t in complted_task:
            myfile.write(t + "\n")


def listbox2_delete():
    selected_item=listbox2.curselection()
    for j in selected_item:
        tsk = listbox2.get(j)
        listbox2.delete(j)
    with open("compltedFile.txt","r+")as filee:
        lines_from_completed_task_file=filee.readlines()
        changedlines=[line for line in lines_from_completed_task_file if tsk not in line]
    with open("compltedFile.txt", "w") as filee:
        filee.writelines(changedlines)




def completed():
    task_completed=listbox.curselection()
    for i in task_completed:
        item=listbox.get(i)
        listbox2.insert(tk.END,item)
        listbox.delete(i)
        with open("tasks.txt","r+") as file:
            lines=file.readlines()
        changedlines=[line for line in lines if item not in line]


        with open("tasks.txt", "w") as file:
            file.writelines(changedlines)
    save_in_completed_file()



def edit_task():

    def update_task():
        item1=win_entry.get()
        listbox.delete(selected_item)
        listbox.insert(tk.END,item1)
        msgbox.showinfo("Task updated", "The task has been successfully updated in the list.")
    def go_back():
        win.destroy()
    win = customtkinter.CTk()
    win.title("Edit task")
    win.geometry("300x300")
    win_entry = customtkinter.CTkEntry(win, corner_radius=10, width=500, text_color="black")
    win_entry.pack()
    lbl = customtkinter.CTkButton(win, corner_radius=15,text="Go back",command=go_back)
    lbl.pack()
    try:
        selected_item = listbox.curselection()
        current_text = listbox.get(selected_item)
        win_entry.insert(0,current_text)
        win_button = customtkinter.CTkButton(win, corner_radius=15, hover=TRUE, command=update_task,text="Update task")
        win_button.pack()
    except:
        msgbox.showwarning("warning","first select a single item from the list")
    win.mainloop()

frame = customtkinter.CTkFrame(master=window,width=200,border_width=100, fg_color="grey",border_color="grey")
frame.pack(side="left",fill="y")  # Adjusted packing options
lb1 = customtkinter.CTkLabel(window, text="To do List",font=("bold",30),width=1200,height=80,corner_radius=0, fg_color="pink")
lb1.pack(side="top",fill="x")
button1 = customtkinter.CTkButton(frame,corner_radius=25,height=50, text="Add Task",command=add_item)
button1.place(x=20,y=40)
button2 = customtkinter.CTkButton(frame,corner_radius=25,height=50,hover=TRUE, text="Delete completed task",command=listbox2_delete)
button2.place(x=20,y=140)
button3 = customtkinter.CTkButton(frame,corner_radius=25,height=50, text="remove Tasks", command=delete_item)
button3.place(x=20,y=240)
button4= customtkinter.CTkButton(frame,corner_radius=25,height=50, text="Edit Task",command=edit_task)
button4.place(x=20,y=340)
button4= customtkinter.CTkButton(frame,corner_radius=25,height=50, text="Mark as Done",command=completed)
button4.place(x=20,y=440)


# Entry for adding items
entry = customtkinter.CTkEntry(window, corner_radius=10, width=500, text_color="black")
entry.pack(pady=10, fill="x")

# Create a frame to hold the labels
labels_frame = tk.Frame(window)
labels_frame.pack()

# Label for "To do tasks"
lbl_todo = customtkinter.CTkLabel(labels_frame, corner_radius=10, width=750, text_color="black", text="To do tasks", fg_color="grey")
lbl_todo.pack(side="left", anchor="w")

# Label for "Completed Tasks"
lbl = customtkinter.CTkLabel(labels_frame, corner_radius=10, width=590, text_color="black", text="Completed Tasks", fg_color="grey")
lbl.pack(side="left")

# Listbox for displaying items
listbox = tk.Listbox(window, selectmode=tk.SINGLE, width=80, height=32, bd=20, highlightcolor="grey", font="bold")
listbox.pack(side="left")

# Listbox for completed tasks
listbox2 = tk.Listbox(window, selectmode=tk.SINGLE, width=80, height=32, bd=20, highlightcolor="grey", font="bold")
listbox2.pack(side="right")

try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            listbox.insert(tk.END, task.strip())
    with open("compltedFile.txt", "r") as file:
        completed_tasks = file.readlines()
        for task in completed_tasks:
            listbox2.insert(tk.END, task.strip())
except FileNotFoundError:
    pass  # Ignore if the file doesn't exist yet



scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side="right", fill="y")

# Configure the listbox to use the scrollbar for vertical scrolling
listbox.config(yscrollcommand=scrollbar.set)


#entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry")
window.mainloop()