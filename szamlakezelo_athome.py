import subprocess # Ezzel lehet külső parancsokat futtatni
from colorama import Fore, Back, Style # Beimportálja a colorama színeit
# GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "01_Számlakezelo\\szamla.txt"
jogosult = False
tranzakciok = []
#######################################
# FUNKCIÓK
#######################################
# Beolvassa a tranzakciókat a fájlból
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global tranzakciok
            tranzakciok = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")
# Elmenti a tranzakciókat a fájlba
def mentes(fajl):
    try:
        with open(fajl, "w", encoding="UTF-8") as f:
            for i in range(len(tranzakciok)):
                f.write(f"{tranzakciok[i].rstrip()}\n")
            
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")
# Kiszámolja és kiírja az aktuális egyenleget
def egyenleg():
    szamla_egyenleg = 0
    
    for sz in tranzakciok:
        szamla_egyenleg += int(sz)
    
    print(f"\nAz egyenleged: {szamla_egyenleg} Ft")
    
    return szamla_egyenleg
# Utalásnál levonja az összeget és a kezelési díjat
def utalas(osszeg):
    print("Utalás: ")
    
    osszeg += round(hasznalati_dij * 0.05)
    
    if osszeg > egyenleg():
        print("\nNem áll rendelkezésre a megfelelő összeg!")
    else:        
        tranzakciok.append(f"-{osszeg}")
    
    egyenleg()
# Hozzáadja a befizetett pénzt a tranzakciókhoz
def penzbetet(osszeg):
    print("Betét: ")
    tranzakciok.append(f"+{osszeg}")
    
    egyenleg()
# Megmutatja az összes vagy az utolsó pár tranzakciót
# darab = 0 esetén az összeset írja ki
def tortenet(darab):
    print("Tranzakciók: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet = len(tranzakciok)-darab
    
    for i in range(kezdet, len(tranzakciok)):
        print(f"\t{tranzakciok[i].rstrip()}")
# Összeadja az összes kiadást
def koltes_osszeg():
    osszeg = 0
    
    for sz in tranzakciok:        
        if int(sz) < 0:
            osszeg += int(sz)
    
    return osszeg
# Összeadja az összes befizetést
def betet_osszeg():
    osszeg = 0
    
    for sz in tranzakciok:        
        if int(sz) > 0:
            osszeg += int(sz)
    
    return osszeg   
# Megkeresi a legnagyobb kiadást
def legnagyobb_kiadas():
    min_ertek = 0
    
    for sz in tranzakciok:
        if int(sz) < min_ertek:
            min_ertek = int(sz)
            
    return min_ertek
#######################################
# A PROGRAM
#######################################
# BEJELENTKEZÉS
# Bekéri a PIN-t, és maximum 3 próbálkozást enged
hibas_belepesszam = 3
pk = int(input("Add meg a PIN kódodat!: "))
if pk == pin_kod:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")
while(not jogosult and hibas_belepesszam > 1):
    print(f"{Fore.RED} Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -= 1
  
    if pk == pin_kod:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")
if not jogosult:
    print(f"{Fore.RED} Hibás PIN kód!")
print(f"{Fore.RESET}", end="")
# Beolvassa a korábbi tranzakciókat
adatbeolvasas(adatfajl)
# FUNKCIÓVÁLASZTÓ MENÜ
# A menü címe
cim = "\nSZÁMLAKEZELŐ PROGRAM\n====================\n"
# A menüpontok
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/átutalás",
    "3. Pénz betét",
    "--------------",
    "4. Tranzakciótörténet",
    "5. Költések összege",
    "6. Betétek összege",
    "7. Legnagyobb kiadás",
    "--------------",
    "9. Kilépés"
]
# Ezeket a menüpontokat lehet kiválasztani
menupontok = [1, 2, 3, 4, 5, 6, 7, 9]
# A menü folyamatosan ismétlődik
while True:
    print(f"{Back.LIGHTCYAN_EX}{cim}")
    print(f"{Back.RESET}", end="")
    
    print(f"{Fore.LIGHTCYAN_EX}", end="")
    
    for me in menu:
        print(f"{me}")
    # Bekéri a választott menüpontot
    valasztas = int(input("Válassz tevékenységet: "))
    # Ha rossz menüpontot adunk meg, újra bekéri
    while valasztas not in menupontok:
        print("Nincs ilyen menüpont!\n")
        
        print(cim)    
        for me in menu:
            print(f"{me}")
        valasztas = int(input("Válassz tevékenységet: "))
    print(f"{Fore.RESET}", end="")
    # A kiválasztott menüpont alapján elindítja a megfelelő funkciót
    if valasztas == 1:
        egyenleg()
    elif valasztas == 2:
        u = int(input("Kivétel vagy utalás összege: "))
        utalas(u)
    elif valasztas == 3:
        b = int(input("Betét összege: "))
        penzbetet(b)
    elif valasztas == 4:
        m = int(input("Előzmény mérete (db) Minden: [0]: "))
        tortenet(m)
    elif valasztas == 5:
        print(f"\nÖsszes költés: {koltes_osszeg()} Ft")
    elif valasztas == 6:
        print(f"\nÖsszes pénzbetét: {betet_osszeg()} Ft")
    elif valasztas == 7:
        print(f"Legnagyobb kiadás: {legnagyobb_kiadas()} Ft")
    # Kilépés előtt elmenti az adatokat
    elif valasztas == 9:
        mentes(adatfajl)
        exit()
    # Megvárja, amíg a felhasználó megnyom egy billentyűt
    # Utána letörli a konzol tartalmát
    input(f"Üss egy billentyűt a folytatáshoz...")
    subprocess.run(["cls"], shell=True)
