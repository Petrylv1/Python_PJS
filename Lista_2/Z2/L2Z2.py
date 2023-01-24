import csv
import random

def losowanie_danych(ilosc):
    data = []
    with open('imiona.txt', encoding="utf-8") as f:
        imiona = f.read().splitlines()
    with open('nazwiska.txt', encoding="utf-8") as f:
        nazwiska = f.read().splitlines()
    with open('ulice.txt', encoding="utf-8") as f:
        ulice = f.read().splitlines()
    with open('miasta.txt', encoding="utf-8") as f:
        miasta = f.read().splitlines()
    with open('kraje.txt', encoding="utf-8") as f:
        kraje = f.read().splitlines()
    for i in range(ilosc):
        imie = random.choice(imiona)
        nazwisko = random.choice(nazwiska)
        pesel = ''.join([str(random.randint(0, 9)) for _ in range(11)])
        ulica = random.choice(ulice)
        nr_domu = str(random.randint(1, 50))
        miasto = random.choice(miasta)
        kraj = random.choice(kraje)
        data.append([imie, nazwisko, pesel, ulica, nr_domu, miasto, kraj])
    # zapisanie danych w pliku csv
    with open('losowe_dane.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['imie', 'nazwisko', 'pesel', 'ulica', 'nr_domu', 'miasto', 'kraj'])
        writer.writerows(data)

# wywołanie funkcji z ilością danych podaną przez użytkownika
ilosc = int(input("Podaj ilość danych, które chcesz wygenerować: "))
losowanie_danych(ilosc)
