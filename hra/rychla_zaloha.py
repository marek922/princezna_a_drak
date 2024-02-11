import hlavni_dejova_linka
import udalosti
from kostka import sestisnna
import time
from postavy import hrdina

print("X" * 80)
print()
print(""" Ahoj dobrodruhu, zaslechl jsem, že v nedaleké věži, je uvězněná princezna.
Nechceš se ji pokusit vysvobodit, stejně nemáš nic lepšího na práci.
Nebude to jednoduché, ale ty se přei ničeho nebohíš""")
print()
print("X" * 80)

print()
vlastni_jmeno = str(input("Jak ti máme říkat dobrodruhu?\n"))

print(f"""Skvěle {vlastni_jmeno} Teď budeš mít za úkol, rozdělit 10 dovednostních bodů, mezi tyto atribut:
Životy, Útok, Obrana, Intelihence a odolnosti proti hladu. Rozděluj uvážlivě a pamatuj, jen 10 bodů! """)
print()


def zadani_hodnot(text):
    while True:
        try:
            hodnota = int(input(text))
            return hodnota
        except ValueError:
            print("Takhle to nepůjde, zadej prosím pouze celé číslo")


celkem = 0
pokus_cislo = 10

while celkem != pokus_cislo:
    zivot_dodatek = zadani_hodnot(("Kolik bodů přičteš k životů? čím více, tím odolnější budeš\n"))
    utok_dodatek = zadani_hodnot("Kolik bodů přičteš k Útoku? čím více, tím větší rány budeš rozdávat\n")
    obrana_dodatek = zadani_hodnot("Kolik bodů přičteš k Obraně? čím více, tím silnější tvůj štít bude\n")
    inteligence_dodatek = zadani_hodnot("Kolik bodů přičteš k Inteligenci? Důvtip by se neměl podceňovat\n")
    hlad_dodatek = zadani_hodnot("Kolik bodů přičteš k Poteřbě jíst? čím více, tím méně budeš muse jíst\n")
    print()
    celkem = zivot_dodatek + utok_dodatek + obrana_dodatek + inteligence_dodatek + hlad_dodatek

    if celkem < pokus_cislo:
        print("Nejspíš neumíš moc dobře, počítat, nějaké body ti ještě zbyly, zkus to znovu, ať to nemáš moc těžké")
    if celkem > pokus_cislo:
        pokus_cislo -= 1
        print(f"""Kdepak, podvádět se nevyplcí, říkal jsme ti, jen 10. Tobě to bylo málo co?
        tak teď už jich máš jen {pokus_cislo} """)
        print()

print("Povedlo se :)")
print()
time.sleep(2)

hrdina.jmeno = vlastni_jmeno
hrdina.zivoty += zivot_dodatek
hrdina.utok += utok_dodatek
hrdina.obrana += obrana_dodatek
hrdina.inteligence += inteligence_dodatek
hrdina.hlad += hlad_dodatek
hrdina.max_zivot += zivot_dodatek
hrdina.max_hlad += hlad_dodatek
print(hrdina)

time.sleep(2)
print()
print()
pokyny = ("""   Pohybujeme se stále, jen v příkazovém řádku, takže toho moc neumíš, ale máš následující možnosti:
Když stiskneš 1 - půjdeš hledat stopy do lesa 
Když stiskneš 2 - Podíváš se co máš v tlumoku a budeš moc něco použít
když stiskneš 3 - posuneš se zas o něco blíže k princezně
když stiskneš 4 - vypíšu ti tvoje aktulní zdraví a uroveň hladu. 
když stiskneš 5 - zopakuji ti tvé možnosti

Tak a teď už Vážně hurá za princeznou""")
print(pokyny)

vyhral_jsi = "ne"
pokrok = 0

while hrdina.je_nazivu() or vyhral_jsi == "ano":
    while True:
        try:
            print()
            volba = int(input("Tak co uděláme teď?\n"))
            break
        except ValueError:
            print("Už zas? říkam aby jsi zádavál jen celá čísla")

    if volba == 1:
        delka_chuze = float(input("""Na jak dlouho se chceš projít? Čím déle půjdeš, tím větší hlad budeš mit,
         ale můžeš najít zajímavější věci. Jedna jednotka procházky, zvýší tvůj hlad o jednu Jednotku 

         Můžeš jít o 1 jendnotku , o 3 jednotky, nebo až o 5 jednotky 

         Tak o kolik půjdeš? (1/3/5)\n"""))

        if delka_chuze == 1:
            udalosti.les1.prochazej_se()
            print(udalosti.les1)
            hrdina.jez()

        if delka_chuze == 3:
            udalosti.les2.prochazej_se()
            print(udalosti.les2)
            for z in range(3):
                hrdina.jez()

        if delka_chuze == 5:
            udalosti.les3.prochazej_se()
            print(udalosti.les3)
            for z in range(5):
                hrdina.jez()

    if volba == 2:
        hrdina.vypis_veci()
        pouzit = str(input("Chceš něco z toho použít? ano/ne\n")).lower()
        print()
        if pouzit == "ano":
            hrdina.pouzij()
        if pouzit == "ne":
            print("Tak jsi de podíval, a můžeme jít dál")
        # else:
        # print("Prosím, napiš jen ano nebo ne. Jinak nebudu vědět co mám dělat")

    if volba == 3:
        pokrok += 1
        if pokrok == 1:
            print(hlavni_dejova_linka.ukol1)
            hlavni_dejova_linka.ukol1.hadej()
        if pokrok == 2:
            print(hlavni_dejova_linka.ukol2)
            print()
            hlavni_dejova_linka.ukol2.hadej_hadanku()
        if pokrok == 3:
            print(hlavni_dejova_linka.ukol3)
            hlavni_dejova_linka.ukol3.kamen_nuzky_papir()
        if pokrok == 4:
            pass
        if pokrok == 5:
            pass
    if volba == 4:
        print(hrdina.graficky_zivot())
        print(hrdina.graficky_hlad())
    if volba == 5:
        print(pokyny)

if hrdina.je_nazivu():
    pass
else:
    print()
    print("Je mi líto, zemřel jsi ")