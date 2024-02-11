import random
from postavy import hrdina

class Les1:
    def __init__(self):
        self.seznam_nalez = ["Obyčejná voda","Běžný meč","obyčený štít","kniha","boruvka"]
        self.popis_nalez = ["doplnit životy", "vylepšit tvůj utok", "Zdokonalit tvou obranu", "stat se chytřejším", "zahnat hlad"]
        self.ucinek_nalez = [1,1,1,1,2]
        self.nahodny_index = None

    def prochazej_se(self):
        try:
            self.nahodny_index=random.randint(0,len(self.seznam_nalez)+0)
            hrdina.seznam_veci.append(self.seznam_nalez[self.nahodny_index])
            hrdina.popis_veci.append(self.popis_nalez[self.nahodny_index])
            hrdina.ucinek_veci.append(self.ucinek_nalez[self.nahodny_index])
        except IndexError:
            hrdina.zivoty-=2

    def __str__(self):
        try:
            return str (f""""Skvěle, procházel jsi se a našel jsi následující:
            {self.seznam_nalez[self.nahodny_index]}. tahle vec ti pomůže {self.popis_nalez[self.nahodny_index]}, přidá ti {self.ucinek_nalez[self.nahodny_index]}""")
        except IndexError:
            return str ("Sakra, máš smůlu, špláp jsi na ostrou větv a přicházíš o 2 životy")

les1=Les1()


class Les2:
    def __init__(self):
        self.seznam_nalez = ["Pramenitá voda","Prvotřídní meč","Bytelný štít","Velmi tlustá kniha"," čerstvá boruvka"]
        self.popis_nalez = ["doplnit životy", "vylepšit tvůj utok", "Zdokonalit tvou obranu", "stat se chytřejším",
                            "zahnat hlad"]
        self.ucinek_nalez = [3,3,3,3,6]
        self.nahodny_index = None

    def prochazej_se(self):
        try:
            self.nahodny_index = random.randint(0, len(self.seznam_nalez) + 0)
            hrdina.seznam_veci.append(self.seznam_nalez[self.nahodny_index])
            hrdina.popis_veci.append(self.popis_nalez[self.nahodny_index])
            hrdina.ucinek_veci.append(self.ucinek_nalez[self.nahodny_index])
        except IndexError:
            hrdina.zivoty -= 4

    def __str__(self):
        try:
            return str(f""""Šel jsi hlouběji do lesa se a našel jsi následující:
            {self.seznam_nalez[self.nahodny_index]}. tahle vec ti pomůže {self.popis_nalez[self.nahodny_index]}, přidá ti {self.ucinek_nalez[self.nahodny_index]}""")
        except IndexError:
            return str("Ty jsi tu díru vážně neviděl? přicházíš o 4 životy")


les2 = Les2()

class Les3:
    def __init__(self):
        self.seznam_nalez = ["Křisťálová voda","Legendární meč","Nebyčejný štít","Zajímavá kniha","výborná boruvka"]
        self.popis_nalez = ["doplnit životy", "vylepšit tvůj utok", "Zdokonalit tvou obranu", "stat se chytřejším",
                            "zahnat hlad"]
        self.ucinek_nalez = [5,5,5,5,10]
        self.nahodny_index = None

    def prochazej_se(self):
        try:
            self.nahodny_index = random.randint(0, len(self.seznam_nalez) + 0)
            hrdina.seznam_veci.append(self.seznam_nalez[self.nahodny_index])
            hrdina.popis_veci.append(self.popis_nalez[self.nahodny_index])
            hrdina.ucinek_veci.append(self.ucinek_nalez[self.nahodny_index])
        except IndexError:
            hrdina.zivoty -= 6

    def __str__(self):
        try:
            return str(f"""Stravil jsi v lese celý den a našel jsi následující:
            {self.seznam_nalez[self.nahodny_index]}. tahle vec ti pomůže {self.popis_nalez[self.nahodny_index]}, přidá ti {self.ucinek_nalez[self.nahodny_index]}""")
        except IndexError:
            return str("Potkal jsi medvěda a nebyl příliš přáteský, přicházíš o 6 životů")


les3 = Les3()


