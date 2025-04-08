#esempio base
class Esempio():
    x = 10

#creazione oggetto base
oggetto_1 = Esempio()
oggetto_2 = Esempio()

#modifica attributo
oggetto_1.x = 20
oggetto_2.x = 50

print(oggetto_1.x)
print(oggetto_2.x)

class Penna():
    altezza = 0
    larghezza = 0

    #metodo costruttore: self rappresenta l'oggetto stesso
    def __init__(self, h, l):
        self.altezza = h
        self.larghezza = l
    
oggetto_penna = Penna(10, 40)

print(oggetto_penna.altezza)
print(oggetto_penna.larghezza)

non_lo_so = Penna(5, 6)


