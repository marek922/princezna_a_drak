import random
import time
from postavy import hrdina
import kostka
from postavy import drak
class Ukol_1: # deti - uhodni číslo - na pokusy - když vyhraje dosaten +5 utok nebo 5+ stit když ne tak ma smulu
    def __init__(self, pokusy):
        pokusy-=7
        self.pocet_pokusu=pokusy
        self.cislo=random.randint(1, 10)
        self.odpoved=None
        self.i=1
    def __str__(self):
        return str (f""" Na oboru vydíš polorozbeřnou věž a vidáš se s měrem k ní. Procházíš krásnou krajinou,
Když tu narazíš na skupinku dětí hrající si u vody. Hrají si na rytíře a říkají,
že když uhodneš, kolik dnes už snědli buchet, dají ti svůj největší poklad. Ale pozor, máš na to
jen {self.pocet_pokusu} pokusů a pokud neuhodneš, budeš je muset nakrmit. 

Souhlasíš a poprosíš alespoň o malinkou bápovědu. Prý je to něco mezi 1 až 10""")


    def hadej(self):
        """

        :return:
        """
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
                hrdina.seznam_veci.append("Vzácný meč od dětí")
                hrdina.popis_veci.append("vylepšit tvůj utok")
                hrdina.ucinek_veci.append(5)
            self.pocet_pokusu -= 1
            self.i+=1
        if self.pocet_pokusu == 0 and self.odpoved!=self.cislo:
            print()
            print(f"Neuhodl jsi, správný výsledek byl {self.cislo}, Dětsi se ti smějí. Pdáš jim vlastní svačinu a zahanbeně odcházíš pryč")
            for z in range(2):
                hrdina.jez()


class Ukol_2:

    def __init__(self): #inteligence by mohla mít vliv na .... na nic
        self.spravna_odpoved=0
        self.pokus=0
        pass
    def __str__(self):
        return str(f""" Procházíš se krajinou, přes pole a lesy přímou k věži. Když najednou narazíš na jeskyni, 
        zvědavosti nedá a nahlídneš dovnitř. A koho tam nevidíš, Glum si pochutnává na čerstvé rybyčce a ty už určitě 
        moc dobře víš, jaká je Glumova oblíbená hra. Ano, hádanky. Slíbil ti, že když uhodneš 2 ze tří hádanek, pomůže ti 
        zachránit princeznu:) když se ti to ale nepovede, přijdeš o všechny předměty v tlumoku.""")

    hadanky={"cas":"pohltí: ptáky, stromy, květiny, kouše ocel; drtí tvrdé kameny na mouku; zabíjí krále, ničí města.",
            "tma":"Nemůže být viděno, nemůže být slyšeno. Leží za hvězdami a pod horami a prázdné díry vyplňuje. Končí život, zabíjí smích",
            "vitr":"Bez hlasu křičí, bez křídel létá, bez zubů kouše, bez úst šeptá. Co to je?",
             "slib":"Co můžeš vzít, zachránit nebo zlobit, ale nikdy nemůžeš vidět?",
             "sen":"Co můžeš vidět, ale nikdy se toho dotknout",
             "tajemstvi":"Když ho máš, hceš ho sdílet, když ho sdílíš, tak ho nemáš",
             "ozvena":"Mluví a nemá ústa, slyší, a nemá uši.Nemá tělo ale ožije hlasem.",
             "pavel":"Pavlova matka, má tři syny, první se jmenuje Pondělí, druhý úterý. Jak se jmenuje třetí",
            "prsten":"Copak to mám v kapsičce"}


    def hadej_hadanku(self):
        """

        :return:
        """
        while self.spravna_odpoved !=2 and self.pokus !=3:
            self.pokus+=1
            nahodna_hadanka = random.choice(list(self.hadanky.keys()))
            print (self.hadanky[nahodna_hadanka])
            odpoved=str(input("Co je to? (jedno slovo bez diakritiky)\n")).lower()
            if odpoved == nahodna_hadanka:
                self.spravna_odpoved+=1
                print("nevím, jak je to možné ale uhold jsi")
                print(f"Odpovědl jsi správně na {self.spravna_odpoved}")
                del self.hadanky[nahodna_hadanka]
            else:
                print("Tohle bohužel nebyla správná opodvěď.")
                del self.hadanky[nahodna_hadanka]

        if self.spravna_odpoved >1:
            print("""Glum nevěřícně krotí hlavou. Přehlrál jsi mě to je pravda, a já slib dodoržím,
            Princenu hlídá zlí drak, tady máš 12-stěnou kostku, s kterou ho snáze porazíš.""")
            hrdina.kostka=kostka.desetistena

        else:
            print("Neporazil jsi mě, ale nic si z toho nedelěje, nejsi první ani poslední. Nech tu všechny svoje věci a teď táhni, odkud jsi přišel")
            hrdina.seznam_veci.clear()
            hrdina.popis_veci.clear()
            hrdina.ucinek_veci.clear()

