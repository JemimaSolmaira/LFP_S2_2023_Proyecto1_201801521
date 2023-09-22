class operadores:
    def __init__(self, nodo, lado , operacion, valor1, valor2, resultado):
        self._nodo = nodo
        self._lado = lado
        self._operacion = operacion
        self._valor1 = valor1
        self._valor2 = valor2
        self._resultado = resultado
        
    @property
    def nodo(self):
        return self._nodo
    
    @nodo.setter
    def nodo(self, nodo):
        self._nodo = nodo
        
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, lado):
        self._lado = lado
        
    @property
    def operacion(self):
        return self._operacion
    
    @operacion.setter
    def operacion(self, operacion):
        self._operacion = operacion
        
    @property
    def valor1(self):
        return self._valor1
    
    @valor1.setter
    def valor1(self, valor1):
        self._valor1 = valor1
        
    @property
    def valor2(self):
        return self._valor2
    
    @valor2.setter
    def valor2(self, valor2):
        self._valor2 = valor2
        
    @property
    def resultado(self):
        return self._resultado
    
    @resultado.setter
    def resultado(self, resultado):
        self._resultado = resultado
    