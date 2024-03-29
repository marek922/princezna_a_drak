import sqlite3
from hlavni_dejova_linka import zadani_hodnot
class Databaze:
    def nejlepsich_deset_podle_urovne(self,obtiznost): #vypíše deset nejlepších hráčů s danou obtížností
        self.obtiznost = obtiznost
        conn = sqlite3.connect('nejlepsi_skore.db')
        cur = conn.cursor()
        cur.execute("""SELECT jmeno, minuty, vteriny, utok, obrana, zivoty FROM vyherci
                                    WHERE vysledek = 'Vyhra' AND obtiznost = ? ORDER BY minuty, vteriny, zivoty DESC, utok DESC, obrana DESC LIMIT 10""",
                    (self.obtiznost,))
        results = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM vyherci WHERE obtiznost = ?", (self.obtiznost,))
        pocet_her = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM vyherci WHERE vysledek = 'Vyhra' AND obtiznost = ?", (self.obtiznost,))
        pocet_vitezstvi = cur.fetchone()[0]
        print(f"Top 10 hráčů s obtížností {self.obtiznost}:")
        for index, row in enumerate(results, start=1):
            jmeno, minuty, vteriny, utok, obrana, zivoty = row
            print(
                f"{index}. {jmeno}: {minuty} minut {vteriny} sekund, Útok: {utok}, Obrana: {obrana}, Zbylé životy: {zivoty}")
        print()
        print(f"Celkový počet odehraných her: {pocet_her}")
        print(f"Celkový počet vítězných her: {pocet_vitezstvi}")
        if pocet_her>0:
            print(f"Průměrná úspěšnost je {((pocet_vitezstvi / pocet_her) * 100):.2f}%")



        conn.commit()
        conn.close()

    def smazat_data_z_tabulky(self): # vymaže všechny data z tabulky
        conn = sqlite3.connect('nejlepsi_skore.db')
        cur = conn.cursor()
        sql_dotaz = f"DELETE FROM vyherci"
        cur.execute(sql_dotaz)
        conn.commit()
        conn.close()

    def smazat_data_podle_jmena(self,jmeno): #vymaža data podle zadaného jmnéna
        conn = sqlite3.connect('nejlepsi_skore.db')
        cur = conn.cursor()
        sql_dotaz = f"DELETE FROM vyherci WHERE jmeno = ?"
        cur.execute(sql_dotaz, (jmeno,))
        conn.commit()
        conn.close()

    def smazat_data_z_tabulky_podle_obtiznosti(self, obtiznost):#smaže data podle zadané obtížnosti
        conn = sqlite3.connect('nejlepsi_skore.db')
        cur = conn.cursor()
        sql_dotaz = f"DELETE FROM vyherci WHERE obtiznost = ?"
        cur.execute(sql_dotaz, (obtiznost,))
        conn.commit()
        conn.close()

databeze=Databaze()


volba=6
uprava_databaze=input("Pro spuštění programu, stiskni Enter") # pokud hráč po spuštění programu nezmačkne anter, ale zadá slovo databaze tak se spustí rozhraní pro upravu databaze
if uprava_databaze == "databaze":
    while volba!=5:
        volba=zadani_hodnot(" pro vypis zadej 1 / pro smazani podle jmena zadej 2/ pro smazaní dat zadej 3 / pro smazani dat podle obtiznosti 4 / konec 5\n",1,5)
        if volba==1:
            for a in range(3):
                databeze.nejlepsich_deset_podle_urovne(a+1)
                print()
        if volba==2:
            jmeno=input("zadej hráče, kterého chceš smazat ")
            databeze.smazat_data_podle_jmena(jmeno)
            print()
        if volba==3:
            databeze.smazat_data_z_tabulky()
        if volba==4:
            obtiznost=zadani_hodnot("Zadej číslo urovně, kterou chceš smazat... 1 až 3...",1,3)
            databeze.smazat_data_z_tabulky_podle_obtiznosti(obtiznost)
            print()
        if volba==5:
            print("uprava dokončena")
