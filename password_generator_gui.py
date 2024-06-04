import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.letters_var = tk.BooleanVar(value=True)
        self.letters_check = tk.Checkbutton(root, text="Include Letters", variable=self.letters_var)
        self.letters_check.pack()

        self.numbers_var = tk.BooleanVar(value=True)
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.numbers_var)
        self.numbers_check.pack()

        self.symbols_var = tk.BooleanVar(value=True)
        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_entry = tk.Entry(root, width=50)
        self.password_entry.pack()

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_password)
        self.copy_button.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            use_letters = self.letters_var.get()
            use_numbers = self.numbers_var.get()
            use_symbols = self.symbols_var.get()

            password = generate_password(length, use_letters, use_numbers, use_symbols)
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid length")

    def copy_password(self):
        password = self.password_entry.get()
        if password:
            copy_to_clipboard(password)
        else:
            messagebox.showwarning("No Password", "Generate a password first")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
