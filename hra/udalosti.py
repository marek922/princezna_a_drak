import random
from postavy import hrdina

class Les1: #nizka obtiznost
    def __init__(self):

        self.seznam_nalez = ["obyčejná voda","běžný meč","obyčený štít","kniha","boruvka"]
        self.popis_nalez = ["doplnit životy", "vylepšit tvůj útok", "zdokonalit tvou obranu", "stát se chytřejším", "zahnat hlad"]
        self.ucinek_nalez = [1,1,1,1,2]
        self.nahodny_index = None

    def prochazej_se(self):
        """
        Vybere náhodný index a podle něj přidá do seznamu věcí danou položku, pokud je index mimo seznam, ubere hrdinovy životy.
        :return: hrdiny upravené seznamy, popřípadě ubraní životy
        """
        try:
            self.nahodny_index=random.randint(0,len(self.seznam_nalez)+0)
            hrdina.seznam_veci.append(self.seznam_nalez[self.nahodny_index])
            hrdina.popis_veci.append(self.popis_nalez[self.nahodny_index])
            hrdina.ucinek_veci.append(self.ucinek_nalez[self.nahodny_index])
        except IndexError:
            hrdina.zivoty-=2

    def __str__(self):
        """
        :return: vypíše co se přidalo do seznamu a jaké to má účinky, popřípadě o kolik životů hrdina přišel
        """
        try:
            return str (f""""Skvěle, procházel jsi se a našel jsi následující:
            {self.seznam_nalez[self.nahodny_index]}. tahle vec ti pomůže {self.popis_nalez[self.nahodny_index]}, přidá ti {self.ucinek_nalez[self.nahodny_index]}""")
        except IndexError:
            return str ("Sakra, máš smůlu, šlápl jsi na ostrou větev a přicházíš o 2 životy")

les1=Les1()


class Les2:#stredni obtiznost
    def __init__(self):
        self.seznam_nalez = ["pramenitá voda","prvotřídní meč","bytelný štít","velmi tlustá kniha"," čerstvá boruvka"]
        self.popis_nalez = ["doplnit životy", "vylepšit tvůj utok", "zdokonalit tvou obranu", "stat se chytřejším",
                            "zahnat hlad"]
        self.ucinek_nalez = [3,3,3,3,6]
        self.nahodny_index = None

    def prochazej_se(self):
        """
        Stejné, jaké třída Les 1, jen s pozměněnými položkami
        """

        try:
            self.nahodny_index = random.randint(0, len(self.seznam_nalez) + 1)
            hrdina.seznam_veci.append(self.seznam_nalez[self.nahodny_index])
            hrdina.popis_veci.append(self.popis_nalez[self.nahodny_index])
            hrdina.ucinek_veci.append(self.ucinek_nalez[self.nahodny_index])
        except IndexError:
            hrdina.zivoty -= 4

    def __str__(self):
        """
        vypíše co se přidalo do seznamu a jaké to má účinky, popřípadě o kolik životů hrdina přišel
        """
        try:
            return str(f""""Šel jsi hlouběji do lesa se a našel jsi následující:
            {self.seznam_nalez[self.nahodny_index]}. tahle věc ti pomůže {self.popis_nalez[self.nahodny_index]}, přidá ti {self.ucinek_nalez[self.nahodny_index]}""")
        except IndexError:
            return str("Ty jsi tu díru vážně neviděl? Přicházíš o 4 životy ")


les2 = Les2()

class Les3: #nejvyssí obtiznost
    def __init__(self):
        self.seznam_nalez = ["křisťálová voda","legendární meč","nebyčejný štít","zajímavá kniha","výborná boruvka"]
        self.popis_nalez = ["doplnit životy", "vylepšit tvůj utok", "zdokonalit tvou obranu", "stat se chytřejším",
                            "zahnat hlad"]
        self.ucinek_nalez = [5,5,5,5,10]
        self.nahodny_index = None

    def prochazej_se(self):
        """
         Stejné, jaké třída Les 1, jen s pozměněnými položkami
        """
        try:
            self.nahodny_index = random.randint(0, len(self.seznam_nalez) + 2)
            hrdina.seznam_veci.append(self.seznam_nalez[self.nahodny_index])
            hrdina.popis_veci.append(self.popis_nalez[self.nahodny_index])
            hrdina.ucinek_veci.append(self.ucinek_nalez[self.nahodny_index])
        except IndexError:
            hrdina.zivoty -= 6

    def __str__(self):
        """
        vypíše co se přidalo do seznamu a jaké to má účinky, popřípadě o kolik životů hrdina přišel
        """
        try:
            return str(f"""Strávil jsi v lese celý den a našel jsi následující:
            {self.seznam_nalez[self.nahodny_index]}. tahle vec ti pomůže {self.popis_nalez[self.nahodny_index]}, přidá ti {self.ucinek_nalez[self.nahodny_index]}""")
        except IndexError:
            return str("Potkal jsi medvěda a nebyl příliš přátelský, přicházíš o 6 životů")


les3 = Les3()


