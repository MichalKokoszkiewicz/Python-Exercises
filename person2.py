from person import *

lista = [
    Person("Jan", "Nowak", 22, "Męzczyzna"),
    Person("Marek", "Wrona", 32, "Męzczyzna"),
    Person("Marian", "Ptak", 17, "Męzczyzna"),
    Person("Joanna", "Wiśniewska", 25, "Kobieta"),
    Student("Anna", "Wróbel", 18, "Kobieta", [4, 5, 3, 4, 5]),
    Student("Michał", "Kowalczyk", 19, "Męzczyzna", [4, 3, 3, 4, 5]),
    Student("Halina", "Wójcik", 21, "Kobieta", [4, 3, 5, 4, 5]),
    Employee("Zbigniew", "Kowalski", 44, "Męzczyzna", 5432),
    Employee("Piotr", "Zieliński", 53, "Męzczyzna", 8888),
    Employee("Maria", "Kamińska", 28, "Kobieta", 123456),
]

#fn = lambda p: p.sex == "Męzczyzna"
#filter(fn, lista)

#only_name = lambda p: p.name + " " + p.lastname
#map_name_lastname = map(only_name, lista)
#list_name_lastname = list(map_name_lastname)
#print(list_name_lastname)
#print()

for i in filter(lambda p: p.sex == "Męzczyzna", lista):
    print(i)
print()

studenci = list(filter(lambda p : isinstance(p, Student), lista))
suma = 0
for s in studenci:
    suma += s.avg()
print("srednia studentow: ", round(suma / len(studenci), 2))
print()

pracownicy = list(filter(lambda p : isinstance(p, Employee), lista))
suma = 0
for e in pracownicy:
    suma += e.salary
print("srednia zarobki pracownikow: ", round(suma / len(pracownicy), 2))
