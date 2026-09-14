# GLOBÁLIS VÁLTOZÓK


pin_kod = 1414
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "szamla.txt"
jogosult = False


############################
# FUNKCIÓK
############################
def egyenleg():
    print(f"Az egyenleged: ")

def utalas(osszeg):
    print("Utalás: ")

def penzbetetel(osszeg):
    print("Betétel: ") 


# darab = 0 -> összes tranzakció
# darab = !=0 -> utolsó tranzakció


def tortenet(darab):
    print("Tranzakciók: ")

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

print(cim)
for me in menu:
    print(f"{me}")

valasztas=int(input("Válassz tevékenységet: "))

while valasztas not in menupontok:
    print("Nincs ilyen menüpont!\n")

    print(cim)
    for me in menu:
        print(f"{me}")

if valasztas == 1:
    egyenleg()
elif valasztas == 2:
    utalas(123)
elif valasztas == 3:
    penzbetetel(10000)
elif valasztas == 4:
    tortenet(0)
elif valasztas == 9:
    exit()
    
    

    