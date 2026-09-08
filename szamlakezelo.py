#GLOBALIS VALTOZOK
pin_kod=1414
egyenleg=0
hasznalati_dij=1000
adatfajl="szamla.txt"
jogosult=False

hibas_belepesszam=3

pk=int(input("Add meg a PIN kódot: "))

if pk==pin_kod:
    jogosult=True

while(not jogosult and hibas_belepesszam>0):
    print("hibás pin kód")
    pk=int(input("Add meg a PIN kódot: "))
    hibas_belepesszam-=1

    if pk==pin_kod:
        jogosult=True
        print("Sikeres bejelentkezés!")

