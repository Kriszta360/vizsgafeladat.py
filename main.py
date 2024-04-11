# Az alábbi Python kód egy olyan alapvető rendszert hoz létre, amely kezeli egy szálloda szobafoglalásait. Az osztályokat és a kód egy részét készítettem el, amely lehetővé teszi foglalások létrehozását, lemondását és listázását, valamint egy egyszerű felhasználói interfészt biztosít a különböző műveletek végrehajtásához.

import datetime

# Absztrakt Szoba osztály
class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

# EgyágyasSzoba osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(10000, szobaszam)

# KétagyasSzoba osztály
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(15000, szobaszam)

# Szálloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas_hozzaad(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                raise Exception('A szoba már foglalt ezen a napon.')
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szobaszam, datum, szoba.ar))
                return szoba.ar
        raise Exception('Nincs ilyen szobaszám.')

    def foglalas_torol(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return
        raise Exception('Nincs ilyen foglalás.')

    def foglalasok_listaz(self):
        return self.foglalasok

# Foglalás osztály
class Foglalas:
    def __init__(self, szobaszam, datum, ar):
        self.szobaszam = szobaszam
        self.datum = datum
        self.ar = ar

    def __str__(self):
        return f'Szobaszám: {self.szobaszam}, Dátum: {self.datum}, Ár: {self.ar}'

# Felhasználói interfész és adatvalidáció
def main():
    szalloda = Szalloda('CodeWay Hotel')
    szalloda.szoba_hozzaad(EgyagyasSzoba(101))
    szalloda.szoba_hozzaad(KetagyasSzoba(102))
    szalloda.szoba_hozzaad(EgyagyasSzoba(103))

    # Töltsd fel a rendszert 5 foglalással
    try:
        szalloda.foglalas_hozzaad(101, datetime.date(2024, 4, 10))
        szalloda.foglalas_hozzaad(102, datetime.date(2024, 4, 11))
        szalloda.foglalas_hozzaad(103, datetime.date(2024, 4, 12))
        szalloda.foglalas_hozzaad(101, datetime.date(2024, 4, 13))
        szalloda.foglalas_hozzaad(102, datetime.date(2024, 4, 14))
    except Exception as e:
        print(e)

    # Felhasználói interakciók
    while True:
        print("Üdvözöljük a Véndiófa Vendégházban!")
        print("1: Foglalások listáz")
        print("2: Foglalás")
        print("3: Lemondás")
        print("4: Kilépés")
        valasztas = input("Kérjük, válasszon egy opciót (1-4): ")


        if valasztas == '1':
            print("Az összes foglalás listázása:")
            for foglalas in szalloda.foglalasok_listaz():
                print(foglalas)

        if valasztas == '2':
            try:
                szobaszam = int(input("Adja meg a szobaszámot: "))
                ev = int(input("Adja meg az évet (pl. 2024): "))
                honap = int(input("Adja meg a hónapot (1-12): "))
                nap = int(input("Adja meg a napot (1-31): "))
                datum = datetime.date(ev, honap, nap)

                if datum <= datetime.date.today():
                    raise Exception("A foglalás dátuma nem lehet a múltban.")
                ar = szalloda.foglalas_hozzaad(szobaszam, datum)
                print(f"A foglalás sikeresen létrejött. Az ár: {ar} Ft.")
            except Exception as e:
                print(e)

        elif valasztas == '3':
            try:
                szobaszam = int(input("Adja meg a szobaszámot: "))
                ev = int(input("Adja meg az évet (pl. 2024): "))
                honap = int(input("Adja meg a hónapot (1-12): "))
                nap = int(input("Adja meg a napot (1-31): "))
                datum = datetime.date(ev, honap, nap)
                szalloda.foglalas_torol(szobaszam, datum)
                print("A foglalás sikeresen lemondva.")
            except Exception as e:
                print(e)

        elif valasztas == '4':
            print("Kilépés a programból.")
            break

        else:
            print("Érvénytelen opció, kérem próbálja újra!")

# Program indítása
if __name__ == '__main__':
    main()