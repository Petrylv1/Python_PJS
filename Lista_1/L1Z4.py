print("Lista 1 zad 4")
print("================")
print("Ciągi znaków")
print("=================")

sentence = input("Podaj zdanie: ")

print("Liczba wszystkich liter: ", len(sentence))

print("Liczba liter bez spacji: ", len(sentence.replace(" ", "")))
exclude_char = input("Podaj znak do pominięcia: ")
print("Liczba liter bez podanego znaku: ", len(sentence.replace(exclude_char, "")))

print("Wyrazy w zdaniu: ", sentence.split())

split_char = input("Podaj znak do podziału zdania: ")
sentence_parts = sentence.split(split_char)
print("Części zdania po podziale: ", sentence_parts)