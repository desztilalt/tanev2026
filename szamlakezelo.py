# GLOBÁLIS VÁLTOZÓK


pin_kod = 1414
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "szamla.txt"
jogosult = False
tranzakciok=[]


############################
# FUNKCIÓK
############################


def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global tranzakciok
            tranzakciok = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")
        
        
def mentes(fajl):
    try:
        with open(fajl, "w", encoding="UTF-8") as f:
            f.writelines(tranzakciok)
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")
        

def egyenleg():
    szamla_egyenleg=0
    
    for sz in tranzakciok:
        szamla_egyenleg += int(sz)
        
    print(f"Az egyenleged: {szamla_egyenleg} Ft")


def utalas(osszeg):
    print("Utalás: ")
    
    osszeg += round(hasznalati_dij * 0.05)
    
    if osszeg>egyenleg():
        print("Nem áll rendelkezésre elegendő fedezet!")
    else:
        tranzakciok.append(f"-{osszeg}")

    egyenleg()

def penzbetetel(osszeg):
    print("Betétel: ") 
    tranzakciok.append(f"+{osszeg}")

    egyenleg()
    
    
# darab = 0 -> összes tranzakció
# darab = !=0 -> utolsó tranzakció


def tortenet(darab):
    print("Tranzakciók: ")
    
    if darab==0:
        kezdet=0
    else:
        kezdet=len(tranzakciok)-darab
    
    for i in range(kezdet, len(tranzakciok)):
        print(f"\t{tranzakciok[i].rstrip()}")


############################
# FUNKCIÓK VÉGE
############################


# MŰKÖDÉS
# BELÉPÉS


hibas_belepesszam = 3


pk = int(input("Add meg a PIN kódodat!: "))

if pk == pin_kod:
    jogosult = True
    print("Sikeres belépés!")

while (not jogosult and hibas_belepesszam > 1):
    print (f"Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -= 1
    
    if pk == pin_kod:
        jogosult = True
        print("Sikeres belépés!")

if not jogosult:
    print(f"Hibás pin kód!")

adatbeolvasas(adatfajl)


# FUNKCIÓVÁLASZTÓ MENÜ


cim="\nSZÁMLAKEZELŐ PROGRAM\n==========================\n"
menu=[
    "1. Egyenleg lekérdezése",
    "2. Pénz kivétel/utalás",
    "3. Pénz betétel",
    "-----------------------",
    "4. Tranzakciótörténet",
    "9. Kilépés"
]


menupontok=[1, 2, 3, 4, 9]

while True:
    print(cim)
    for me in menu:
        print(f"{me}")

    valasztas=int(input("Válassz tevékenységet: "))

    while valasztas not in menupontok:
        print("Nincs ilyen menüpont!\n")

        print(cim)
        for me in menu:
            print(f"{me}")


    #KÉPERNYŐ TÖRLÉSE
    
    
    print(f"{'\n'*20}")
    

    if valasztas == 1:
        egyenleg()
        
    elif valasztas == 2:
        u=int(input("Kivétel vagy utalás összege: "))
        utalas(u)

    elif valasztas == 3:
        b=int(input("Betétel összege: "))
        penzbetetel(b)
        
    elif valasztas == 4:
        m=int(input("Előzmény mérete (db) Minden: [0]: "))
        tortenet(m)
        
    elif valasztas == 9:
        mentes(adatfajl)
        exit()


    