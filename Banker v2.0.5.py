# UPDATE 2.0 
#✔ NOWE GUI
#✔ Bugfix
#✔ 

#Banker 12/05/2025 18:24
#UPDATE: 2.1.5

#DC : Nie Długo
#INFO: https://github.com/Lllightt/Banker/tree/Versions

import random

Login = str(input("Podaj Login: "))
Pin = int(input("Podaj Pin: "))
PrawLogin = "Fajne"
PrawPin = 1646
Pensja = 1
konto = 1000
LVL = 0
czas = 0

# FIRMA ZMIENNE
firma_owned = False
firma_Popularity = 1


#CENY ULEPSZEN
Cena_Upgrade_1 = 200
Cena_Upgrade_2 = 450
Cena_Upgrade_3 = 1150


if PrawLogin == Login and PrawPin == Pin:
    print("Zalogowano")
    while True:
        czas += 1
        cena_firmy = firma_Popularity * Pensja * firma_Popularity * 3

        print("\n﹄| MENU |﹃")
        print(" ")
        print("1. Zarabiaj           |$|")
        print("2. Sprawdź stan konta |$|")
        print("3. Wypłać             |$|")
        print("4. Kup Edukację")
        print("5. Sprawdź Level")
        print("6. Kup Bitcoin | LVL 30+ | |8000-10000 zł| |$|")
        print("...........")
        print("Strona 2. Przejdź na następną stronę")
        print(" ")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            zarobek = Pensja * (LVL * 2 if LVL > 0 else 1)

            if firma_owned:
                zarobek_firmy = firma_Popularity * 10
                zarobek += zarobek_firmy
                print(f"Zarobek z firmy: {zarobek_firmy} zł")

            konto += zarobek
            print(f" ✔ Dodano {zarobek} zł. Nowy stan konta: {konto} zł.")

        elif wybor == "2":
            print(f"Aktualny stan konta: {konto} zł.")

        elif wybor == "3":
            try:
                wyplata = int(input("Ile chcesz wypłacić? "))
                if wyplata > konto:
                    print("✘ Nie masz tylu pieniędzy na koncie. ✘")
                else:
                    konto -= wyplata
                    print(f" ✔ Wypłacono {wyplata} zł. Pozostało: {konto} zł.")
            except ValueError:
                print("Wprowadź poprawną liczbę.")

        elif wybor == "4":
            print("\n╭-  MENU EDUKACJI -╯")
            print(" ")
            print("1. Harvard  | 100k tys | | +15 LVL |☆ ")
            print("2. Stanford | 10k tys  | | +10 LVL |✧")
            print("3. Batory   | 1k tys   | | +5 LVL |")
            print("4. Zagle    | 100 tys  | | +1 LVL |")
            print("............")
            print("5. Wyjdz")
            print(" ")
            szkolenie = input("Wybierz opcję: ")

            if szkolenie == "5":
                print("Wyjście")
            elif szkolenie == "1" and konto >= 100000:
                konto -= 100000
                LVL += 15
                print(f" ✔ Kupiłeś Harvard. Masz teraz LVL: {LVL}. Pozostało: {konto} zł.")
            elif szkolenie == "2" and konto >= 10000:
                konto -= 10000
                LVL += 10
                print(f" ✔ Kupiłeś Stanford. Masz teraz LVL: {LVL}. Pozostało: {konto} zł.")
            elif szkolenie == "3" and konto >= 1000:
                konto -= 1000
                LVL += 5
                print(f" ✔ Kupiłeś Batory. Masz teraz LVL: {LVL}. Pozostało: {konto} zł.")
            elif szkolenie == "4" and konto >= 100:
                konto -= 100
                LVL += 1
                print(f" ✔ Kupiłeś Zagle. Masz teraz LVL: {LVL}. Pozostało: {konto} zł.")
            else:
                print(" ✘ Nie masz wystarczająco pieniędzy lub wybrałeś złą opcję. ✘")

        elif wybor == "5":
            print(f"Aktualny Level: {LVL} Poziom")


#KUPNO BITCOIN
        elif wybor == "6" and LVL >= 30:
            cena_bitcoin = random.randint(8000, 10000)
            bitcoin = random.randint(1, 50000)
            print(f"Cena Bitcoina: {cena_bitcoin} zł")
            print(f"Masz {konto} zł")

            if konto >= cena_bitcoin:
                decyzja = input("Chcesz kupić? (tak/nie): ").lower()
                if decyzja == "tak":
                    konto -= cena_bitcoin
                    print(f" ✔ Kupiłeś Bitcoina. Możesz go sprzedać za: {bitcoin} zł.")
                    decyzja_sprzedaz = input("Sprzedać teraz? (tak/nie): ").lower()
                    if decyzja_sprzedaz == "tak":
                        konto += bitcoin
                        print(f" ✔ Sprzedano. Nowy stan konta: {konto} zł.")
                    else:
                        print(" ✘ Zatrzymano Bitcoina (nie sprzedano). ✘")
                else:
                    print(" ✘ Nie kupiłeś Bitcoina ✘")
            else:
                print("✘ Nie masz wystarczająco pieniędzy ✘")
