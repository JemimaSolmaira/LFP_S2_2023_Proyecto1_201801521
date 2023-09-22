class errores:
    def __init__(self, tipo, descripcion, linea, columna):
        self._tipo = tipo
        self._descripcion = descripcion
        self._linea = linea
        self._columna = columna
        
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def linea(self):
        return self._linea
    
    @property
    def columna(self):
        return self._columna
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
        
    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion
        
    @linea.setter
    def linea(self, linea):
        self._linea = linea
        
    @columna.setter
    def columna(self, columna):
        self._columna = columna
        
    def __str__(self):
        return "Tipo: " + self._tipo + " Descripcion: " + self._descripcion + " Linea: " + str(self._linea) + " Columna: " + str(self._columna) 
    