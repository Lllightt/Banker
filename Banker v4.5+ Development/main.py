
import tkinter as tk
from tkinter import messagebox
import random
import pygame
import sys
import os
import threading
import time
import json
ostatnia_muzyka = None


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Urzycie:
sciezka_muzyka = resource_path("Muzyka/plik_muzyczny.mp3")
sciezka_efekt = resource_path("Efekty/efekt_dzwiekowy.wav")

# GAME
PrawLogin = "Fajne"
PrawPin = 1646
Pensja = 1
konto = 1000
LVL = 0
czas = 0
# ZMIENNE
firma_owned = False
firma_Popularity = 1
Cena_Upgrade_1 = 1000
Cena_Upgrade_2 = 1450
Cena_Upgrade_3 = 5670
secretcode = random.randint(1,99999)
#MINERALY
# zloto = random.randint(1,50948)
# posiadane_zloto = 0
posiadane_zloto = 0
posiadane_srebro = 0
posiadane_diament = 0
# posiadane_srebro = 0
# diament = random.randint(1,500000)
# posiadane_diament = 0
#PODATKI
randPodatek = random.randint(100000,1000000)
Podatek = randPodatek
Podatek_Zaplacony = False

# SAVE JSON
save_plik = "save.json"
##########

def zapisz_gre():
    dane = {
        "konto": konto,
        "LVL": LVL,
        "czas": czas,
        "posiadane_zloto": posiadane_zloto,
        "posiadane_srebro": posiadane_srebro,
        "posiadane_diament": posiadane_diament,
        "firma_owned": firma_owned,
        "firma_Popularity": firma_Popularity,
        "Podatek": Podatek,
        "Podatek_Zaplacony": Podatek_Zaplacony
    }
    with open(save_plik, "w") as f:
        json.dump(dane, f)
    messagebox.showinfo("Zapis", "✔ Gra zapisana!")
def load_game():
    global konto, LVL, czas, posiadane_zloto, posiadane_srebro, posiadane_diament
    global firma_owned, firma_Popularity, Podatek, Podatek_Zaplacony

    if os.path.exists(save_plik):
        with open(save_plik, "r") as f:
            dane = json.load(f)
        konto = dane["konto"]
        LVL = dane["LVL"]
        czas = dane["czas"]
        posiadane_zloto = dane["posiadane_zloto"]
        posiadane_srebro = dane["posiadane_srebro"]
        posiadane_diament = dane["posiadane_diament"]
        firma_owned = dane["firma_owned"]
        firma_Popularity = dane["firma_Popularity"]
        Podatek = dane["Podatek"]
        Podatek_Zaplacony = dane["Podatek_Zaplacony"]
        messagebox.showinfo("Wczytano", "✔ Gra wczytana!")
    else:
        messagebox.showerror("Błąd", "❌ Brak zapisu gry.")
def odtworz_muzyke():
    global Podatek,konto
    try:
        pygame.mixer.init()
        if konto >= (Podatek / 2):
            pygame.mixer.music.load("Muzyka/Almost.mp3")
        else:
            pygame.mixer.music.load("Muzyka/muzyka.mp3")
        pygame.mixer.music.play(-1)
    except Exception as e:
        messagebox.showwarning("Muzyka", f"Nie udało się odtworzyć muzyki:\n{e}")

codes = [
    "IoG",
    "BankerGUI",
    "Banker3.0"
]
def start_game():
    #infoupdate = messagebox.showinfo("UPDATE 4.0","Dziękuję za pobranie Banker w tym update zostały dodane nowe funkcje i poprawione błędy jak: Muzyka,Efekty,Minerały,Koniec Gry")
    loginsound = pygame.mixer.Sound("Efekty/login.mp3")
    login = loginentry.get()
    try:
        pin = int(pinentry.get())
    except ValueError:
        messagebox.showerror("Błąd", "PIN musi być liczbą.")
        return

    if login == PrawLogin and pin == PrawPin:
        login_window.destroy()
        open_main_menu()
        loginsound.play()
    else:
        messagebox.showerror("Błąd logowania", "✘ Nieprawidłowy login lub PIN ✘")

