import math

class operaciones:
    def __init__(self):
        self.lista = []
        
    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        return a / b
    
    def potencia(self, a, b):
        return a ** b
    
    def raiz(self, a, b):
        return a ** (1/b)
    
    def inverso(self, a):
        return 1/a
    
    def seno(self, a):
        return math.sin(a)
    
    def coseno(self, a):
        return math.cos(a)
    
    def tangente(self, a):
        return math.tan(a)
    
    def modulo(self, a, b):
        return a % b    