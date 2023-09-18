# Tema L24 Python
# 1. Implementati o clasa Punct care contine coordonatele x si y (x orizontala, y verticala).
# Coordonatele se vor transmite prin constructor. Implementati o metoda “maiSus” care verifica
# daca un punct primit ca parametru este mai sus (y mai mare) decat punctul pe care se apeleaza
# si returneaza true sau false. Exemplu de apel: p1.maiSus(p2)


class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def maiSus(self, punct):
        if punct.y > self.y:
            return True
        else:
            return False
p1 = Punct(3, 5)
p2 = Punct(2, 8)

print(p1.maiSus(p2))  