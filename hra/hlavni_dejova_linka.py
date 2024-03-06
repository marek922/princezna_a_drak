import random
import time
from postavy import hrdina
import kostka
from postavy import drak

class Ukol_1:  # první úkoly, ve kterém je potřeba uhodnout náhodné číslo, uspěch přidá meč s utokem z 5 a nesupěch odebere 5 nasicení
    def __init__(self, pokusy):
        """
        :param pokusy: počet pokusů je o 9 menší, než je hrdinova Inteligence
        """
        pokusy-=9
        self.pocet_pokusu=pokusy
        self.cislo=random.randint(1, 10)
        self.odpoved=None
        self.i=1
    def __str__(self):
        """
        :return: Textový úvod do prvního úkolu s dětmi
        """
        return str (f""" Na obzoru vidíš polorozbořenou věž a vydáš se směrem k ní. Procházíš krásnou krajinou
když tu narazíš na skupinku dětí dovádějícíh u vody. Hrají si na rytíře a slibují,
že pokud uhodneš kolik dnes už snědly buchet, dají ti svůj největší poklad. Ale pozor, máš na to
jen {self.pocet_pokusu} pokusů a pokud neuhodneš, budeš je muset nakrmit alespoň 5 buchtami. 

Souhlasíš, ale poprosíš je alespoň o malinkou nápovědu. Prý je to něco mezi 1 až 10""")


    def hadej(self):
        """
        Samotná hra na hádání náhodně vygenerovaného čísla
        :return:vrací meč na vylepšení životů nebo snížený atribut hladu
        """
        while self.cislo != self.odpoved and self.pocet_pokusu != 0: #hráč hádá dokud mu nedojdou pokusy, nebo neuhodl číslo
            self.odpoved = int(input("Zadej tvůj tip "))
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
                print(f"Gratuluji, uhodl jsi to na {(self.i)}. pokusy ")
                print("Děti se diví, že jsi jejich hádanku uhodl a velmi neochotně ti dávají krásný meč")
                print("Netušíš, kde k němu přišly, ale máš z něj velikou radost. Při použití se tvá síla zvýší o 5")
                hrdina.seznam_veci.append("Vzácný meč od dětí")
                hrdina.popis_veci.append("vylepšit tvůj utok")
                hrdina.ucinek_veci.append(5)
                hrdina.zasoba_jidla+=5
            self.pocet_pokusu -= 1
            self.i+=1
        if self.pocet_pokusu == 0 and self.odpoved!=self.cislo:
            print()
            print(f"Neuhodl jsi - správný výsledek byl {self.cislo}. Děti se ti smějí. Dáš jim svačinu a zahanbeně odcházíš pryč")
            for z in range(5):
                hrdina.jez()