def open_main_menu():
    game = tk.Tk()
    game.title("Banker Menu")
    game.geometry("600x500")
    game.config(bg="#8ebcff")
    

    output = tk.Label(game, text="", fg="Black", font=("Fixedsys", 24), wraplength=500)
    output.pack(pady=10)

    def zarabiaj():
        global konto, czas
        klik = pygame.mixer.Sound("Efekty/kupno.mp3")
        czas += 1
        zarobek = Pensja * (LVL * 2 if LVL > 0 else 1)
        klik.play()
        if firma_owned:
            zarobek += firma_Popularity * 10
        konto += zarobek
        output.config(text=f"✔ Zarobiono {zarobek} zł. Konto: {konto} zł")

    def pokaz_konto():
        output.config(text=f"💰 Konto: {konto} zł")

    def pokaz_lvl():
        output.config(text=f"📈 Level: {LVL}")
#Edukacja
    def open_edukacja():
        edu = tk.Toplevel()
        edu.title("Edukacja")
        edu.geometry("400x300")
        edu.config(bg="#abeb83")

        def kup(cena, lvl_bonus, nazwa):
            global konto, LVL
            if konto >= cena:
                konto -= cena
                LVL += lvl_bonus
                messagebox.showinfo("✔ Edukacja", f"Kupiłeś {nazwa}. Nowy LVL: {LVL}")
                levelup = pygame.mixer.Sound("Efekty/levelup.mp3")
                levelup.play()
            else:
                messagebox.showerror("✘ Błąd", "✘ Za mało pieniędzy.")

        tk.Button(edu, bg="#68a840", font=("PT Sans", 24), text="Harvard (250k, +15 LVL)", command=lambda: kup(250000, 15, "Harvard")).pack(pady=5)
        tk.Button(edu,  bg="#68a840", font=("PT Sans", 24), text="Stanford (15k, +10 LVL)", command=lambda: kup(15000, 10, "Stanford")).pack(pady=5)
        tk.Button(edu,  bg="#68a840", font=("PT Sans", 24),text="Batory (5k, +5 LVL)", command=lambda: kup(5000, 5, "Batory")).pack(pady=5)
        tk.Button(edu,  bg="#68a840", font=("PT Sans", 24), text="Zagle (500, +1 LVL)", command=lambda: kup(500, 1, "Zagle")).pack(pady=5)
#koniec
#bitcoin
    def pokaz_bitcoin():
        error = pygame.mixer.Sound("Efekty/error.mp3")
        global konto
        if LVL < 30:
            error.play()
            output.config(text="Musisz mieć co najmniej LVL 30 by kupić Bitcoin.")
            return
        cena_bitcoin = random.randint(8000, 10000)
        bitcoin = random.randint(1, 13999)
        if konto >= cena_bitcoin:
            if messagebox.askyesno("Bitcoin", f"Cena Bitcoina to {cena_bitcoin} zł. Kupujesz?"):
                konto -= cena_bitcoin
                if messagebox.askyesno("Sprzedaż", f"Sprzedać za {bitcoin} zł?"):
                    konto += bitcoin
                    output.config(text=f"✔ Sprzedano za {bitcoin} zł. Konto: {konto} zł")
                else:
                    output.config(text="✔ Zakupiono Bitcoina, ale nie sprzedano.")
        else:
            error.play()
            output.config(text="✘ Za mało pieniędzy.")
