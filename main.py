import tkinter as tk
from tkinter import messagebox
import subprocess

# 🎨 Paleta de colores
BG = "#0f172a"
FG = "#e2e8f0"
ENTRY_BG = "#1e293b"
BTN_BG = "#2563eb"
BTN_FG = "#ffffff"
BTN_HOVER = "#3b82f6"

FONT_LABEL = ("Segoe UI", 12, "bold")
FONT_ENTRY = ("Segoe UI", 12)
FONT_BTN = ("Segoe UI", 11, "bold")

def run_command(args):
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip() if e.stderr else "Error al ejecutar."

def create_action():
    name = name_var.get().strip()
    number = number_var.get().strip()
    if name and number:
        output = run_command(["python3", "create_contact.py", name, number])
        messagebox.showinfo("Crear", output)
    else:
        messagebox.showwarning("Faltan datos", "Nombre y número son obligatorios.")

def read_action():
    output = run_command(["python3", "read_contacts.py"])
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

def update_action():
    name = name_var.get().strip()
    number = number_var.get().strip()
    if name and number:
        output = run_command(["python3", "update_contact.py", name, number])
        messagebox.showinfo("Actualizar", output)
    else:
        messagebox.showwarning("Faltan datos", "Nombre y nuevo número requeridos.")

def delete_action():
    name = name_var.get().strip()
    if name:
        output = run_command(["python3", "delete_contact.py", name])
        messagebox.showinfo("Eliminar", output)
    else:
        messagebox.showwarning("Faltan datos", "Nombre requerido.")

def create_button(parent, text, command):
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        bg=BTN_BG,
        fg=BTN_FG,
        activebackground=BTN_HOVER,
        activeforeground=BTN_FG,
        relief="flat",
        font=FONT_BTN,
        height=2,
        width=10
    )
    btn.pack(side="left", expand=True, fill="x", padx=5)
    return btn

# 🖼️ Ventana principal
root = tk.Tk()
root.title("Gestor de Contactos")
root.geometry("540x620")
root.configure(bg=BG)

# Campo nombre
tk.Label(root, text="Nombre", bg=BG, fg=FG, font=FONT_LABEL).pack(pady=(20, 0))
name_var = tk.StringVar()
entry_name = tk.Entry(root, textvariable=name_var, bg=ENTRY_BG, fg=FG, insertbackground=FG,
                      relief="flat", font=FONT_ENTRY, highlightthickness=1)
entry_name.pack(pady=6, padx=20, ipady=8, fill="x")

# Campo número
tk.Label(root, text="Número", bg=BG, fg=FG, font=FONT_LABEL).pack()
number_var = tk.StringVar()
entry_number = tk.Entry(root, textvariable=number_var, bg=ENTRY_BG, fg=FG, insertbackground=FG,
                        relief="flat", font=FONT_ENTRY, highlightthickness=1)
entry_number.pack(pady=6, padx=20, ipady=8, fill="x")

# Botones CRUD
btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=15, padx=20, fill="x")

create_button(btn_frame, "Crear", create_action)
create_button(btn_frame, "Leer", read_action)
create_button(btn_frame, "Actualizar", update_action)
create_button(btn_frame, "Eliminar", delete_action)

# Resultado
tk.Label(root, text="Contactos", bg=BG, fg=FG, font=("Segoe UI", 13, "bold")).pack(pady=(10, 5))
output_text = tk.Text(root, height=18, bg=ENTRY_BG, fg=FG, insertbackground=FG,
                      relief="flat", wrap="word", font=("Segoe UI", 11))
output_text.pack(padx=20, pady=(0, 20), fill="both", expand=True)

root.mainloop()
