class StaticArray:
    def __init__(self,n):
        self.data = [None] * n
    def get_at(self,i):
        if not (0 <=i < len(self.data)): raise IndexError
        return self.data[i]
    def set_at(self, i, x):
        if not(0 <= i < len(self.data)): raise IndexError
        self.data[i] = x

def mismo_cumple(estudiantes):
    """
    Encuentra a un par de estudiantes con la misma fecha
    de cumpleaños.
    Entrada: Tupla (nombre,cumple)
    Salida: Tupla con nombres de estudiantes o none
    """
    n = len(estudiantes)
    record = StaticArray(n)
    for k in range(n):
        (nombre1,cumple1) = estudiantes[k]
        for i in range(k):
            (nombre2,cumple2) = record.get_at(i)
            if cumple1 == cumple2:
                return (nombre1,nombre2)
        record.set_at(k, (nombre1,cumple1))
    return None 

todos = (('Alex','23-05'),('Juan','02-03'),('Paty','23-05'))

y = mismo_cumple(todos)
print(y)