ukol2=Ukol_2()



class Ukol_3:  # - Voják - můžeš si s ním zahrát nužky papír nebo ho zabít, povede se jen když máš sílu 25 a víc jinak isntatní smrt

    def __init__(self):
        self.hrac_vyhra=0
        self.vojak_vyhra=0

    def __str__(self):
        return str(f""" Jdeš okolo tábora žoldáků, když zahlédneš vojáka, jak si leští stříbrný štít. 
        mimodek mu ho pochválíš. Poděkuje a posteskne si, že už nemá s kým hrát kámen nůžky papír. Pak se zamyslí a řekne:
        nechceš si se mnou zahrát ty? Když mě porazíš, dám ti tenhle štít, když tě ale porazím já, dáš mi svůj meč:).""")

    def kamen_nuzky_papir(self):
        """

        :return:
        """
        volba=int(input("Chceš si s ním zahrát ? zvol 1, chceš raději odejít? zvol 2, chceš ho praštít, vzít štít a utéct? zvol 3\n"))
        if volba == 1:
            while self.hrac_vyhra != 3 and self.vojak_vyhra != 3:
                moznosti = ["kamen", "nuzky", "papir"]
                hrac = input("Zadej kamen, nuzky nebo papir: ").lower()
                vojak = random.choice(moznosti)

                print(f"Vojak zvolil: {vojak}")

                if hrac in moznosti:
                    if hrac == vojak:
                        print("Remíza!")
                    elif (hrac == "kamen" and vojak == "nuzky") or \
                        (hrac == "nuzky" and vojak == "papir") or \
                        (hrac == "papir" and vojak == "kamen"):
                        self.hrac_vyhra += 1
                        print(f"Vyhráli jsi po {self.hrac_vyhra}!")

                    else:
                        self.vojak_vyhra += 1
                        print(f"Voják vyhrál po {self.vojak_vyhra}!")

                else:
                    print("Tohle neplatí. Zadejte pouze kamen, nuzky nebo papir.")
            if self.hrac_vyhra ==3:
                print("Gratuluji, vyhrál, jsi má na co být hrdý a tady ti předávám svůj šít ")
                hrdina.seznam_veci.append("Vojákuv štít")
                hrdina.popis_veci.append("vylepšit tvůji obranu")
                hrdina.ucinek_veci.append(5)
            else:
                print("Tak jsme zas vyhrál, už to začíná být nuda, dej mi svůj meč a pokračuj dál ")
                hrdina.utok-=5
        if volba ==2:
            print("Mávneš nat tím rukou a pokračuješ dál ")
        if volba ==3:
            print("Sotva jsi šáhl po meči, tak tak ti voják, přiložil ten svůj ke krku, tohle si jsi neměl dělat. ")
            print("přicházíš o 10 životů a na tohle setkání už jen tak nezapomeneš ")
            hrdina.zivoty-=10


ukol3=Ukol_3()