class Ukol_2:

    def __init__(self): # druhý úkol s hádáním hádanek
        self.spravna_odpoved=0
        self.pokus=0
        pass
    def __str__(self):
        """
        Textový úvod do hry s hádankami
        """
        return str(f"""     Procházíš se krajinou, přes pole a lesy přímo k věži. Když najednou narazíš na jeskyni. 
        Zvědavost ti nedá a nahlídneš dovnitř. A koho tam nevidíš - Glum si pochutnává na čerstvé rybičce a ty už určitě 
        moc dobře víš, jaká je Glumova oblíbená hra. Ano, hádanky. Slíbil ti, že když uhodneš 2 ze 3 hádanek, pomůže ti 
        zachránit princeznu:) Když se ti to ale nepovede, přijdeš o celý tlumok a předměty v něm.""")

    hadanky={"cas":"Pohltí: ptáky, stromy, květiny. Kouše ocel, drtí tvrdé kameny na mouku, zabíjí krále a ničí města.",
            "tma":"Nemůže být viděno, nemůže být slyšeno. Leží za hvězdami a pod horami a prázdné díry vyplňuje. Končí život, zabíjí smích",
            "vitr":"Bez hlasu křičí, bez křídel létá, bez zubů kouše, bez úst šeptá. Co to je?",
            "slib":"Co můžeš dát, zachovat nebo porušit, ale nikdy nemůžeš vidět?",
            "sen":"Co můžeš vidět, ale nikdy se toho dotknout",
            "tajemstvi":"Když ho máš, chceš ho sdílet, když ho sdílíš, tak ho nemáš",
            "ozvena":"Mluví a nemá ústa, slyší a nemá uši. Nemá tělo, ale ožije hlasem.",
            "pavel":"Pavlova matka má tři syny. První se jmenuje Pondělí, druhý Úterý. Jak se jmenuje třetí?",
            "prsten":"Copak to mám v kapsičce"}


    def hadej_hadanku(self):
        """
        Samotná hra na hádání hádanek
        :return: Poskytne hrdinovi 12-stenou kostku nebo mu odebere všechny předměty
        """
        while self.spravna_odpoved !=2 and self.pokus !=3:
            self.pokus+=1
            nahodna_hadanka = random.choice(list(self.hadanky.keys())) # vebre náhodnou hádanku ze slovníku
            print (self.hadanky[nahodna_hadanka]) #vypíše prve vybranou hádnku
            odpoved=str(input("Co je to? (jedno slovo bez diakritiky)\n")).lower() # převede odpověď na malá písmena
            print()
            if odpoved == nahodna_hadanka:
                self.spravna_odpoved+=1
                print("Nevím, jak je to možné, ale uhodl jsi.")
                print(f"Odpověděl jsi správně na {self.spravna_odpoved}\n")
                del self.hadanky[nahodna_hadanka] # smaže vybranou hádnku, aby se neopakovali
            else:
                print("Tohle bohužel nebyla správná opodvěď.")
                del self.hadanky[nahodna_hadanka] # smaže vybranou hádnku, aby se neopakovali

        if self.spravna_odpoved >1:
            print("""Glum nevěřícně kroutí hlavou. Přehrál jsi mě, to je pravda, a já slib dodržím,
            Princenu hlídá zlý drak Šmak. Tady máš 12-stěnou kostku s kterou ho snáze porazíš.""")
            hrdina.kostka=kostka.dvanactistena # uprava hrdinovy kostky
            hrdina.zasoba_jidla += 5

        else:
            print("Neporazil jsi mě, ale nic si z toho nedelěj. Nejsi první, ani poslední. Nech tu celý tlumok a teď táhni, odkud jsi přišel")
            hrdina.seznam_veci.clear() # smaže položky v seznnamu věci u hrdniny
            hrdina.popis_veci.clear() # smaže položky v poposu věci u hrdiny
            hrdina.ucinek_veci.clear() # smaže položky v ucinku věcci u hrdiny
            hrdina.hrdina_ma_tlumok="ne"

ukol2=Ukol_2()



class Ukol_3: # 3 . úkol s vojákem a hra kámen nůžky papír

    def __init__(self):
        self.hrac_vyhra=0
        self.vojak_vyhra=0

    def __str__(self):
        """
        Textový úvod k úkolu s vojákem
        """
        return str(f"""     Jdeš okolo tábora žoldáků, když tu zahlédneš vojáka, jak si leští stříbrný štít. 
        Mimoděk mu ho pochválíš. Poděkuje a posteskne si, že už nemá s kým hrát kámen nůžky papír. Pak se zamyslí a řekne:
        Nechceš si se mnou zahrát ty? Když mě porazíš, dám ti tenhle štít, když tě ale porazím já, dáš mi svůj meč:).\n""")

    def kamen_nuzky_papir(self):
        """
        Samotná hra kámen nůžky papír
        :return: podle volby hráče, hrdina získá štít, nebo přijde o 5 bodů útoku, popřípadě o 10 životů
        """
        volba=int(input("Chceš si s ním zahrát ? zvol 1 Chceš raději odejít? zvol 2 Chceš ho praštít, vzít štít a utéct? zvol 3\n"))
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
                        print(f"Vyhrál jsi po {self.hrac_vyhra}!   Voják zatím vyhrál {self.vojak_vyhra} her.")

                    else:
                        self.vojak_vyhra += 1
                        print(f"Voják vyhrál po {self.vojak_vyhra}!     Ty jsi zatím vyhrál {self.hrac_vyhra} her.")

                else:
                    print("Tohle neplatí. Zadejte pouze kamen, nuzky nebo papir.")
            if self.hrac_vyhra ==3:
                print("Gratuluji, vyhrál jsi a máš na co být hrdý. Tady ti předávám můj štít ")
                hrdina.seznam_veci.append("Vojákuv štít") # přidání štítů a všch jeho astributů do příslušných seznamů.
                hrdina.popis_veci.append("vylepšit tvůji obranu")
                hrdina.ucinek_veci.append(5)
                hrdina.zasoba_jidla += 5
            else:
                print("Tak jsem zas vyhrál. Už to začíná být nuda. Dej mi svůj meč a pokračuj dál. ")
                hrdina.utok-=5 # odebere hrdinový 5 bodů z útoku
        if volba ==2:
            print("Mávneš nad tím rukou a pokračuješ dál ")
        if volba ==3:
            nahoda=random.randint(1,3)
            if nahoda == 1 or 2:
                print("Sotva jsi šáhl po meči, tak ti voják přiložil ten svůj ke krku. Tohle si jsi neměl dělat. ")
                print("Přicházíš o 10 životů a na tohle setkání už jen tak nezapomeneš ")
                hrdina.zivoty-=10 # ubere hrdinovy životy
            else:
                print("Dříve než si voják uvědomil co se děje, tak jsi ho prašil jílcem meče a i se štítem jsi utekl pryč.")
                hrdina.seznam_veci.append("Vojákův štít")  # přidání štítů a všch jeho astributů do příslušných seznamů.
                hrdina.popis_veci.append("vylepšit tvoji obranu")
                hrdina.ucinek_veci.append(5)
                hrdina.zasoba_jidla += 5



