import tkinter as tk
from tkinter import filedialog, messagebox
import encryption

def process_file(action):
    if not selected_file.get():
        messagebox.showerror("Error", "Please select a file.")
        return
    
    if not algorithm.get():
        messagebox.showerror("Error", "Please select an algorithm.")
        return
    
    input_file = selected_file.get()
    output_file = "output.enc" if action == "encrypt" else "output.dec"
    
    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    iv = "abcdef9876543210abcdef9876543210"

    alg = algorithm.get().lower()
    
    if action == "encrypt":
        encryption.encrypt_file(input_file, output_file, alg, key, iv)
        messagebox.showinfo("Success", f"File has been encrypted using {algorithm.get()}!")
    else:
        encryption.decrypt_file(input_file, output_file, alg, key, iv)
        messagebox.showinfo("Success", f"File has been decrypted using {algorithm.get()}!")

root = tk.Tk()
root.title("File Encryption/Decryption")

selected_file = tk.StringVar(root)
tk.Label(root, text="Selected File:").grid(row=0, column=0, sticky='w')
tk.Entry(root, textvariable=selected_file, state='readonly', width=50).grid(row=0, column=1)
tk.Button(root, text="Select File", command=lambda: select_file()).grid(row=0, column=2)

algorithm = tk.StringVar(root)
tk.Label(root, text="Algorithm:").grid(row=1, column=0, sticky='w')
algorithm_options = ['AES-256-CBC']
algorithm_menu = tk.OptionMenu(root, algorithm, *algorithm_options)
algorithm_menu.grid(row=1, column=1, sticky='w')

tk.Button(root, text="Encrypt", command=lambda: process_file("encrypt")).grid(row=2, column=0, sticky='w')
tk.Button(root, text="Decrypt", command=lambda: process_file("decrypt")).grid(row=2, column=1, sticky='w')

def select_file():
    filename = filedialog.askopenfilename()
    if filename:
        selected_file.set(filename)

root.mainloop()
