import json
from tkinter import filedialog
from lectura import Scanner

# Abre el archivo JSON
#with open("ejemplo.json", "r") as archivo:
    # Lee el contenido del archivo y carga los datos JSON en un diccionario
    #datos = json.load(archivo)

# Muestra el contenido en la consola
#print("Nombre:", datos["nombre"])
#print("Edad:", datos["edad"])
#print("Ciudad:", datos["ciudad"])
#print("Hobbies:", ", ".join(datos["hobbies"]))
#print("Contacto:")
#print("   Email:", datos["contacto"]["email"])
#print("   Teléfono:", datos["contacto"]["telefono"])

leer = Scanner()


contenido = ""
archivo = "ejemplo" + ".json"
if archivo:
    with open(archivo, 'r') as file:
        contenido = file.read()
        
  
leer.Analizar(contenido)
leer.mostrarResultados()

#leer.eliminarSignos()
#leer.Arbol()


#leer.get_instruccion()
#leer.get_instruccion()
#leer.get_instruccion()
leer.AnalisisTabla()
print("Tabla de Simbolos")
leer.mostrarResultados()
#leer.mostrarResultados()
leer.crearModificado()
leer.mostrarResultados()





