from Automovil import *

c1 = Automovil('rojo', 20)

print(c1.color)

print(c1.ruedas)
print(c1.velocidad)
c1.acelera()
print(c1.velocidad)
c2 = Automovil('azul',30)
print(c2.color)
print(c2.ruedas)
c2.acelera()
#c2.frena()
print(c2.velocidad)

