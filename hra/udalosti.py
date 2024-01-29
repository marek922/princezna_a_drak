import random
from postavy import Hrdina


class Les:
    def __init__(self, delka_prochazky):
        self.delka_prochazky=delka_prochazky
        self.seznam_nalez = ["Obyčejná Voda","Běžný meč","Obyčený štít","Kniha","Boruvka"]
        self.popis_nalez = ["doplnit životy", "vylepšit tvůj utok", "Zdokonalit tvou obranu", "stat se chytřejším", "zahnat hlad"]
        self.ucinek_nalez = [1,1,1,1,2]
        self.nahodny_index = None

    def prochazej_se(self):
        try:
            self.nahodny_index=random.randint(0,self.delka_prochazky)
            Hrdina.seznam_veci.append(self.seznam_nalez[self.nahodny_index])
            Hrdina.popis_veci.append(self.popis_nalez[self.nahodny_index])
            Hrdina.ucinek_veci.append(self.ucinek_nalez[self.nahodny_index])
        except IndexError:
            pass # kod pro ubraní životů zatím nevyřešeno

    def __str__(self):
        try:
            return str (f""""Skvěle, procházel jsi se a našel jsi následující:
            {self.seznam_nalez[self.nahodny_index]}. tahle vec ti pomůže {self.popis_nalez[self.nahodny_index]}, přidá ti {self.ucinek_nalez[self.nahodny_index]}""")
        except IndexError:
            return str ("Sakra, máš smůlu, špláp jsi na ostrou větv a přicházíš o 2 životy")



les1=Les(5)





class Les1(Les):
    pass
class Les2(Les):
    pass
class Les3(Les):
    pass

