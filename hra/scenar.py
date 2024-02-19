import random

import hlavni_dejova_linka
from hlavni_dejova_linka import Ukol_1
import udalosti
from kostka import sestisnna
import time
from postavy import hrdina

print("X" * 80+"\n")
print(""" Ahoj dobrodruhu, zaslechl jsem, že v nedaleké věži je uvězněná princezna.
Nechceš se ji pokusit vysvobodit? Stejně nemáš nic lepšího na práci.
Nebude to jednoduché, ale ty se přeci ničeho nebojíš\n""")
print("X" * 80+"\n")

vlastni_jmeno = str(input("Jak ti máme říkat dobrodruhu?\n"))

print(f"""Skvěle {vlastni_jmeno} teď budeš mít za úkol rozdělit 10 dovednostních bodů mezi tyto atributy:
Životy, Útok, Obrana, Inteligence a Odolnost proti hladu. Rozděluj uvážlivě a pamatuj, jen 10 bodů!\n """)


def zadani_hodnot(text):
    """
    Metoda pro zadávání hodnot s upozorněním na jinou hodnotu než číslo
    :param text: Zadaná hodnota
    """
    while True:
        try:
            hodnota = int(input(text))
            return hodnota
        except ValueError:
            print("Takhle to nepůjde. Zadej prosím pouze celé číslo")


celkem = 0
pokus_cislo = 10

while celkem != pokus_cislo: # postupné přiřazování hodnot pomocí funkce "zadání hodnot" k atribitům a následná kontrola, za byl přiřazen správný počet
    zivot_dodatek = zadani_hodnot(("Kolik bodů přičteš k životům? Čím více, tím odolnější budeš\n"))
    utok_dodatek = zadani_hodnot("Kolik bodů přičteš k útoku? Čím více, tím větší rány budeš rozdávat\n")
    obrana_dodatek = zadani_hodnot("Kolik bodů přičteš k obraně? Čím více, tím silnější tvůj štít bude\n")
    inteligence_dodatek = zadani_hodnot("Kolik bodů přičteš k inteligenci? Důvtip by se neměl podceňovat\n")
    hlad_dodatek = zadani_hodnot("Kolik bodů přičteš k potřebě jíst? Čím více, tím méně budeš muset jíst\n")
    print()
    celkem = zivot_dodatek + utok_dodatek + obrana_dodatek + inteligence_dodatek + hlad_dodatek

    if celkem < pokus_cislo:
        print("Nejspíš neumíš moc dobře počítat. Nějaké body ti ještě zbyly, zkus to znovu.")
    if celkem > pokus_cislo:
        pokus_cislo -= 1
        print(f"""Kdepak, podvádět se nevyplácí. Říkal jsem ti, jen 10. Tobě to bylo málo co?
        Tak teď už jich máš jen {pokus_cislo}\n """)


print("Povedlo se:)\n")

time.sleep(2)

hrdina.jmeno=vlastni_jmeno     # přičtení zadaných atributů, k základním atributům hrdiny
hrdina.zivoty+=zivot_dodatek
hrdina.utok+=utok_dodatek
hrdina.obrana+=obrana_dodatek
hrdina.inteligence+=inteligence_dodatek
hrdina.hlad+=hlad_dodatek
hrdina.max_zivot+=zivot_dodatek
hrdina.max_hlad+=hlad_dodatek
print(hrdina) # vypsání instance hrdina

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


pokrok = 0

while hrdina.je_nazivu(): # samotný průběh hrou
    while True:
        try:
            print()
            volba = int(input("Tak co uděláme teď? Jestli nevíš, zmáčkni 5 \n"))
            break
        except ValueError:
            print("Už zase? Říkam, aby jsi zadával jen celá čísla")

    if volba == 1:
        delka_chuze = float(input("""Na jak dlouho se chceš projít? Čím déle půjdeš, tím větší hlad budeš mít,
         ale můžeš najít zajímavější věci. Jedna jednotka procházky, sníží tvoji uroveň najezení o 1.

         Můžeš jít o 1 jednotku, o 3 jednotky, nebo o 5 jednotek 
          
         Tak o kolik půjdeš? (1/3/5)\n"""))

        if delka_chuze == 1: #spustí procházení v lese s nejniží obtížností
            udalosti.les1.prochazej_se()
            print(udalosti.les1)
            hrdina.jez()

        if delka_chuze == 3: #spustí procházení v lese s prostřední obtížností
            udalosti.les2.prochazej_se()
            print(udalosti.les2)
            for z in range(3):
                hrdina.jez()

        if delka_chuze == 5: #spustí procházení v lese s nejtěžší obtížností
            udalosti.les3.prochazej_se()
            print(udalosti.les3)
            for z in range(5):
                hrdina.jez()


    if volba == 2: # funkce na práci s předměty
        hrdina.vypis_veci()
        pouzit = str(input("Chceš něco z toho použít? ano/ne\n")).lower()
        print()
        if pouzit == "ano":
            hrdina.pouzij()
        if pouzit == "ne":
            print("Tak jsi se podíval a můžeme jít dál")
        elif pouzit != "ano" and pouzit != "ne":
            print("Sorry jako, ale tomuhle příkazu jsem vážně nerozumněl. ")

    if volba ==3:
        pokrok += 1

        if pokrok == 1:
            ukol1=Ukol_1(hrdina.inteligence)
            print(ukol1)
            ukol1.hadej()
        if pokrok == 2:
            print(hlavni_dejova_linka.ukol2)
            print()
            hlavni_dejova_linka.ukol2.hadej_hadanku()
        if pokrok == 3:
            print(hlavni_dejova_linka.ukol3)
            hlavni_dejova_linka.ukol3.kamen_nuzky_papir()
        if pokrok == 4:
            print(hlavni_dejova_linka.ukol4)
            hlavni_dejova_linka.ukol4.zadej_heslo()
        if pokrok == 5:
            print(hlavni_dejova_linka.ukol5)
            hlavni_dejova_linka.ukol5.boj_s_drakem()

            if hrdina.je_nazivu():
                print("Gratuluji, vyhrál jsi - princezna je tvoje ")
                break

    if volba == 4:
        print(hrdina.graficky_zivot())
        print(hrdina.graficky_hlad())
    if volba == 5:
        print(pokyny)

if hrdina.je_nazivu():
    pass
else:
    print()
    print("Je mi líto, zemřel jsi. Zkus to znovu, třeba budeš mít více štěstí. ")