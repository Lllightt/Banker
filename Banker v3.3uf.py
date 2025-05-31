import tkinter as tk
from tkinter import messagebox
import random

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
zloto = random.randint(1,50948)
posiadane_zloto = 0
srebro = random.randint(1,10000)
posiadane_srebro = 0
diament = random.randint(1,500000)
posiadane_diament = 0
#PODATKI
randPodatek = random.randint(100000,1000000)
Podatek = randPodatek
Podatek_Zaplacony = True
# KODY
codes = [
    "IoG",
    "BankerGUI",
    "Banker3.0"
]

def start_game():
    login = loginentry.get()
    try:
        pin = int(pinentry.get())
    except ValueError:
        messagebox.showerror("Błąd", "PIN musi być liczbą.")
        return

    if login == PrawLogin and pin == PrawPin:
        login_window.destroy()
        open_main_menu()
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
        czas += 1
        zarobek = Pensja * (LVL * 2 if LVL > 0 else 1)
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
            else:
                messagebox.showerror("✘ Błąd", "✘ Za mało pieniędzy.")

        tk.Button(edu, bg="#68a840", font=("PT Sans", 24), text="Harvard (250k, +15 LVL)", command=lambda: kup(250000, 15, "Harvard")).pack(pady=5)
        tk.Button(edu,  bg="#68a840", font=("PT Sans", 24), text="Stanford (15k, +10 LVL)", command=lambda: kup(15000, 10, "Stanford")).pack(pady=5)
        tk.Button(edu,  bg="#68a840", font=("PT Sans", 24),text="Batory (5k, +5 LVL)", command=lambda: kup(5000, 5, "Batory")).pack(pady=5)
        tk.Button(edu,  bg="#68a840", font=("PT Sans", 24), text="Zagle (500, +1 LVL)", command=lambda: kup(500, 1, "Zagle")).pack(pady=5)
#koniec
#bitcoin
    def pokaz_bitcoin():
        global konto
        if LVL < 30:
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
            output.config(text="✘ Za mało pieniędzy.")
#koniec
#Strona 2
    def open_page2():
        page2 = tk.Toplevel(game)
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
            global Podatek, Wzrost_Podatki
            Podatki_main = tk.Toplevel(page2)
            Podatki_main.title("Podatki")
            Podatki_main.geometry("400x300")
            Podatki_main.config(bg="#f4b0f5")
            Frame_Podatki = tk.Frame(Podatki_main, bg="#f4b0f5", width=300, height= 200)
            Frame_Podatki.place(width=800,height=700)
            Frame_Podatki.pack(pady=10)
            def sprawdz_podatek():
                global Podatek, Wzrost_Podatki, konto
                messagebox.showerror("INFO:", f"Masz do zapłacenia {Podatek} zł")
            def zaplac_podatek():
                global Podatek, Wzrost_Podatki, konto
                if konto >= Podatki:
                    konto -= Podatki
                    Podatki = 0
                    Wzrost_Podatki = 1
                    Podatek_Zaplacony = True
                else:
                    messagebox.showerror("✘ Błąd", "✘ Za mało pieniędzy.")
            tk.Button(Frame_Podatki, text="Sprawdz Podatki", command=sprawdz_podatek,bg="#b96cba", font=("Fixedsys", 24)).pack(pady=10)
            tk.Button(Frame_Podatki, text="Zapłać Podatki", command=zaplac_podatek,bg="#b96cba", font=("Fixedsys", 24)).pack(pady=10)
        def koniec_gry():
            global Podatek, Podatek_Zaplacony,secretcode
            if Podatek_Zaplacony == True:
                messagebox.showinfo(f"Podatki",f"Pokonałeś Grę Wyślij na discord kod: BANKERKONIEC{secretcode}")
        def kupno_mineraly():
            global zloto,srebro,diament,posiadane_diament,posiadane_srebro,posiadane_zloto
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
                kupno_window = tk.Toplevel(main_mineral)
                kupno_window.geometry("400x400")
                kupno_window.config(bg="#f5f542")
                kupno_window.title("KUPNO ZLOTA")
                tk.Label(kupno_window,text=f"Złoto teraz kosztuję: {zloto} zł",fg="Black", font=("Fixedsys", 24), wraplength=500).pack(pady=5)
                tk.Entry(kupno_window).pack(pady=5)
            tk.Button(main_mineral, text="Kup Zloto", command=kupno_zlota,bg="#cf7938", font=("Fixedsys", 24)).pack(pady=5)
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

login_window.mainloop()