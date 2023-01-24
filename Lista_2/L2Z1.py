# Moduł z funkcjami
def znajdz_min_max(arr):
    min_value = min(arr)
    max_value = max(arr)
    min_index = arr.index(min_value)
    max_index = arr.index(max_value)
    return min_value, min_index, max_value, max_index

def liczenie_sredniej(arr):
    return sum(arr) / len(arr)

def szukanie_pozycji(arr, value):
    if value in arr:
        return arr.index(value)
    else:
        return -1

# część główna 
arr = []
for i in range(15):
        arr.append(int(input("Podaj liczbę: ")))

min_value, min_index, max_value, max_index = znajdz_min_max(arr)
print("Najmniejsza liczba:", min_value, "o indeksie", min_index)
print("Największa liczba:", max_value, "o indeksie", max_index)

srednia = liczenie_sredniej(arr)
print("Średnia wartość:", srednia)

value = int(input("Podaj liczbę, której pozycję chcesz znaleźć: "))
pozycja = szukanie_pozycji(arr, value)
if pozycja ==-1:
    print("Podana liczba nie znajduje się w tablicy")
else:
    print("Podana liczba znajduje się na pozycji", pozycja)