class Ukol_4:

    def __init__(self):
        self.slova = ["vytrvalost", "odvaha", "statecnost", "hrdina", "slava", "obetavost", "prsten", "udatnost", "respekt"]
        self.nahodne_slovo=self.slova[random.randint(0, len(self.slova)-1)]
        self.pocet_pokusu = 6
    def __str__(self):
        return str(f""" Konečně jsi došel až k věži, je všší než jsi očekával, zkoušíš zaklepat, ale nic se neděje. 
        na bráně je jen vybledý nápis: vložte heslo a okolo spoustu rozházených písmenek. zkusíš zadat správné heslo? """)

    def zadej_heslo (self):
        skyte_slovo=[]
        for pismeno in self.nahodne_slovo:
            skyte_slovo.append("_")

        while "_" in skyte_slovo:
            zadane_pismeno =input("Zadej pismeno v heslu\n").lower()
            for index in range(0,len(skyte_slovo)):
                if zadane_pismeno == self.nahodne_slovo[index]:
                    skyte_slovo[index]=zadane_pismeno
            if zadane_pismeno not in self.nahodne_slovo:
                print("špatně, tohle písmeno v heslu není")
                self.pocet_pokusu-=1
                if self.pocet_pokusu > 0:
                    print(f"zbývá pokusů {self.pocet_pokusu}")
                if self.pocet_pokusu==0:
                    print(f"Došli ti pokusy, teď ti začnou ubývat životy ")
                if self.pocet_pokusu <0:
                    hrdina.zivoty-=1
                    if hrdina.zivoty==0:
                        break
                    print("Zase špatně, přišel jsi o život")
                    print(hrdina.graficky_zivot())

            jen_pomlcky = ""
            for znak in skyte_slovo:
                jen_pomlcky += znak
            print(jen_pomlcky)
            print()

        if "_" not in self.nahodne_slovo and hrdina.zivoty>0:
            print("Brána se otevřela a ty můžeš vstoupit ")


ukol4=Ukol_4()

class Ukol_5:

    def __init__(self, postava1, postava2):
        self.postava1=postava1
        self.postava2=postava2
        self.vytrvalost=2

    def __str__(self):
        return str(f""" Rozzaril jsi veliké dveře, procházíš údrobami věže, a po princezně ani památky.
Stoupáš po schodech nahoru do posledního patra. když v tu jí uvidíš, spí na posteli. Chceš ji probudit 
polibkkem, tak jak se to v pohádkách dělá, ale když v tom něco zaslechneš a zatebou se objeví veliký drak. 
není čas na zbyt hurá do boje """)

    def boj_s_drakem (self):
         while self.postava1.je_nazivu() and self.postava2.je_nazivu():
            styl_boje=int(input("Chceš zaútočit, nebo se bránit? pro útok stiskni 1 a pro obranu 2\n"))
            if styl_boje==1:
                self.vytrvalost-=1
                if self.vytrvalost>=0:
                    self.postava1.utoc(self.postava2)
                if self.vytrvalost<0:
                    prekvapeni=random.randint(1,10)
                    if prekvapeni>7:
                        self.postava2.utoc(self.postava1)
                    else:
                        self.postava1.jez()
                        self.postava1.utoc(self.postava2)
                print()
                print(f"tvoje aktuální vytrvalost je {self.vytrvalost}")
                print(f"tvoje aktuální zdraví je: {self.postava1.graficky_zivot()}")
                print(f"tvoje aktuální mira nasyceni je: {self.postava1.graficky_hlad()}")
                print(f"Drakovy životy jsou {self.postava2.graficky_zivot()}")
                print()

            if styl_boje==2:
                self.vytrvalost+=1
                if self.vytrvalost>5:
                    self.postava1.zivoty+=1
                self.postava2.utoc(self.postava1)
                print()
                print(f"tvoje aktuální vytrvalost je {self.vytrvalost}")
                print(f"tvoje aktuální zdraví je: {self.postava1.graficky_zivot()}")
                print(f"tvoje aktuální mira nasyceni je: {self.postava1.graficky_hlad()}")
                print(f"Drakovy životy jsou {self.postava2.graficky_zivot()}")
                print()

ukol5=Ukol_5(hrdina,drak)
