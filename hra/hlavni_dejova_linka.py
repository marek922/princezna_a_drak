import random
import time
from postavy import Hrdina

class Ukol_1: # deti - uhodni číslo - na pokusy - když vyhraje dosaten +5 utok nebo 5+ stit když ne tak ma smulu
    def __init__(self, pocet_pokusu):
        self.pocet_pokusu=pocet_pokusu+10
        self.cislo=random.randint(1, 10)
        self.odpoved=None
        self.max_pokusu=pocet_pokusu
        self.i=1
    def __str__(self):
        return str (f""" Na oboru vydíš polorozbeřnou věž a vidáš se s měrem k ní. Procházíš krásnou krajinou,
Když tu narazíš na skupinku dětí hrající si u vody. Hrají si na rytíře a říkají,
že když uhodneš, kolik dnes už snědli buchet, dají ti svůj největší poklad. Ale pozor, máš na to
jen {self.pocet_pokusu} pokusů a pokud neuhodneš, budeš je muset nakrmit. 

Souhlasíš a poprosíš alespoň o malinkou bápovědu. Prý je to něco mezi 1 až 10""")


    def hadej(self):
        while self.cislo != self.odpoved and self.pocet_pokusu != 0:
            self.odpoved = int(input("Zadej tvůj typ "))
            if self.odpoved < self.cislo:
                print()
                print("Zkus něco většího")
                print(f"zbývá ti jen {self.pocet_pokusu - 1} pokus ")
            elif self.odpoved > self.cislo:
                print()
                print("Zkus něco menšího ")
                print(f"zbývá ti jen {self.pocet_pokusu - 1} pokus ")
            else:
                print()
                print(f"Gratuluji, uhodl jsi to na {(self.i)}. pokus ")
                print("Děti se diví, že jsi jejich hádanku uhol a velmi neochotně ti dávají krásný meč")
                print("netušíš, kde k němu přišli, ale máš z něho velikou radost, při použití tvé síly zvýší o 5")
                Hrdina.seznam_veci.append("Vzácný meč od dětí")
                Hrdina.popis_veci.append("vylepšit tvůj utok")
                Hrdina.ucinek_veci.append(5)
            self.pocet_pokusu -= 1
            self.i+=1
        if self.pocet_pokusu == 0 and self.odpoved!=self.cislo:
            print()
            print(f"Neuhodl jsi, správný výsledek byl {self.cislo}, Dětsi se ti smějí a ty zahanbeně odcházíš pryč")


ukol1=Ukol_1(0)


class Ukol_2:
    pass
    # - glum - Hádanka - uhodnky hádanku - bude na to mít jen určitý čas - napsat více hádaken program si vybere kterou použije použít slovnik !!!!
class Ukol_3:
    pass
    # - Voják - můžeš si s ním zahrát nužky papír nebo ho zabít, povede se jen když máš sílu 25 a víc jinak isntatní smrt
class Ukol_4:
    pass
    # Šibenice - program hodí slovo a hráč háda, za každé špatné mísmeno ztatí život
class Ukol_5:
    pass
    # zabij draka - Klasický boj jeden na jednoho hráč si během hdy muže doplnovat životy možná by mohl i utect a vrátit se do lsesa .... možná