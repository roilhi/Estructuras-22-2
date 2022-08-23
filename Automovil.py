class Automovil:
    """
    Clase que define el estado y comportamiento de 
    un automóvil
    """
    ruedas = 4 #Atributo de instancia

    def __init__(self,color, aceleracion): #Constructur
        self.color = color # Atributos de clase
        self.aceleracion = aceleracion
        self.velocidad = 0
    def acelera(self): # Métodos
        self.velocidad = self.velocidad + self.aceleracion
    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v
## Clase que hereda los atributos de automovil
class AutoVolador(Automovil):
    ruedas = 6
    def __init__(self, color, aceleracion, esta_volando=False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando
    def vuela(self):
        self.esta_volando = True
    def atteriza(self):
        self.esta_volando = False
    
    