ukol3=Ukol_3()

class Ukol_4: # 4 ukol na hádání hesla do věže

    def __init__(self):
        """
        slova je seznam možností, z kterých může program vybírat
        náhodné slovo je slovo, který prohram vybral
        počet pokusů je počet pokusů , který hráč má, než mu začnou mizet životy
        """
        self.slova = ["vytrvalost", "odvaha", "statecnost", "hrdina", "slava", "obetavost", "prsten", "udatnost", "respekt", "programator"]
        self.nahodne_slovo=self.slova[random.randint(0, len(self.slova)-1)]
        self.pocet_pokusu = 5
    def __str__(self):
        """
        Textový úvod k úkolu se vstupem do věže
        """
        return str(f"""     Konečně jsi došel až k věži. Je vyšší než jsi očekával. Zkoušíš zaklepat, ale nic se neděje. 
        Na bráně je jen vybledý nápis: vložte heslo a na zemi okolo je spousta rozházených písmenek. Zkusíš zadat správné heslo?\n """)

    def zadej_heslo (self):
        """
        Samotná hra na hádání hesla
        :return: ubrané životy, pokud hráč neuhodne slovo na příšluný počet životů
        """
        skyte_slovo=[] #nahradí všechna písmena ve skrytém slově pomlčekou a nahraje je do seznamu
        for pismeno in self.nahodne_slovo:
            skyte_slovo.append("_")

        while "_" in skyte_slovo: # program pobeží, dokud sryté slovo, bude obsahovat pomlčku
            zadane_pismeno =input("Zadej písmeno v heslu\n").lower()
            for index in range(0,len(skyte_slovo)): # program projede skyrté slovo a pokud obsahuje zadané písmeno, tak ho doplní místo pomlčky do skrytého slova
                if zadane_pismeno == self.nahodne_slovo[index]:
                    skyte_slovo[index]=zadane_pismeno
            if zadane_pismeno not in self.nahodne_slovo: # v případě že písmeno není ve skyrytém slově, odebere pokus
                print("špatně, tohle písmeno v heslu není")
                self.pocet_pokusu-=1
                if self.pocet_pokusu > 0:
                    print(f"zbývá pokusů {self.pocet_pokusu}")
                if self.pocet_pokusu==0:
                    print(f"Došly ti pokusy, teď ti začnou ubývat životy ")
                if self.pocet_pokusu <0: #jakmile dojdou pokusy, zažnou ubývat životy
                    hrdina.zivoty-=1
                    if hrdina.zivoty==0: #jamile dojdou životy hra skončí
                        break
                    print("Zase špatně, přišel jsi o život")
                    print(hrdina.graficky_zivot())

            jen_pomlcky = ""
            for znak in skyte_slovo: # přvode seznam skyrytého slova na textový řetěz - díky tomu, je to vizuálně hezčí
                jen_pomlcky += znak
            print(jen_pomlcky+"\n")


        if "_" not in self.nahodne_slovo and hrdina.zivoty>0: # podmínka pro vítězství ve hře
            print("Brána se otevřela a ty můžeš vstoupit ")
            hrdina.zasoba_jidla += 5


