import math

class Punto:
    #costruttore con i punti voluti
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #metodo per muovere il punto
    def muovi(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    #metodo che calcola la distanza con pitagora
    def distanza_da_origine(self):
        distanza = math.sqrt(self.x**2 + self.y**2)
        return print(f"Il punto dista {distanza} dall'origine")

#creo un punto
mio_punto = Punto(5,3)

#muovo il punto
mio_punto.muovi(1,1)
mio_punto.muovi(3,-5)

#calcolo e stampo la distanza
mio_punto.distanza_da_origine()