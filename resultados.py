class resultados:
    def __init__(self, operacion, a, b, res):

        self._operacion = operacion
        self._a = a
        self._b = b
        self._resultado = res
        

    @property
    def operacion(self):
        return self._operacion
    
    @operacion.setter
    def operacion(self, operacion):
        self._operacion = operacion
        
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, a):
        self._a = a
        
    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, b):
        self._b = b
        
    @property
    def resultado(self):
        return self._resultado
    
    @resultado.setter
    def resultado(self, resultado):
        self._resultado = resultado
        