ukol4=Ukol_4()

class Ukol_5:

    def __init__(self, postava1, postava2):
        self.postava1=postava1
        self.postava2=postava2
        self.vytrvalost=2

    def __str__(self):
        return str(f"""     Rozrazil jsi veliké dveře, procházíš útrobami věže, ale po princezně ani památky.
Stoupáš po schodech nahoru do posledního patra. Když v tu jí uvidíš spát na posteli. Chceš ji probudit 
polibkem, tak jak se to v pohádkách přeci dělá. Když v tom něco zaslechneš a za tebou se objeví veliký drak. 
Není čas na zbyt, hurá do boje. 

Jen malá vsuvka: pamatuj, že každým útokem ti klesne vytrvalost a pokud spadne do záporných hodnot, budeš mít hlad.
A ty už moc dobře víš, co to znamená. Při záporné  vytrvalosti se ti útok nemusí povést a zaútočí naopak drak. 
Když se ale budeš bránit, tvoje vytrvalost bude stoupat. Pokud bude dost vysoká, přijde možná i další bonus. 
Konec vsuvky a hurá do boje""")

    def boj_s_drakem (self):
        """
        Samotný boj s drakem, hráč dostane na výběr, jestli se chce bránit, nebo útočit.
        Při útoku mu klesá vytrvalost, když vytrvalost klesne na pod nulu, přichází o 5 jednotek nasycení a následně životů za každý utok a apliuje se princip překvapení.
        Za  každou obranu se mu naopak zvedá vytrvalost o 1 a pokud je vytrvalost větší než 5, tak se mi přidá i 5 životů
        Princip překvapení - náhodné číslo a podkud je větší než 5. tak neútočí hráč, ale drak.
        :return: Smrt jedné z postav
        """
        while self.postava1.je_nazivu() and self.postava2.je_nazivu(): #cyklus běží, dokud je jedna z postav na živu
            styl_boje=int(input("Chceš zaútočit, nebo se bránit? pro útok stiskni 1 a pro obranu 2\n"))
            if styl_boje==1:
                self.vytrvalost-=1 # při útoku klesne vytrvalost o 1
                if self.vytrvalost>=0: # pokud je vytrvalost rovna, nebo větší než 0 provede se běžný útok
                    self.postava1.utoc(self.postava2)
                if self.vytrvalost<0:
                    prekvapeni=random.randint(1,10) #generování překvapení
                    if prekvapeni>5:
                        print(f"Zakopl jsi a promrhal tak šanci na útok. Místo toho se na tebe vrhl drak")
                        self.postava2.utoc(self.postava1) # pokud bude překvapení menší než 5, tak útočí drak
                    else:
                        for p in range(5):
                            self.postava1.jez()
                        self.postava1.utoc(self.postava2)
                print()
                print(f"tvoje aktuální vytrvalost je {self.vytrvalost}")
                print(f"{self.postava1.graficky_zivot()}")
                print(f"{self.postava1.graficka_zasoba_jidla()}")
                print(f"Drakuv {self.postava2.graficky_zivot()}\n")
                print()

            if styl_boje==2:
                self.vytrvalost+=1
                if self.vytrvalost>5:
                    self.postava1.zivoty+=5
                self.postava2.utoc(self.postava1)
                print()
                print(f"tvoje aktuální vytrvalost je {self.vytrvalost}")
                print(f"{self.postava1.graficky_zivot()}")
                print(f"{self.postava1.graficka_zasoba_jidla()}")
                print(f"Drakuv {self.postava2.graficky_zivot()}\n")
                print()
            else:
                print("Tak znovu a pořádně")

ukol5=Ukol_5(hrdina,drak)


class Ukol_6:
    def __str__(self):
        return str ("""Našel jsi krásný palouček, který tě přímo vybízel ke spánku. Neodolal jsi a na chvilku jsi si zdřímnul.
        
        Vzbudil jsi se krásně odpočatý a říkáš si, že už jsi se dlouho tak hezky bevyspal. 
        
        Získáváš 5 životů """)

    def spanek(self):
        hrdina.zivoty+=5

ukol6=Ukol_6()
