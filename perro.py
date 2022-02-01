class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("Guau, Guau")
            
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)

class PerroAsistencia(Perro):
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.trabajando = False
        
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}, amo: {}".format(self.nombre, self.edad, self.peso,self.amo)
    
    def pasear(self):
        print("Soy {}, ayudo a mi dueño, {}, a pasear".format(self.nombre,self.amo))
    
    def ladrar(self):
        if self.trabajando:
            print("Shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabaja(self):
        self.trabajando = True
        
    def descansa(self):
        self.trabajando = False

class Dog(): #Se puede crear sin asignar atributos y despues otorgar valores a cada atributo
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
        else:
            print("Guau, Guau")

salchicho = Perro("Salchicho", 3, 12)
lola = Perro("Lola", 8, 1.5)
miko = Perro("Miko", 8, 3)
rantanplan = PerroAsistencia("Ran Tan Plan", 4, 8, "Lucky Luke")