# Tema L24 Python
# 2. Implementati o clasa InstrumentDeScris care are metodele “foloseste” si “folosireRamasa”.
# Fiecare instrument de scris primeste in constructor un numar care reprezinta folosirea ramasa
# initiala si fiecare apel “foloseste” scade acest numar cu 1. Metoda “folosireRamasa” returneaza
# numarul ce reprezinta folosirea ramasa.
# Implementati o clasa Creion care mosteneste InstrumentDeScris si are in plus metoda “ascute”
# care scate numarul de folosiri cu 5.

class InstrumentDeScris:
    def __init__(self, folosire_ramasa):
        self.folosire_ramasa = folosire_ramasa

    def foloseste(self):
        self.folosire_ramasa -= 1

    def folosireRamasa(self):
        return self.folosire_ramasa

class Creion(InstrumentDeScris):
    def ascute(self):
        self.folosire_ramasa -= 5

instrument = InstrumentDeScris(10)
instrument.foloseste()
print(instrument.folosireRamasa())  

creion = Creion(20)
creion.ascute()
creion.foloseste()
print(creion.folosireRamasa())  
