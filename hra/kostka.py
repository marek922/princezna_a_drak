
class Kostka:
    """
    Třída simulující hod kostkou
    """
    def __init__(self, pocet_stran=6):
        self._pocet_stran = pocet_stran

    def hod (self):  # samotný hod kostkou, gerneruje náhodné číslo mezi 1 a počtem stěn
        import random as _random
        return _random.randint(1,self._pocet_stran)

    def __str__(self):# Vrací textovou hodnotu kosty
        return str (f"Kostla s {self._pocet_stran} stěnami")

sestisnna=Kostka() # základní kostka

dvanactistena=Kostka(12)  # 12 - stěná kostka, lze zíksat po splnění úkolu ve jeskyni

