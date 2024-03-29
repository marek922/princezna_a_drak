from scenar import Princezna_a_drak
from hlavni_dejova_linka import zadani_hodnot
import prace_s_databazi

print("=" * 80 + "\n")
print(""" Vítám tě v cestě na dobrodružstvím. \n""")
print("=" * 80 + "\n")

volba=5

while volba!=4: #uvodní rozhraní hry
    volba=zadani_hodnot(""" --- Jestli chceš zažít život hrdiny, zvol 1  --- 
 --- Jestli tě spíše zajímá, kdo je tady největší hrdina, zvol 2 --- 
 --- Pokud tě zajímá, kdo dobrodružství napsat, zvol 3 --- 
 --- Pro ukončení a návrat do relity zadej 4 --- \n""",1,4)
    if volba==1: #spustí samotnou hru
        hra=Princezna_a_drak()
        hra.hraj()
    if volba==2: #vypíše seznam nejlepších
        for a in range (3):
            prace_s_databazi.databeze.nejlepsich_deset_podle_urovne(a+1)
            print()

    if volba==3: #vypíše titulky
        print(""" Vytvořil Marek Kykal za pomoci rekvalifikačního kurzu ITnetwork \n""")

print("Díky moc a zas brzo na viděnou")