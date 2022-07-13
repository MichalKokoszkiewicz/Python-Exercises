oceny = {}

def srednia_uczen(imie, oceny):
    if imie not in oceny:
        print("Uczeń", imie, "nie ma ocen")
    else:
        suma = 0
        for ocena in oceny[imie]:
            suma += ocena
        srednia = suma / len(oceny[imie])
        print("Średnia dla ucznia", imie, "to:", srednia)

def srednia_uczniow(oceny):
    for imie in oceny.keys():
        srednia_uczen(imie, oceny)

def srednia(oceny):
    suma = 0
    ilosc_ocen = 0
    for imie in oceny.keys():
        for ocena in oceny[imie]:
            suma += ocena
            ilosc_ocen += 1
    srednia = suma / ilosc_ocen
    print("Średnia ocen wszystkich uczniów to:", srednia)

while True:
    imie = input("Podaj imię studenta: ")
    if imie.lower() == 'x':
        print("Czas na statystyki!")
        break
    ocena = float(input("Podaj ocenę: "))

    if imie in oceny:
        oceny[imie].append(ocena)
    else:
        oceny[imie] = [ocena]

srednia(oceny)
srednia_uczniow(oceny)
srednia_uczen("Zbigniew", oceny)