#koniec
#Strona 2
    def open_page2():
        page2sound = pygame.mixer.Sound("Efekty/page2.mp3")
        page2 = tk.Toplevel(game)
        page2sound.play()
        page2.title("Strona 2")
        page2.geometry("400x300")
        page2.config(bg="#f5b0b0")
        def open_codes():
            global codes
            pagecode = tk.Toplevel(page2)
            pagecode.title("Kody")
            pagecode.geometry("400x300")
            pagecode.config(bg="#fff194")
            kod_wpis = tk.Entry(pagecode)
            if kod_wpis in codes:
                messagebox.showinfo("✔", "Kod jest poprawny!")
                codes
        def open_Podatki():
            global Podatek, Wzrost_Podatki,Podatek_Zaplacony
            Podatki_main = tk.Toplevel(page2)
            Podatki_main.title("Podatki")
            Podatki_main.geometry("400x300")
            Podatki_main.config(bg="#f4b0f5")
            Frame_Podatki = tk.Frame(Podatki_main, bg="#f4b0f5", width=300, height= 200)
            Frame_Podatki.place(width=800,height=700)
            Frame_Podatki.pack(pady=10)
            def sprawdz_podatek():
                global Podatek, Wzrost_Podatki, konto,Podatek_Zaplacony
                messagebox.showerror("INFO:", f"Masz do zapłacenia {Podatek} zł")
            def zaplac_podatek():
                global Podatek, Wzrost_Podatki, konto,Podatek_Zaplacony
                if konto >= Podatek:
                    konto -= Podatek
                    Podatek = 0
                    Wzrost_Podatki = 1
                    Podatek_Zaplacony = True
                    def zmien_muzyke():
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Muzyka/GameCompletion.mp3")
                        pygame.mixer.music.play(1)
                    zmien_muzyke()
                    messagebox.showinfo(f"Podatki",f"Pokonałeś Grę Wyślij na discord kod: BANKERKONIEC{secretcode}")
                    

                else:
                    messagebox.showerror("✘ Błąd", "✘ Za mało pieniędzy.")
            tk.Button(Frame_Podatki, text="Sprawdz Podatki", command=sprawdz_podatek,bg="#b96cba", font=("Fixedsys", 24)).pack(pady=10)
            tk.Button(Frame_Podatki, text="Zapłać Podatki", command=zaplac_podatek,bg="#b96cba", font=("Fixedsys", 24)).pack(pady=10)
        def koniec_gry():
            global Podatek, Podatek_Zaplacony,secretcode
            if Podatek_Zaplacony == True:
                messagebox.showinfo(f"Podatki",f"Pokonałeś Grę Wyślij na discord kod: BANKERKONIEC{secretcode}")
