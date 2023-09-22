import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from lectura import Scanner

archivoGlobal = ""

def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.json")])
    archivoGlobal = archivo
    if archivo:
        with open(archivo, 'r') as file:
            contenido.delete(1.0, tk.END)
            contenido.insert(tk.END, file.read())

def guardar_archivo():
    archivo = archivoGlobal+".json"
    if archivo:
        with open(archivo, 'w') as file:
            file.write(contenido.get(1.0, tk.END))

def guardar_como():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, 'w') as file:
            file.write(contenido.get(1.0, tk.END))
            
def analizarclick():
    messagebox.showinfo("Analisis", "Analisis realizado con exito")
    
def erroresclick():
    messagebox.showinfo("Errores", "No se encontraron errores")
    
def reportesclick():
    archivo = "reportes" + ".json"
    if archivo:
        with open(archivo, 'w') as file:
            file.write(contenido.get(1.0, tk.END))
    
    cont = ""
    archivo = "reportes" + ".json"
    if archivo:
        with open(archivo, 'r') as file:
            cont = file.read()
            
    leer = Scanner()
    leer.Analizar(cont)
    leer.eliminarSignos()
    leer.Arbol()
    
    

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.title("Analisis Lexico Archivos JSON")

menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

archivo_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_command(label="Guardar como", command=guardar_como)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)

contenido = tk.Text(ventana)
contenido.pack(expand=True, fill="both", padx=15, pady=15)

boton_reportes = tk.Button(ventana, text="Reportes", command=reportesclick, width=10)
boton_reportes.pack(padx=10, pady=10, side="right")

boton_errores = tk.Button(ventana, text="Errores", command=erroresclick, width=10)
boton_errores.pack(padx=10, pady=10, side="right")

boton_analizar = tk.Button(ventana, text="Analizar", command=analizarclick, width=10)
boton_analizar.pack(padx= 10, pady=10, side="right")

ventana.mainloop()
