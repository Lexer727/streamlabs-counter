import tkinter as tk
import keyboard
import os
import sys

def increment():
    with open('./counter.txt' , 'r+') as f:
        data = int(f.read())
        f.truncate(0)
        f.seek(0)
        data = str(data+1)
        label1.config(text=data)
        f.write(data)

def decrement():
    with open('./counter.txt' , 'r+') as f:
        data = int(f.read())
        f.truncate(0)
        f.seek(0)
        data = str(data-1)
        label1.config(text=data)
        f.write(data)

def set():
    try:
        data = str(int(user_input.get()))
        with open('./counter.txt' , 'w') as f:
            label1.config(text=data)
            f.write(data)
        entry1.delete(0, 'end')
    except:
        print("Wrong Type")
        button3.config(text="NUMBER PLS")
        root.after(1000, lambda: button3.config(text="Set Counter"))
        entry1.delete(0, 'end')

datafile = "app.ico"
if not hasattr(sys, "frozen"):
    datafile = os.path.join(os.path.dirname(__file__), datafile)
else:
    datafile = os.path.join(sys.prefix, datafile)



root = tk.Tk()
root.title("Counter")
root.iconbitmap(default=datafile)
root.minsize(260,130)
user_input = tk.StringVar(root)

#top Frame
topFrame = tk.Frame(root)
topFrame.pack(fill=tk.X, expand=True, pady=5, padx=5)

button1 = tk.Button(topFrame, width=3,  text="-", font="Arial 24 bold", command = decrement)
button2 = tk.Button(topFrame, width=3, text="+", font="Arial 24 bold", command = increment)
label1 = tk.Label(topFrame, font="Arial 24 bold")

topFrame.columnconfigure(0, weight=1)
topFrame.columnconfigure(1, weight=1)
topFrame.columnconfigure(2, weight=1)

button1.grid(row=0, column=0)
label1.grid(row=0, column=1)
button2.grid(row=0, column=2)

#bottom Frame
bottomFrame = tk.Frame(root)
bottomFrame.pack(expand=True, pady=5, padx=5)

entry1 = tk.Entry(bottomFrame, width=10, text="set", font="Arial 22 bold", textvariable=user_input)
entry1.bind(increment)
button3 = tk.Button(bottomFrame, width=10, padx=15, text="Set Counter", font="Arial 16 bold", command = set)

bottomFrame.columnconfigure(0, weight=1)
bottomFrame.columnconfigure(1, weight=1)

entry1.grid(row=0, column=0)
button3.grid(row=0, column=1)

try:
    with open('./counter.txt' , 'r') as f:
        data = f.read()
        label1.config(text=data)
except:
    with open('./counter.txt' , 'w+') as f:
        f.write("0")
        label1.config(text="0")

keyboard.add_hotkey('ctrl+shift+up', increment)
keyboard.add_hotkey('ctrl+shift+down', decrement)
root.mainloop()