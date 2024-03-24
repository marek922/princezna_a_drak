import random
import hlavni_dejova_linka
from hlavni_dejova_linka import Ukol_1
from hlavni_dejova_linka import Ukol_4
from hlavni_dejova_linka import Ukol_7
import udalosti
import time
from postavy import hrdina
from postavy import drak


print("X" * 80 + "\n")
print(""" Ahoj dobrodruhu, zaslechl jsem, že v nedaleké věži je uvězněná princezna.
Nechceš se ji pokusit vysvobodit? Stejně nemáš nic lepšího na práci.
Nebude to jednoduché, ale ty se přeci ničeho nebojíš\n""")
print("X" * 80 + "\n")

hrat="ano"

while hrat=="ano":
    pocatecni_cas = time.time() #spustí časomíru každé hry
    print()
    vlastni_jmeno = str(input("Jak ti máme říkat dobrodruhu?\n"))
    print()
    obtiznost=hlavni_dejova_linka.zadani_hodnot(""" Jak těžká má záchrana být? 
    
    pro lehkou obtížnost stiskni 1 
    pro normální obtížnost stiskni 2
    pro hrdinskou obtížnost stikni 3\n""",1,3)


    if obtiznost==1: #nastevení lehké obtížnosti
        pocet_bodu=15 #počet bodů na přidělení
        obtiznost_hadanka=1 #uprava pokusů na hádání čísla (ukol1)
        obtiznost_pocitani=3 #uprava počtu příkladů v sedmém ukolu
        sance_na_zraneni=0  #rozšíření rozsahu výběru a tím zvýšení šance zranení v lese
        obtiznost_heslo=2   #uprava pokusů na hádání hesla (ukol4)
        obtiznost_drak=-5  #uprava koficientu na upravu draka ( ukol 5)

    if obtiznost==2:
        pocet_bodu=10
        obtiznost_hadanka = 0
        obtiznost_pocitani = 0
        sance_na_zraneni = 1
        obtiznost_heslo = 0
        obtiznost_drak = 0

    if obtiznost==3:
        pocet_bodu=5
        obtiznost_hadanka = -1
        obtiznost_pocitani = -3
        sance_na_zraneni = 2
        obtiznost_heslo = -2
        obtiznost_drak=5

    drak.zivoty+=obtiznost_drak #samotná uprava draka - zivoty
    drak.utok+=obtiznost_drak #samotná uprava draka - utok
    drak.obrana+=obtiznost_drak #samotná uprava draka - obrana

    print(f"""Skvěle {vlastni_jmeno} teď budeš mít za úkol rozdělit {pocet_bodu} dovednostních bodů mezi tyto atributy:
    Životy, Útok, Obrana, Inteligence a zbytek přidáme do zásob jídla. Rozděluj uvážlivě a pamatuj, jen {pocet_bodu} bodů!\n """)




    celkem = 0
    pokus_cislo = pocet_bodu

    while celkem != pokus_cislo and pokus_cislo!=0:  # postupné přiřazování hodnot pomocí funkce "zadání hodnot" k atribitům a následná kontrola, za byl přiřazen správný počet
        zivot_dodatek = hlavni_dejova_linka.zadani_hodnot(("Kolik bodů přičteš k životům? Čím více, tím odolnější budeš\n"))
        utok_dodatek = hlavni_dejova_linka.zadani_hodnot("Kolik bodů přičteš k útoku? Čím více, tím větší rány budeš rozdávat\n")
        obrana_dodatek = hlavni_dejova_linka.zadani_hodnot("Kolik bodů přičteš k obraně? Čím více, tím silnější tvůj štít bude\n")
        inteligence_dodatek = hlavni_dejova_linka.zadani_hodnot("Kolik bodů přičteš k inteligenci? Důvtip by se neměl podceňovat\n")
        jidlo_dodatek = hlavni_dejova_linka.zadani_hodnot("Kolik bodů přičteš k zásobě jídla? Čím více, tím více ho budeš mít a jídlo se vždy hodí:)\n")
        print()
        celkem = zivot_dodatek + utok_dodatek + obrana_dodatek + inteligence_dodatek + jidlo_dodatek

        if celkem < pokus_cislo:
            print("Nejspíš neumíš moc dobře počítat. Nějaké body ti ještě zbyly, zkus to znovu.\n")
        if celkem > pokus_cislo:
            pokus_cislo -= 1
            if pokus_cislo>0:
                print(f"""Kdepak, podvádět se nevyplácí. Říkal jsem ti, jen {pokus_cislo}. Tobě to bylo málo co?
                        Tak teď už jich máš jen {pokus_cislo}\n """)
        if pokus_cislo==0:
            print("Tak a dost, nemáme na to celý den, jdeme dál\n")
            zivot_dodatek=0
            utok_dodatek=0
            obrana_dodatek=0
            inteligence_dodatek=0
            jidlo_dodatek=0
        if pokus_cislo==celkem:
            print("Super, můžeme jít dál:)\n")

    time.sleep(2)

    hrdina.jmeno = vlastni_jmeno  # přičtení zadaných atributů, k základním atributům hrdiny
    hrdina.zivoty += zivot_dodatek
    hrdina.utok += utok_dodatek
    hrdina.obrana += obrana_dodatek
    hrdina.inteligence += inteligence_dodatek
    hrdina.zasoba_jidla += jidlo_dodatek
    hrdina.max_zivot += zivot_dodatek
    hrdina.max_zasoba_jidla+= jidlo_dodatek
    print(hrdina)  # vypsání instance hrdina

    print()
    print()

    time.sleep(2)

    pokyny = ("""   Pohybujeme se stále jen v příkazovém řádku, takže toho moc neumíš, ale máš následující možnosti:
    Když stiskneš 1 - Půjdeš hledat stopy a zajímavé předměty do lesa 
    Když stiskneš 2 - Podíváš se co máš v tlumoku a budeš moci něco použít
    když stiskneš 3 - Posuneš se zas o něco blíž k princezně a za každý splěný úkol dostaneš svačinu 
    když stiskneš 4 - Vypíšu ti tvoje aktuální zdraví a úroveň hladu. 
    když stiskneš 5 - Zopakuji ti tvé možnosti
    
    Tak a teď už vážně hurá za princeznou""")
    print(pokyny)

    def prvni_ukol(): # pokyny k prvnímu ukolu
        ukol1 = Ukol_1(hrdina.inteligence+obtiznost_hadanka)
        print(ukol1)
        ukol1.hadej()

    def druhy_ukol(): # pokyny k druhému ukolu
        print(hlavni_dejova_linka.ukol2)
        print()
        hlavni_dejova_linka.ukol2.hadej_hadanku()

    def treti_ukol(): # pokyny k třetímu ukolu
        print(hlavni_dejova_linka.ukol3)
        print()
        hlavni_dejova_linka.ukol3.kamen_nuzky_papir()

    def sesty_ukol(): # jen přidává životy
        print(hlavni_dejova_linka.ukol6)
        hlavni_dejova_linka.ukol6.spanek()

    def sedmy_ukol(): #pokyny k sedmému úkolu
        if obtiznost==1:
            ukol7=Ukol_7(obtiznost_pocitani,"ne")
        else:
            ukol7=Ukol_7(obtiznost_pocitani)
        print(ukol7)
        print()
        ukol7.pocitej()


    seznam_ukolu=[prvni_ukol,druhy_ukol,treti_ukol,sesty_ukol,sedmy_ukol] #seznam dostupných úkolů

    def aktyvni_ukol(): # náhodně vybere úkol ze seznamu, spustí ho a pak smaže, aby se neopakoval
        ukol=random.choice(seznam_ukolu)
        ukol()
        seznam_ukolu.remove(ukol)

    pokrok = 0

    while hrdina.je_nazivu():  # samotný průběh hrou
        while True:
            try:
                print()
                volba = int(input("Tak co uděláme teď? Jestli nevíš, zmáčkni 5 \n"))
                break
            except ValueError:
                print("Už zase? Říkam, aby jsi zadával jen celá čísla")

        if volba == 1:
            delka_chuze = hlavni_dejova_linka.zadani_hodnot("""Na jak dlouho se chceš projít? Čím déle půjdeš, tím větší hlad budeš mít,
             a více jídla sníš. Ale můžeš najít zajímavější věci. Jedna jednotka procházky, spotřebuje jedno jídlo.
    
             Můžeš jít o 1 jednotku, o 3 jednotky, nebo o 5 jednotek 
    
             Tak o kolik půjdeš? (1/3/5)\n""",1,5)

            if delka_chuze == 1:  # spustí procházení v lese s nejniží obtížností
                udalosti.les1.prochazej_se(sance_na_zraneni)
                print(udalosti.les1)
                hrdina.jez()

            elif delka_chuze == 3:  # spustí procházení v lese s prostřední obtížností
                udalosti.les2.prochazej_se(sance_na_zraneni)
                print(udalosti.les2)
                for z in range(3):
                    hrdina.jez()

            elif delka_chuze == 5:  # spustí procházení v lese s nejtěžší obtížností
                udalosti.les3.prochazej_se(sance_na_zraneni)
                print(udalosti.les3)
                for z in range(5):
                    hrdina.jez()

            else:
                print(" Jsi rebel a zvolil jsi možnost, která nebyla na výběr , takže se vůbec nic nestalo. Příště zvol možnost 1 / 3 / 5")

        if volba == 2:  # funkce na práci s předměty
            if hrdina.hrdina_ma_tlumok == "ano":
                hrdina.vypis_veci()
                pouzit = None
                if len(hrdina.seznam_veci) != 0:
                    while pouzit != "ne" and len(hrdina.seznam_veci) != 0:
                        pouzit = str(input("Chceš něco z toho použít? ano/ne\n")).lower()
                        print()
                        if pouzit == "ano":
                            hrdina.pouzij()
                            print()
                            hrdina.vypis_veci()
                        elif pouzit != "ano" and pouzit != "ne":
                            print("Sorry jako, ale tomuhle příkazu jsem vážně nerozumněl. ")
                print("Tak jsi se podíval a můžeme jít dál")
            else:
                print("Bohužel žádný tlumok nemáš, musel jsi ho nechsat u gluma ")

        if volba == 3: # spuštění samotných úkolů důležitých o záchraně princezny
            pokrok += 1
            if pokrok <4:
                aktyvni_ukol()
            if pokrok == 4:
                ukol4=Ukol_4(obtiznost_heslo)
                print(ukol4)
                ukol4.zadej_heslo()
            if pokrok == 5:
                print(hlavni_dejova_linka.ukol5)
                hlavni_dejova_linka.ukol5.boj_s_drakem()

                if hrdina.je_nazivu():
                    print("Gratuluji, vyhrál jsi - princezna je tvoje ")
                    finalni_cas = time.time()
                    cas_dohrani_minuty = int((finalni_cas - pocatecni_cas) / 60)
                    cas_dohrani_vteriny = int((finalni_cas - pocatecni_cas) % 60)
                    print(f"Hru jsi dohrál za  {cas_dohrani_minuty} minuty a {cas_dohrani_vteriny} vteřin")

                    break

        if volba == 4:
            print(hrdina.graficky_zivot())
            print(hrdina.graficka_zasoba_jidla())
        if volba == 5:
            print(pokyny)

    if hrdina.je_nazivu():
        pass
    else:
        print()
        print("Je mi líto, zemřel jsi. Zkus to znovu, třeba budeš mít více štěstí. ")
        finalni_cas = time.time()
        cas_dohrani_minuty = int((finalni_cas - pocatecni_cas) / 60)
        cas_dohrani_vteriny = int((finalni_cas - pocatecni_cas) % 60)
        print(f"Ve hře jsi vydržel přesně {cas_dohrani_minuty} minuty a {cas_dohrani_vteriny} vteřin")

    print()
    hrdina.restart_postavy()
    hrat=input(" Chceš hrát znovu ? ano / ne\n").lower()


print("Děkji za hru a brzy zas na viděnou ")