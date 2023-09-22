class inf:
    def __init__(self, token, lexema , fila, columna):
        self._token = token
        self._lexema = lexema
        self._fila = fila
        self._columna = columna
        
    @property
    def token(self):
        return self._token
    
    @property
    def lexema(self):
        return self._lexema
    
    @property
    def fila(self):
        return self._fila
    
    @property
    def columna(self):
        return self._columna
    
    
    
    @token.setter
    def token(self, token):
        self._token = token
        
    @lexema.setter
    def lexema(self, lexema):
        self._lexema = lexema
        
    @fila.setter
    def fila(self, fila):
        self._fila = fila
        
    @columna.setter
    def columna(self, columna):
        self._columna = columna
        