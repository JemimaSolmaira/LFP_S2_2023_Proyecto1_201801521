from operaciones import operaciones
class Math:
    def __init__(self):
        self.operciones = operaciones()

    def operar(self, operacion, a, b):
        if operacion == "suma":
            resultado = self.operciones.suma(a, b)
        elif operacion == "resta":
            resultado = self.operciones.resta(a, b)
        elif operacion == "multiplicacion":
            resultado = self.operciones.multiplicacion(a, b)
        elif operacion == "division":
            resultado = self.operciones.division(a, b)
        elif operacion == "potencia":
            resultado = self.operciones.potencia(a, b)
        elif operacion == "raiz":
            resultado = self.operciones.raiz(a, b)
        elif operacion == "inverso":
            resultado = self.operciones.inverso(a)
        elif operacion == "seno":
            resultado = self.operciones.seno(a)
        elif operacion == "coseno":
            resultado = self.operciones.coseno(a)
        elif operacion == "tangente":
            resultado = self.operciones.tangente(a)
        elif operacion == "modulo":
            resultado = self.operciones.modulo(a, b)
            
        return resultado
        