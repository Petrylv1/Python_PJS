print("Podaj nieparzysty tekst")
tekst = input()
a = len(tekst)
while a % 2 == 0:
    print("Podałeś parzysty tekst! Podaj ponownie")
    tekst = input()
    a = len(tekst)

for i in range(a * 2):

    for j in range (a * 2 - 1):
        if i + j == a - 1 or j - i == a - 1 or i == a - 1:
            print("*", end="")
        elif i == a - 2 and j == a - 1:
            print(tekst, end="");
        elif i == a - 2 and j > 1 and j < a + 2:
            print("", end="")
        else:
            print(" ", end="")
    print(" ")