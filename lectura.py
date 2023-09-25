from operadores import operadores
from errores import errores
from inf import inf  
from Math import Math
from operadores import operadores
from graphiz import Grafica
import json

class Scanner:
    def __init__(self):
        self.matematica = Math()
        self.nodo = 0
        self.tokens = []
        self.errores = []
        self.operar = []
        self.resultados = []
        self.configuracion = []
        self.tokens2 = []
     
    def analisis (self, contenido):
        self.Analizar(contenido)
        self.eliminarSignos()
        self.AnalisisTabla()
        self.Ndatos()

    def mErrores(self, nombreArchivo):
        self.crearErrores(nombreArchivo)
    
    
    #Transformacion de la cadena de texto a tokens, y se agregan los primeros errores
    #Se agregan los tokens a la lista de tokens
    def Analizar(self, dato):
        line = 1
        col = 1
        i = 0
        while i < len(dato):
            char = dato[i]
            if char.isspace():
                if char == "\n":
                    line += 1
                    col = 1
                elif char == "\t":
                    col += 4
                else:
                    col += 1
                i += 1
            elif char == '"':
                string, pos = self.textos(dato[i + 1 :], i)
                col += len(string) + 1
                i = pos + 2
                token = inf(string,"string", line, col)
                self.tokens.append(token)
            elif char in ["{", "}", "[", "]", ",", ":"]:
                col += 1
                i += 1
                token = inf(char,"simbolo", line, col)
                self.tokens.append(token)
            elif char.isdigit():
                number, pos = self.numeros(dato[i:], i)
                col += pos - i
                i = pos
                token = inf(number, "numero", line, col)
                self.tokens.append(token)
            else:
                
                self.agregarError(char, "Error lexico: caracter desconocido", line, col)
                
                print(
                    "Error: caracter desconocido:",
                    char,
                    "en linea:",
                    line + 1,
                    "columna:",
                    col + 1,
                )
                i += 1
                col += 1
    

    #token para los textos
    def textos(self,dato, i):
        token = ""
        for char in dato:
            if char == '"':
                return [token, i]
            token += char
            i += 1
        print("Error: string no cerrado")


    # token para los numeros
    def numeros(self, dato, i):
        token = ""
        isDecimal = False
        for char in dato:
            if char.isdigit():
                token += char
                i += 1
            elif char == "." and not isDecimal:
                token += char
                i += 1
                isDecimal = True
            else:
                break
        if isDecimal:
            return [float(token), i]
        return [int(token), i]

    
    #limpiar signos en la tabla de tokens
    def eliminarSignos(self):
        for i in self.tokens:
            if i.token == "," or i.token == ":" :
                self.tokens.remove(i)
                  
                       
    #obtener datos de la lista de tokens a la lista de resultados
    def get_instruccion(self):
        operacion = None
        value1 = None
        value2 = None
        resultado = None
        i=0
        self.nodo += 1
        lado = ""
        
        while True:
            
            
            if len(self.tokens) == 0:
                break
            
            token = self.tokens.pop(0)

            if token.token == "operacion":
                operacion = self.tokens.pop(0).token
            elif token.token == "valor1":
                value1 = self.tokens.pop(0).token
                if value1 == "[":
                    value1 = self.get_instruccion()
                    lado = "a"
            elif token.token == "valor2":
                value2 = self.tokens.pop(0).token

                if value2 == "[":
                    value2 = self.get_instruccion()  
                    lado = "b" 
            elif token.token in ["texto", "fondo", "fuente", "forma"]:
                config = self.tokens.pop(0).token
                self.configuracion.append(config)

            else:
                pass

           
            if operacion and value1 and value2:
                resultado = self.matematica.operar(operacion, value1, value2)
                self.resultados.append(operadores(self.nodo, lado , operacion, value1, value2, resultado))
                return resultado
            
            if operacion and operacion in ["seno", "coseno", "tangente", "inverso"] and value1:
                resultado = self.matematica.operar(operacion, value1, 0)
                self.resultados.append(operadores(self.nodo, lado ,  operacion, value1, 0, resultado))
                
                return resultado

    
        return None
  
    def mostrarResultados(self):
        print(str(len(self.tokens)) + "tokens")
        for i in self.tokens:
            print(str(i.token))

                
    
    #crear el grafo
    def Arbol(self):
        
        i = 1

        
        arbol = Grafica()
        j = 0
        string = ""
        k = 0
        while self.tokens:
            
            self.get_instruccion()
            
            for i in self.resultados:
                print(i.operacion + " " + str(i.valor1) + " " + str(i.valor2) + " " + str(i.resultado))
                
            print("-------------------")
            
            arbol.reiniciarOperaciones()
            
            for i in self.resultados:
                
                arbol.agregarOperaciones(i.operacion, i.resultado, i.valor1, i.valor2)
            
            
            
            tam = len(self.resultados)-1 
            print("tam: " + str(tam))
            k = 1  
            while tam > 0:
                lado = self.resultados[tam].lado 
                print("lado: " + lado)
                if lado == "a":
                    string += "No" + str(j+tam) + "a" + " -> " + "No" + str(j+tam-1) + "\n"
                elif lado == "b":
                    string +=  "No" + str(j+tam) + "b" + " -> " + "No" + str(j+tam-1) + "\n"
                 
                    
                tam -= 1
            
            j += len(self.resultados)
            
            
            arbol.grupoColumnas(string)        
            self.resultados.clear()
            
            string = ""
            
            
        arbol.configuraciones("Nodo1", self.configuracion[1], self.configuracion[2], self.configuracion[3])
        arbol.crearArchivo()
        arbol.ConvertirArchivo()
        
        
    #Buscar y corregir errores en la tabla de tokens
    def AnalisisTabla(self):
        
        i = 1
        while i < len(self.tokens):
            token = self.tokens[i].token
            lexema = self.tokens[i].lexema
            reservadas = ["texto", "fondo", "fuente", "forma"]


            if lexema == "string":
                if self.tokens[i-2].token in reservadas:
                    print(str(self.tokens[i-2].token) + " " + str(self.tokens[i-1].token) + " " + str(self.tokens[i].token))
                    print("correcto")
                else:
                    parametros = self.revString(token)
                    
                    if parametros[0] != "":
                        self.agregarError(parametros[0], "Error lexico", self.tokens[i].fila, self.tokens[i].columna)
                        self.tokens[i].token = parametros[1]
            i += 1
                    
                                  
    #Revision de strings            
    def revString(self, strin):
        palabras = ["operaciones", "operacion", "valor1", "valor2","suma", "resta", "multiplicacion", "division", "potencia", "modulo", "coseno" ,"seno", "tangente", "raiz" , "texto", "fondo", "fuente", "forma"]
        string = strin.lower()
        error = ""
        palabra = ""
        for i in palabras:

            j = 0
            k = 0
            while j < len(i) and k < len(string):
                if i[j] == string[k]:
                    palabra += string[k]
                    j += 1
                    k += 1
                    
                else:
                    error = string[k]
                    k += 1
                    
            
            if palabra == i:
                    break
            else:
                palabra = ""
                error = ""

        return error, palabra        
            
     
    #nuevo archivo        
    def Ndatos(self):
        
        operaciones = {}
        ndatos = []
        while self.tokens:
            self.get_instruccion()
            
            
            for i in self.resultados:
                print(i.operacion + " " + str(i.valor1) + " " + str(i.valor2) + " " + str(i.resultado))
                
            print("-------------------")   
            tam = len(self.resultados)-1
            
            if tam >= 0:
                ndatos.append(self.diccionario(tam)) 
            
            
            self.resultados.clear()
            
        operaciones["operaciones"] = ndatos   
        operaciones["configuracion"] = self.config()
        
        
         
        with open("operaciones.json", "w") as file:
            json.dump(operaciones, file, indent=4)
            print("Archivo Creado")
            
            
    def config (self):
        con = []
        config = {}
        
        config ["texto"] = self.configuracion[0]
        config ["fondo"] = self.configuracion[1]
        config ["fuente"] = self.configuracion[2]
        config ["forma"] = self.configuracion[3]
        
        con.append(config)
        
        return con
                   
                
                
    def diccionario(self, i):
        ndatos = []
        dato = self.resultados[i]
        

        diccionario = {}
        diccionario["operacion"] = dato.operacion
        if dato.lado == "a": 
            ndatos.append(self.diccionario(i-1))
            diccionario["valor1"] = ndatos
        else:
            diccionario["valor1"] = dato.valor1
            
        if dato.lado == "b":
            ndatos.append(self.diccionario(i-1))
            diccionario["valor2"] = ndatos    
        else:
            diccionario["valor2"] = dato.valor2
        
            
        return diccionario                   
            
   
        
        

    def Caracteres(self, token):
        llaves = ["{", "}"]
        corchetes = ["[", "]"]
        Dospuntos = [":"]
        alfabeto = ['"', "s", "u", "m", "a", "r", "e", "t", "i", "p", "l", "c", "o", "n", "d", "v", "x", "o", "g", "p", "c", "e", "i", "o", "n", "l", "r", "z", "s", "n"]
        numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        coma = [","]    
        tipo = ""
        if token in llaves:   
            tipo = "llave"
        elif token in corchetes:
            tipo = "corchete"
        elif token in Dospuntos:
            tipo = "dosPuntos"
        elif token in alfabeto:
            tipo = "alfabeto"
        elif token in numeros:
            tipo = "numero"
        elif token in coma:
            tipo = "coma"

        return tipo
        
                
    
            
    def crearErrores(self, nombreArchivo):

        diccionario = { }
        i = 0
        agregar = []
        
        while i < len(self.errores):
            err = {}
            err["No" ] = i + 1
            err["descripcion"] = {"lexema": self.errores[i].tipo, "tipo": self.errores[i].descripcion, "fila": self.errores[i].linea, "columna": self.errores[i].columna}
            agregar.append(err)
            i += 1
        
        diccionario ["errores"] = agregar
        
        nombre = nombreArchivo + ".json"
        
        
        with open(nombre, "w") as file:
            json.dump(diccionario, file, indent=4)
            print("Archivo Creado")

        
    def agregarError(self, lexema, tipo, fila, columna):
        self.errores.append(errores(lexema, tipo, fila, columna))
        print("error agregado:" + lexema + " " + tipo + " " + str(fila) + " " + str(columna))
        

    
    def verErrroes(self):
        for i in self.errores:
            print(i.lexema + " " + i.tipo + " " + str(i.fila) + " " + str(i.columna))