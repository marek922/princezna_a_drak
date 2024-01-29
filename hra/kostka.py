
class Kostka:
    def __init__(self, pocet_stran=6):  #Definuje počet stěň, lze (změnit)
        self._pocet_stran = pocet_stran

    def hod (self):  # Reprezentuje hod kostkou
        import random as _random
        return _random.randint(1,self._pocet_stran)

    def __str__(self):# Vrací textovou hodnotu kosty
        return str (f"Kostla s {self._pocet_stran} stěnami")

sestisnna=Kostka()  # zkušenobní kostky přijdou smazat

desetistena=Kostka(12) # zkušenobní kostky přijdou smazat