#KONIEC

#STRONA 2
        elif wybor.lower() == "strona 2":
            print(" ")
            print("﹄| STRONA 2/2 |﹃")
            print(" ")
            print("7. Kody")
            print("8. Menu Firmy")
            print("..........")
            print("Powrót. Idzie do menu głównego")
            print(" ")
            Wybor2 = input("Wybierz opcję: ").lower()

            if Wybor2 == "7":
                print("Kody są od developera lub z losowych przyczyn.")
                KodWpisany = input("Kod: ")
                if KodWpisany == "IoG":
                    LVL += 0
                    konto += 10
                    print("Dano +0 LVL i 10 zł")
                    print(f"Teraz masz {LVL} LVL, {konto} zł")
                    print("Tego kodu możesz używać ile chcesz")
                else:
                    print("✘ Kod Nieprawidłowy ✘")

            elif Wybor2 == "powrót":
                print("Powrócono")

            elif Wybor2 == "8":
                print(" ")
                print("--MENU FIRMY--")
                print(" ")
                print("1. Kup Firmę | 399 zł | |$|")
                print("2. Ulepsz Firmę |  200+ zł | |$|")
                print("3. Sprzedaj Firmę")
                print(" ")
                FirmaChoose = input("Wybierz opcję: ")

                if FirmaChoose == "1":
                    if konto >= 399:
                        konto -= 399
                        firma_owned = True
                        print(f"✔ Kupiłeś Firmę!! Teraz możesz ją ulepszać.")
                    else:
                        print(" ✘ Nie masz wystarczająco pieniędzy. ✘ ")

                elif FirmaChoose == "2" and firma_owned:
                    print(" ")
                    print(f"Plan 1 - | {Cena_Upgrade_1} | | + 1 Popularnośći FIRMY | ")
                    print(f"Plan 2 - | {Cena_Upgrade_2} | | + 3 Popularnośći FIRMY | ")
                    print(f"Plan 3 - | {Cena_Upgrade_3} | | + 5 Popularnośći FIRMY | ")
                    print(" ")
                    WybierzPlan = input("Wybierz plan: ").lower()

                    if WybierzPlan == "plan 1" and  konto >= Cena_Upgrade_1:
                        konto -= Cena_Upgrade_1
                        firma_Popularity += 1
                        Cena_Upgrade_1 = int(Cena_Upgrade_1 * 2)
                        print("✔ Kupiono plan 1")
                    elif WybierzPlan == "plan 2" and  konto >= Cena_Upgrade_2:
                        konto -= Cena_Upgrade_2
                        firma_Popularity += 3
                        Cena_Upgrade_2 = int(Cena_Upgrade_2 * 2)
                        print("✔ Kupiono plan 2")
                    elif WybierzPlan == "plan 3" and  konto >= Cena_Upgrade_3:
                        konto -= Cena_Upgrade_3
                        firma_Popularity += 5
                        Cena_Upgrade_3 = int(Cena_Upgrade_3 * 2)
                        print("✔ Kupiono plan 3")
                    else:
                        print("✘ Zła odpowiedź lub nie masz pieniędzy. ✘")
                    print(f"Popularność firmy: {firma_Popularity}, LVL: {LVL}, Konto: {konto} zł.")

                elif FirmaChoose == "3":
                    print(f"Twoja Firma jest warta {cena_firmy} zł. Czy chcesz sprzedać?")
                    Wybierz = input("Sprzedać? Tak/Nie ").lower()
                    if Wybierz == "tak":
                        konto += cena_firmy
                        firma_owned = False
                        firma_Popularity = 1
                        print(f" ✔ Sprzedano firmę za {cena_firmy} zł.")
                    elif Wybierz == "nie":
                        print("✘ Nie sprzedano firmy. ✘")
                    else:
                        print("✘ Nieprawidłowa odpowiedź. ✘")
                else:
                    print("✘ Nieprawidłowa opcja, spróbuj ponownie ✘")
            else:
                print("✘ Nieprawidłowa opcja, spróbuj ponownie ✘")
#KONIEC
        else:
            print("✘ Nieprawidłowa opcja, spróbuj ponownie ✘")
else:
    print("✘ Nieprawidłowy login lub PIN. ✘")