
import kostka
class Postava: #třída pro univerzální postavu
    def __init__(self, jmeno, zivoty, utok, obrana, inteligence, kostka):
        """

        :param jmeno:
        :param zivoty:
        :param utok:
        :param obrana:
        :param inteligence:
        :param kostka:
        """
        self.jmeno=jmeno
        self.zivoty=zivoty
        self.max_zivot=zivoty
        self.utok=utok
        self.obrana=obrana
        self.inteligence=inteligence
        self.kostka=kostka
        self.zprava = ""

    def __str__(self):
        return str(f"Ahoj, já jsem hrdina {self.jmeno} mám {self.zivoty} životů, a těším se na to, co s polu prožijeme")

    def je_nazivu(self):
        return self.zivoty>0

    def uber_zivot(self, pocet):
        self.zivoty-=pocet


    def graficky_ukazatel(self, aktulani, maxilmani, popis):
        """

        :param aktulani:
        :param maxilmani:
        :param popis:
        :return:
        """
        celkem=maxilmani
        pocet=int(aktulani/maxilmani*celkem)
        if pocet<0:
            pocet=0

        if pocet==(celkem/2):
            return f"Aktuální počet {popis} je {aktulani} [{'-'*(celkem-pocet)}{'X'*pocet}]\n Jsi v půlce {popis}"
        if pocet==3:
            return f"Aktuální počet {popis} je {aktulani} [{'-' * (celkem - pocet)}{'X' * pocet}]\n Nechci tě stresovat, ale zbývají ti jen 3 jednotky {popis}"
        if pocet==1:
            return f"Aktuální počet {popis} je {aktulani} [{'-' * (celkem - pocet)}{'X' * pocet}]\n Konec se blíží !!! "
        else:
            return f"Aktuální počet {popis} je {aktulani} [{'-' * (celkem - pocet)}{'X' * pocet}]"


    def graficky_zivot(self):
        return self.graficky_ukazatel(self.zivoty, self.max_zivot, "životů")

    def aktualizuj_zpravu(self,zprava):
        self.zprava=zprava

    def vypis_zpravu(self):
        return self.zprava

    def utoc(self, protivnik):
        hod_utok=self.kostka.hod()
        uder = self.utok + hod_utok
        print(f"na kostce padlo {hod_utok}, takže {self.jmeno} útočí za {self.utok+hod_utok}")
        protivnik.bran_se(uder)

    def bran_se(self, uder):
        hod_obrana=self.kostka.hod()
        print(f"na kostce padlo {hod_obrana}, takže {self.jmeno} se brání za {self.obrana+hod_obrana}")
        zraneni = uder - (self.obrana+hod_obrana)
        if zraneni > 0:
            print (f"{self.jmeno} utrpěl zranění {zraneni}")
            self.zivoty-=zraneni
            if self.zivoty<0:
                self.zivoty=0
                print(f"{self.jmeno} utrpěl smrtelné zranění a zemřel")

        else:
            print(f"{self.jmeno} bez potíží odrazil útok")


class Hrdina(Postava):
    def __init__(self, jmeno, zivoty, utok, obrana, inteligence, kostka, hlad ):
        super().__init__(jmeno, zivoty, utok, obrana, inteligence, kostka)
        self.hlad=hlad
        self.max_hlad=hlad #hlad funguje jako životy, když hlad bude na nule, začnou mizet životy
        self.zprava = ""
    def __str__(self):
        return str(f"""Ahoj, já jsem hrdina {self.jmeno} mám {self.zivoty} životů, útočím za {self.utok} bodů a můj štít vydrží až {self.obrana} ran.
Jsem docela jedlík, hlad začnu mít po {self.hlad} hodinách. Do menzi mě sice nevzali, ale moje inteligence dosahuje {self.inteligence} bodů.
        Ale teď už koncec keců a hurá za princeznou.""")

    def jez (self):
        """

        :return:
        """
        self.hlad-=1
        if self.hlad <0:
            self.hlad=0
            self.zivoty-=1

    def graficky_hlad(self):
        return self.graficky_ukazatel(self.hlad, self.max_hlad, "hladu")

    seznam_veci=[]
    popis_veci=[]
    ucinek_veci=[]

    def prace_s_tlumokem (self):
        pass

    def vypis_veci(self):
        for polozka in range(len(self.seznam_veci)):
            print(f"{polozka} - {self.seznam_veci[polozka]} - Pomože ti {self.popis_veci[polozka]} - Díky tomu máš vylepšení {self.ucinek_veci[polozka]}")
        print()
        print(f"Tvoje aktální schopnosti jsou: Životy: {self.zivoty}, Útok: {self.utok}, Obrana: {self.obrana}, Inteligence: {self.inteligence}, Hlad: {self.hlad},")
        print()
    def pouzij (self):
        index=int(input("Kterou položku chceš využít?\n"))
        if index <0 or index > len(self.seznam_veci):
            print("Netuším, jak jsi na to přišel, ale takovou položku v tlumoku nemáš")
        else:
            if "voda" in self.seznam_veci[index]:
                self.zivoty += int(self.ucinek_veci[index])
            if "meč" in self.seznam_veci[index]:
                self.utok += int(self.ucinek_veci[index])
            if "štít" in self.seznam_veci[index]:
                self.obrana += int(self.ucinek_veci[index])
            if "kniha" in self.seznam_veci[index]:
                self.inteligence += int(self.ucinek_veci[index])
            if "boruvka" in self.seznam_veci[index]:
                self.hlad += int(self.ucinek_veci[index])

            print(f"Skvěle, použil jsi {self.seznam_veci[index]}")
            print(f"Tvoje aktální schopnosti jsou: Životy: {self.zivoty}, Útok: {self.utok}, Obrana: {self.obrana}, Inteligence: {self.inteligence}, Hlad: {self.hlad},")
            del self.seznam_veci[index]
            del self.popis_veci[index]
            del self.ucinek_veci[index]


hrdina=Hrdina(None,10,10,10,10,kostka.desetistena,10)
drak=Postava("Šmak", 20, 10, 10, 20, kostka.sestisnna)

