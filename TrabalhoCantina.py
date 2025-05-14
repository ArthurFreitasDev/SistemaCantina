import tkinter as tk
import os
root = tk.Tk()
root.title("Teste")
root.resizable(width=False, height=False)
root.geometry("500x500")

def button_click():
    print("Button Click!")

labelframe1 = tk.LabelFrame(root, text="LabelFrame")
labelframe1.pack()

label1 = tk.Label(labelframe1, text="TESTETESTETESTE")
label1.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(labelframe1, width=50)
entry.grid(row=0, column=1, padx=10)




root.mainloop()