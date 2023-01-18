def wprowadzanie_ocen(przedmiot):
    oceny = []
    while True:
        ocena = int(input(f"Podaj ocenę z {przedmiot}(Podaj 0 jeśli chcesz zakończyć dodawanie ocen): "))
        if ocena == 0:
            break
        if ocena >= 2 and ocena <= 5:
            oceny.append(ocena)
        else:
            print("Podałeś złą liczbę!")
    return oceny

def zliczanie_sredniej(oceny):
    if len(oceny) == 0:
        return 0
    return sum(oceny) / len(oceny)

matematyka = []
algorytmy = []
programowanie = []

while True:
    print("| ========================================= |")
    print("| Oceny cząstkowe                           |")
    print("| ==========================================|")
    print("| Wybierz przedmiot aby dodać z niego oceny |")
    print("| 1. Matematyka                             |")
    print("| 2. Algorytmy                              |")
    print("| 3. Programowanie                          |")
    print("| 4. Policz średnią                         |")
    print("| ==========================================| ")

    wybor = input()

    if wybor == '1':
        matematyka = wprowadzanie_ocen("matematyki")
    elif wybor == '2':
        algorytmy = wprowadzanie_ocen("algorytmów")
    elif wybor == '3':
        programowanie = wprowadzanie_ocen("programowania")
    elif wybor == '4':
        break
    
print("| ========================================= |")
print("| Liczenie średniej:                        |")
print("| ========================================= |")
print("| 1.Wszystkich przedmiotów                  |")
print("| 2.Matematyki                              |")
print("| 3.Algorytmów                              |")
print("| 4.Programowania                           |")
print("| 5.Zestawienie ocen                        | ")
print("| ==========================================| ")

wybor = input()

if wybor == '1':
    wszystkie_oceny = matematyka + algorytmy + programowanie
    srednia = zliczanie_sredniej(wszystkie_oceny)
    print(f"Twoja średnia ocen z wszystkich przedmiotów: {srednia}")
elif wybor == '2':
    srednia = zliczanie_sredniej(matematyka)
    print(f"Twoja średnia ocen z matematyki: {srednia}")
elif wybor == '3':
    srednia = zliczanie_sredniej(algorytmy)
    print(f"Twoja średnia ocen z algorytmów: {srednia}")
elif wybor == '4':
    srednia = zliczanie_sredniej(programowanie)
    print(f"Twoja średnia ocen z programowania: {srednia}")
elif wybor == '5':
    srednia1 = zliczanie_sredniej(matematyka)
    srednia2 = zliczanie_sredniej(algorytmy)
    srednia3 = zliczanie_sredniej(programowanie)
    print(f"Twoja średnia ocen z matematyki: {srednia1}")
    print(f"Twoja średnia ocen z algorytmów: {srednia2}")
    print(f"Twoja średnia ocen z programowania: {srednia3}")
    