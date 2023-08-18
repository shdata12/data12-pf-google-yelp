import tkinter as tk
import re
import pyperclip

def convert_drive_link(input_link):
    match = re.search(r'/file/d/([^/]+)', input_link)
    if match:
        file_id = match.group(1)
        new_link = f'https://drive.google.com/open?id={file_id}'
        return new_link
    else:
        return "Enlace de Google Drive no válido"

def copy_to_clipboard(link):
    pyperclip.copy(link)

def show_popup():
    popup = tk.Toplevel()
    popup.title("Convertir Enlace de Google Drive")

    label = tk.Label(popup, text="Ingresa el enlace de Google Drive:")
    label.pack()

    entry = tk.Entry(popup)
    entry.pack()

    def convert_and_copy():
        input_link = entry.get()
        output_link = convert_drive_link(input_link)
        copy_to_clipboard(output_link)
        result_label.config(text="Enlace convertido y copiado al portapapeles.")

    convert_button = tk.Button(popup, text="Convertir y Copiar", command=convert_and_copy)
    convert_button.pack()

    result_label = tk.Label(popup, text="")
    result_label.pack()

def main():
    root = tk.Tk()
    root.title("Ventana Principal")

    open_popup_button = tk.Button(root, text="Ingresar Enlace de Google Drive", command=show_popup)
    open_popup_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

