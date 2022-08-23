class Perro:
    def sonido(self):
        print('Ladrido')

class Gato:
    def sonido(self):
        print('Maullido')

class Vaca:
    def sonido(self):
        print('Mugido')

def a_cantar(animales):
    for animal in animales:
        animal.sonido()
if __name__=='__main__':
    perro = Perro()
    gato = Gato()
    gato_2 = Gato()
    vaca = Vaca()
    perro_2 = Perro()
    granja = [perro, gato, vaca,gato_2,perro_2]
    a_cantar(granja)
