from os import path
import json

class ArchivosJson:
    def __init__(self, Archivo, nombreArchivo):
        self._Archivo = []
        self._Archivo = Archivo
        self._nombreArchivo = nombreArchivo
        


    def crearArchivo(self):
        with open(self._nombreArchivo + ".json", "w") as file:
            json.dump(self._Archivo, file, indent=4)
            print("Archivo Creado")