#dichiaro la classe
class Automobile:
    #attributo di classe
    numero_di_ruote = 4
    #costruttore
    def __init__(self, marca, modello):
        #attributi di istanza
        self.marca = marca
        self.modello = modello
    #metodo di istanza
    def stampa_info(self):
        print("L'automobile e' una", self.marca, self.modello)

#istanzio la classe
macchinina = Automobile("Ford", "Puma")

#metodo di istanza sulla macchinina
macchinina.stampa_info()


#esempio metodo statico
class Calcolatrice:

    #decoratore definito in python
    @staticmethod
    def somma(a, b):
        return a + b

#uso il metodo senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)


#esempio metodo decorato di classe
class Contatore:
    numero_istanze = 0
    def __init__(self):
        Contatore.numero_istanze += 1
    
    @classmethod
    def mostra_numero_istanze(cls):
        #altro modo di richiamare le variabili nel print
        print(f"Sono state create {cls.numero_istanze} istanze.")

c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()