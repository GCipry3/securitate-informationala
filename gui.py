import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import secrets
import base64
import pyperclip  # To handle clipboard operations

import encryption

def generate_key():
    # Generate a 32-byte random key and display it base64 encoded
    random_key = secrets.token_bytes(32)  # 256-bit key for AES-256-CBC
    encoded_key = base64.b64encode(random_key).decode('utf-8')
    key_text.set(encoded_key)

def copy_key_to_clipboard():
    # Copy the current key in the entry to the clipboard
    pyperclip.copy(key_text.get())
    messagebox.showinfo("Copied", "Key copied to clipboard!")

def process_file(action):
    if not selected_file.get():
        messagebox.showerror("Error", "Please select a file.")
        return
    
    if not algorithm.get():
        messagebox.showerror("Error", "Please select an algorithm.")
        return

    if not key_text.get():
        messagebox.showerror("Error", "No encryption key provided.")
        return

    input_file = selected_file.get()
    output_file = "output.enc" if action == "encrypt" else "output.dec"
    alg = algorithm.get().lower()
    
    key = base64.b64decode(key_text.get().encode('utf-8'))  # Decode the key from base64
    
    if 'aes' in alg:
        iv = secrets.token_hex(16)  # 16 bytes IV for AES, generated for each encryption
        if action == "encrypt":
            encryption.encrypt_file(input_file, output_file, alg, key.hex(), iv)
        else:
            encryption.decrypt_file(input_file, output_file, alg, key.hex(), iv)
        # Store the encryption details in database (not shown here, assuming a function exists)
    elif 'rsa' in alg:
        if action == "encrypt":
            key_path = filedialog.askopenfilename(title="Select Public Key File")
            encryption.encrypt_file(input_file, output_file, alg, key_path, None)
        else:
            key_path = filedialog.askopenfilename(title="Select Private Key File")
            encryption.decrypt_file(input_file, output_file, alg, key_path)

    messagebox.showinfo("Success", f"File has been {'encrypted' if action == 'encrypt' else 'decrypted'} using {algorithm.get()}!")

root = tk.Tk()
root.title("File Encryption/Decryption")

selected_file = tk.StringVar(root)
tk.Label(root, text="Selected File:").grid(row=0, column=0, sticky='w')
tk.Entry(root, textvariable=selected_file, state='readonly', width=50).grid(row=0, column=1)
tk.Button(root, text="Select File", command=lambda: select_file()).grid(row=0, column=2)

algorithm = tk.StringVar(root)
tk.Label(root, text="Algorithm:").grid(row=1, column=0, sticky='w')
algorithm_options = ['AES-256-CBC', 'RSA']
algorithm_menu = tk.OptionMenu(root, algorithm, *algorithm_options)
algorithm_menu.grid(row=1, column=1, sticky='w')

key_text = tk.StringVar(root)
tk.Label(root, text="Encryption Key:").grid(row=2, column=0, sticky='w')
key_entry = tk.Entry(root, textvariable=key_text, state='readonly', width=50)
key_entry.grid(row=2, column=1)
tk.Button(root, text="Generate Key", command=generate_key).grid(row=2, column=2)
tk.Button(root, text="Copy Key", command=copy_key_to_clipboard).grid(row=2, column=3)

tk.Button(root, text="Encrypt", command=lambda: process_file("encrypt")).grid(row=3, column=0, sticky='w')
tk.Button(root, text="Decrypt", command=lambda: process_file("decrypt")).grid(row=3, column=1, sticky='w')

def select_file():
    filename = filedialog.askopenfilename()
    if filename:
        selected_file.set(filename)

root.mainloop()
