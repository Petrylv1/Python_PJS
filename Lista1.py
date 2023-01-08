# Zadanie 1
```python
print("Lista 1 zad 1")
print("==========================================")
print("Kalkulator objętości i pól powierzni brył")
print("==========================================")
print("Proszę wybrać bryłę:")
print("a - Kula")
print("b - Prostopadłościan")
print("c - Stożek")

wybor=str(input("Wybór: "))

if(wybor=='a'):
    print("Wybrałeś kulę")
    r =int(input("Podaj promień: "))
    pp = 4*3.14*(r*r)
    obj = (4/3)*3.14*(r*r*r)
    print(f"Pole: {pp}")
    print(f"Objętość: {obj}")
    
if(wybor=='b'):
    print("Wybrałeś Prostopadłościan")
    aP = int(input("Podaj A: "))
    bP = int(input("Podaj B: "))
    cP = int(input("Podaj C: "))
    pp = (2*aP)*bP+(2*bP)*cP+(2*aP)*cP
    obj = aP*bP*cP
    print(f"Pole: {pp}")
    print(f"Objętość: {obj}")
    
if(wybor=='c'):
    print("Wybrałeś Stożek")
    r=int(input("Podaj R: "))
    h=int(input("Podaj H: "))
    l=int(input("Podaj L: "))
    obj = (3.14*(r*r)*h)/3
    pp = 3.14*r*(r+l)
    print(f"Pole: {pp}")
    print(f"Objętość: {obj}")
    
'''
    Kącik przemyśleń:
    
    f przed cudzysłowiem oznacza, że jest to f-string i pozwala na bezpośrednie wstawianie wartości zmiennych do tekstu.
    Wtedy nie trzeba używać metody format a także konkatenacji łańcuchów znaków.
    
'''
```    
