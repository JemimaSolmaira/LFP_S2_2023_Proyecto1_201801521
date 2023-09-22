import os
from resultados import resultados

class Grafica:
    def __init__(self):
        
        self.nombre = ""
        self.fondo =    ""
        self.fuente =   ""
        self.forma =    ""
        self.concatenar = ""
        self.contador = 0
        self.operaciones = ""

    def configuraciones(self, nombre, fondo, fuente, forma):
        self.nombre = nombre
        self.fondo = fondo
        self.fuente = fuente
        self.forma = forma

    def encabezado(self):
        Encabezado = "digraph " + '"' + self.nombre + '"' + " { \n\n "
        Encabezado += "fontname=" + '"' +str(self.fuente) +'"'  + "\n\n"
        Encabezado += "node [fontname=" + '"'+str(self.fuente) +'"' + "]\n\n"
        Encabezado += "edge [fontname=" + '"'+str(self.fuente) +'"' + "]\n\n"
        Encabezado += "graph [newrank = true , nodesep = 0.8, overlap = true, splines = false]\n\n"
        Encabezado += "node [fixedsize = false, fontsize = 24, height = 2, shape = "+ '"'+ str(self.forma)+ '"' + ", style = " + '"' + "filled,setlinewidth(5)" + '"' + ", width = 2.2, shape = "+ '"'+ str(self.forma)+ '"' + ",color = " + '"' + "black" + '"' + " , fillcolor = " + '"' + str(self.fondo) + '"' + "]\n\n"
        Encabezado += "edge [ arrowsize = 0.5, weight = 2, style = " + '"' + "filled,setlinewidth(5)" + '"' + "row = func, arrowhead = 0.1,color = " + '"' + "black" + '"' + ", arrowhead = " + '"' + '"' + ", row = func ]\n\n"

        return Encabezado        
    

    def subgraph(self, flechas):
        string = "subgraph Operaciones {\n"
        string += self.operaciones + "\n"
        string += flechas + "\n"
        return string

    
    def datos(self, operacion, res, a , b):
        nodo = "No" + str(self.contador)
        string = nodo + " [label = " + '"' + str(operacion)+ "=" + str(res) + '"' + "]" + "\n"
        string += nodo + "a" + " [label = " + '"' + str(a) + '"' + "]" + "\n"
        string += nodo + "b" + " [label = " + '"' + str(b) + '"' + "]" + "\n"
        string += nodo + "->" + nodo + "a" + "\n"
        string += nodo + "->" + nodo + "b" + "\n"
        self.contador += 1
        return string
    
    def agregarOperaciones(self, operacion, res, a , b):
        self.operaciones += self.datos(operacion, res, a , b)
     
    def reiniciarOperaciones(self):
        self.operaciones = ""  
        
    def grupoColumnas(self, flechas):
        self.concatenar += self.subgraph(flechas) + "}" 
        
    def reiniciarColumna(self):
        self.Columnas = ""    
        
    
    def stringGeneral(self):
        string = self.encabezado() + self.concatenar + "}" 
        return string
    
    def crearArchivo(self):
        nombrearchivo = self.nombre + ".dot"
        archivo = open(nombrearchivo, "w")
        archivo.write(self.stringGeneral())
        archivo.close()
    
    def ConvertirArchivo(self):
        archivo = self.nombre + ".dot"
        imagen = self.nombre + ".svg"
        comando = "dot -Tsvg " + archivo + " > " + imagen
        os.system(comando)
        
        
        
if (__name__ == "__main__"):

    
    grupos = []
    grupos.append(resultados("Suma", "5", "4", "9"))
    grupos.append(resultados("Suma", "6", "6", "12"))
    grupos.append(resultados("Resto", "10", "7", "3"))

    
    graph = Grafica()
    
    graph.agregarOperaciones(grupos[0].operacion, grupos[0].resultado, grupos[0].a, grupos[0].b)
    graph.agregarOperaciones(grupos[1].operacion, grupos[1].resultado, grupos[1].a, grupos[1].b)
    graph.agregarOperaciones(grupos[2].operacion, grupos[2].resultado, grupos[2].a, grupos[2].b)
    
    
    string = "No0a -> No1" + "\n" + "No1b -> No2"
    

    graph.grupoColumnas(string)
    
    graph.crearArchivo()
    graph.ConvertirArchivo()