#MATERIALY                
        def kupno_mineraly():
            
            main_mineral = tk.Toplevel(page2)
            main_mineral.title("Minerały")
            main_mineral.geometry("400x400")
            main_mineral.config(bg="#e8ae82")
            #LABELE
            label_zloto = tk.Label(main_mineral,text=f"Posiadane Złoto: {posiadane_zloto} zł",fg="Black", font=("Fixedsys", 24), wraplength=500)
            label_zloto.pack(pady=5)
            label_srebro = tk.Label(main_mineral,text=f"Posiadane Srebro: {posiadane_srebro} zł",fg="Black", font=("Fixedsys", 24), wraplength=500)
            label_srebro.pack(pady=5)
            label_diament = tk.Label(main_mineral,text=f"Posiadane Diamenty: {posiadane_diament} zł",fg="Black", font=("Fixedsys", 24), wraplength=500)
            label_diament.pack(pady=5)
            def kupno_zlota():
                zloto = random.randint(1,50948)
                kupno_window = tk.Toplevel(main_mineral)
                kupno_window.geometry("600x400")
                kupno_window.config(bg="#f5f542")
                kupno_window.title("KUPNO ZLOTA")
                tk.Label(kupno_window,text=f"Złoto teraz kosztuję: {zloto} zł za 1 Gram",fg="Black", font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                tk.Label(kupno_window,text=f"Wpisz ile złota chcesz kupić",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                Kupno_Entry = tk.Entry(kupno_window,font=("Fixedsys", 24))
                Kupno_Entry.pack(pady=5)
                def Paragon():
                    ile_kupic = int(Kupno_Entry.get())
                    cena1 = zloto * ile_kupic
                    paragon_fram = tk.Toplevel(kupno_window)
                    paragon_fram.title("Paragon")
                    paragon_fram.geometry("600x500")
                    paragon_fram.config(bg="#ffffff")
                    def Potwierdz():
                        cena = zloto * ile_kupic
                        global konto,posiadane_zloto
                        if konto >= cena:
                            konto -= cena
                            posiadane_zloto += cena
                            messagebox.showinfo("Potwierdzenie", f"Kupiono {ile_kupic} Gram złota za {cena} zł")
                            paragon_fram.destroy()
                        else:
                            messagebox.showerror("Błąd", "Niewystarczające środki na koncie!")
                    def JednakNie():
                        messagebox.showinfo("Anulowano", "Nie dokonano zakupu")
                        paragon_fram.destroy()
                    

                    tk.Label(paragon_fram,text="POTWIERDZENIE PŁATNOŚCI",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    tk.Label(paragon_fram,text=f"Czy chcesz kupić {ile_kupic} Gram złota za:",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    tk.Label(paragon_fram,text=f"{cena1} zł?",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    Yes = tk.Button(paragon_fram, text="Tak", command=Potwierdz,fg="Black",bg="#ffffff", font=("Fixedsys", 24)).pack(pady=2)
                    No = tk.Button(paragon_fram, text="Nie", command=JednakNie,fg="Black",bg="#ffffff", font=("Fixedsys", 24)).pack(pady=2)
                tk.Button(kupno_window, text="Kup", command=Paragon,bg="#faed3c", font=("Fixedsys", 24)).pack(pady=5)
            def kupno_srebra():
                srebro = random.randint(1,10000)
                kupno_window = tk.Toplevel(main_mineral)
                kupno_window.geometry("600x400")
                kupno_window.config(bg="#d3d3d3")
                kupno_window.title("KUPNO SREBRA")
                tk.Label(kupno_window,text=f"Srebro teraz kosztuję: {srebro} zł za 1 Gram",fg="Black", font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                tk.Label(kupno_window,text=f"Wpisz ile Srebra chcesz kupić",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                Kupno_Entry = tk.Entry(kupno_window,font=("Fixedsys", 24))
                Kupno_Entry.pack(pady=5)
                def Paragon():
                    ile_kupic = int(Kupno_Entry.get())
                    cena1 = srebro * ile_kupic
                    paragon_fram = tk.Toplevel(kupno_window)
                    paragon_fram.title("Paragon")
                    paragon_fram.geometry("600x500")
                    paragon_fram.config(bg="#ffffff")
                    def Potwierdz():
                        cena = srebro * ile_kupic
                        global konto,posiadane_srebro
                        if konto >= cena:
                            konto -= cena
                            cena += posiadane_srebro
                            messagebox.showinfo("Potwierdzenie", f"Kupiono {ile_kupic} Gram srebra za {cena} zł")
                            paragon_fram.destroy()
                        else:
                            messagebox.showerror("Błąd", "Niewystarczające środki na koncie!")
                    def JednakNie():
                        messagebox.showinfo("Anulowano", "Nie dokonano zakupu")
                        paragon_fram.destroy()
                    tk.Label(paragon_fram,text="POTWIERDZENIE PŁATNOŚCI",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    tk.Label(paragon_fram,text=f"Czy chcesz kupić {ile_kupic} Gram złota za:",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    tk.Label(paragon_fram,text=f"{cena1} zł?",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    Yes = tk.Button(paragon_fram, text="Tak", command=Potwierdz,fg="Black",bg="#ffffff", font=("Fixedsys", 24)).pack(pady=2)
                    No = tk.Button(paragon_fram, text="Nie", command=JednakNie,fg="Black",bg="#ffffff", font=("Fixedsys", 24)).pack(pady=2)
                tk.Button(kupno_window, text="Kup", command=Paragon,bg="#faed3c", font=("Fixedsys", 24)).pack(pady=5)

            def kupno_diament():
                Diament = random.randint(1,100000)
                kupno_window = tk.Toplevel(main_mineral)
                kupno_window.geometry("600x400")
                kupno_window.config(bg="#d3d3d3")
                kupno_window.title("KUPNO DIAMENTU")
                tk.Label(kupno_window,text=f"Diament teraz kosztuję: {Diament} zł za 1 Gram",fg="Black", font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                tk.Label(kupno_window,text=f"Wpisz ile Diamentu chcesz kupić",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                Kupno_Entry = tk.Entry(kupno_window,font=("Fixedsys", 24))
                Kupno_Entry.pack(pady=5)
                def Paragon():
                    ile_kupic = int(Kupno_Entry.get())
                    cena1 = Diament * ile_kupic
                    paragon_fram = tk.Toplevel(kupno_window)
                    paragon_fram.title("Paragon")
                    paragon_fram.geometry("600x500")
                    paragon_fram.config(bg="#ffffff")
                    def Potwierdz():
                        cena = Diament * ile_kupic
                        global konto,posiadane_diament
                        if konto >= cena:
                            konto -= cena
                            posiadane_diament += cena
                            messagebox.showinfo("Potwierdzenie", f"Kupiono {ile_kupic} Gram srebra za {cena} zł")
                            paragon_fram.destroy()
                        else:
                            messagebox.showerror("Błąd", "Niewystarczające środki na koncie!")
                    def JednakNie():
                        messagebox.showinfo("Anulowano", "Nie dokonano zakupu")
                        paragon_fram.destroy()
                    

                    tk.Label(paragon_fram,text="POTWIERDZENIE PŁATNOŚCI",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    tk.Label(paragon_fram,text=f"Czy chcesz kupić {ile_kupic} Gram srebra za:",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    tk.Label(paragon_fram,text=f"{cena1} zł?",fg="Black",font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                    Yes = tk.Button(paragon_fram, text="Tak", command=Potwierdz,fg="Black",bg="#ffffff", font=("Fixedsys", 24)).pack(pady=2)
                    No = tk.Button(paragon_fram, text="Nie", command=JednakNie,fg="Black",bg="#ffffff", font=("Fixedsys", 24)).pack(pady=2)
                    tk.Button(kupno_window, text="Kup", command=Paragon,bg="#faed3c", font=("Fixedsys", 24)).pack(pady=5)        
                tk.Button(kupno_window, text="Kup", command=Paragon,bg="#faed3c", font=("Fixedsys", 24)).pack(pady=5)

                
                
            tk.Button(main_mineral, text="Kup Zloto", command=kupno_zlota,bg="#cf7938", font=("Fixedsys", 24)).pack(pady=5)
            tk.Button(main_mineral, text="Kup Srebro", command=kupno_srebra,bg="#cf7938", font=("Fixedsys", 24)).pack(pady=5)
            tk.Button(main_mineral, text="Kup Diamenty", command=kupno_diament,bg="#cf7938", font=("Fixedsys", 24)).pack(pady=5)


        def firma_menu():
            firma_win = tk.Toplevel(page2)
            firma_win.title("Firma Menu")
            firma_win.geometry("400x400")
            firma_win.config(bg="#e8ae82")

            def kup_firme():
                global konto, firma_owned
                if konto >= 399:
                    konto -= 399
                    firma_owned = True
                    messagebox.showinfo("Sukces", "✔ Kupiłeś Firmę!")
                else:
                    messagebox.showerror("Błąd", "✘ Za mało pieniędzy.")
            # FIRMA ULEPSZ
            def ulepsz_firme():
                global konto, firma_Popularity, Cena_Upgrade_1, Cena_Upgrade_2, Cena_Upgrade_3
                plans = {
                    "Plan 1": (Cena_Upgrade_1, 1),
                    "Plan 2": (Cena_Upgrade_2, 3),
                    "Plan 3": (Cena_Upgrade_3, 5),
                }
                for name, (cena, bonus) in plans.items():
                    if messagebox.askyesno("Ulepsz Firmę", f"{name}: {cena} zł za +{bonus} Popularności"):
                        if konto >= cena:
                            konto -= cena
                            firma_Popularity += bonus
                            if name == "Plan 1":
                                Cena_Upgrade_1 *= 2.6
                            elif name == "Plan 2":
                                Cena_Upgrade_2 *= 2.8
                            elif name == "Plan 3":
                                Cena_Upgrade_3 *= 3
                            messagebox.showinfo("Sukces", f"✔ Ulepszono firmę. Popularność: {firma_Popularity}")
                        else:
                            messagebox.showerror("Błąd", "✘ Za mało pieniędzy.")
                        break
            # SPRZEDAWANIE FIRMY
            def sprzedaj_firme():
                global konto, firma_owned, firma_Popularity
                cena = firma_Popularity * Pensja * firma_Popularity * 30
                if messagebox.askyesno("Sprzedaż Firmy", f"Sprzedać za {cena} zł?"):
                    konto += cena
                    firma_owned = False
                    firma_Popularity = 1
                    messagebox.showinfo("Sukces", f"✔ Sprzedano za {cena} zł.")

            tk.Button(firma_win, text="Kup Firmę (399 zł)", command=kup_firme,bg="#cf7938", font=("Fixedsys", 24)).pack(pady=5)
            tk.Button(firma_win, text="Ulepsz Firmę", command=ulepsz_firme,bg="#cf7938", font=("Fixedsys", 24)).pack(pady=5)
            tk.Button(firma_win, text="Sprzedaj Firmę", command=sprzedaj_firme,bg="#cf7938", font=("Fixedsys", 24)).pack(pady=5)

        tk.Button(page2, text="Kody", command=open_codes,bg="#e88282", font=("Fixedsys", 24)).pack(pady=10)
        tk.Button(page2, text="Menu Firmy", command=firma_menu,bg="#e88282", font=("Fixedsys", 24)).pack(pady=10)
        tk.Button(page2, text="Podatki", command=open_Podatki,bg="#e88282", font=("Fixedsys", 24)).pack(pady=10)
        tk.Button(page2, text="Minerały", command=kupno_mineraly,bg="#e88282", font=("Fixedsys", 24)).pack(pady=10)
        tk.Button(page2, text="Ukończ Grę", command=koniec_gry,bg="#e88282", font=("Fixedsys", 24)).pack(pady=10)



    tk.Button(game, text="1. Zarabiaj", command=zarabiaj, width=30, bg="#565cba", font=("Fixedsys", 24)).pack(pady=5)
    tk.Button(game, text="2. Stan konta", command=pokaz_konto, width=30,bg="#565cba", font=("Fixedsys", 24)).pack(pady=5)
    tk.Button(game, text="3. LVL", command=pokaz_lvl, width=30,bg="#565cba", font=("Fixedsys", 24)).pack(pady=5)
    tk.Button(game, text="4. Edukacja", command=open_edukacja, width=30,bg="#565cba", font=("Fixedsys", 24)).pack(pady=5)
    tk.Button(game, text="5. Bitcoin (LVL 30+)", command=pokaz_bitcoin, width=30,bg="#565cba",font=("Fixedsys", 24)).pack(pady=5)
    tk.Button(game, text="➡ Strona 2", command=open_page2, width=30,bg="#565cba",font=("Fixedsys", 24)).pack(pady=20)
    tk.Button(game, text="💾 Zapisz grę", command=zapisz_gre, width=30, bg="#565cba", font=("Fixedsys", 20)).pack(pady=5)
    tk.Button(game, text="📂 Wczytaj grę", command=load_game, width=30, bg="#565cba", font=("Fixedsys", 20)).pack(pady=5)
    
# koniec
# Login Window
login_window = tk.Tk()
login_window.title("Banker Login")
login_window.geometry("400x300")
login_window.config(bg="#E4E2E2")

frame = tk.Frame(login_window, bg="#bcb7d9")
frame.place(x=50, y=50, width=300, height=200)

tk.Label(frame, text="Banker", bg="#E4E2E2", fg="#000", font=("Fixedsys", 24)).pack(pady=10)
loginentry = tk.Entry(frame)
loginentry.pack(pady=5)
pinentry = tk.Entry(frame, show="*")
pinentry.pack(pady=5)
tk.Button(frame, text="Zaloguj", command=start_game).pack(pady=20)
odtworz_muzyke()
login_window.mainloop()

