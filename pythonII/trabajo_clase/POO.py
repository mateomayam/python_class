class animal():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def haz_ruido(self):
        print ("AAAAAAAAAAAAAH")

class perro(animal):

    def haz_ruido(self):
        print ("guau")

class gato(animal):
    usa_arenero = True
    def haz_ruido(self):
        print ("miau")

animal.haz_ruido(animal)
perro.haz_ruido(perro)
gato.haz_ruido(gato)