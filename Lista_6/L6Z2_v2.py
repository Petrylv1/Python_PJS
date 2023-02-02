from tkinter import *
from tkinter import ttk
import ttkthemes
import sqlite3
import tkinter.messagebox as messagebox

# Tworzenie bazy danych i tabeli studenci
# oknoGlowne = Tk()
# dbPolaczenie = sqlite3.connect('dziekanat.db')
# dbKursor = dbPolaczenie.cursor()
# sqlQuery = "CREATE TABLE studenci (imie text, nazwisko text, adres text, pesel text, album integer)"
# dbKursor.execute(sqlQuery)
# dbPolaczenie.commit()
# dbPolaczenie.close()

# oknoGlowne.mainloop()

# oknoGlowne = Tk()
# dbPolaczenie = sqlite3.connect('dziekanat.db')
# dbKursor = dbPolaczenie.cursor()
# sqlQuery = "CREATE TABLE oceny (przedmiot text, ocena integer, idStudenta integer)"
# dbKursor.execute(sqlQuery)
# dbPolaczenie.commit()
# dbPolaczenie.close()

# oknoGlowne.mainloop()

def showRekordy():
    siatkaDanych.delete(*siatkaDanych.get_children())
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute("select oid,* from studenci")
    wynikZapytania = dbKursor.fetchall()
    for wierszDanych in wynikZapytania:
        siatkaDanych.insert('', END, values=wierszDanych)
    dbPolaczenie.commit()
    dbPolaczenie.close()


def wyborWiersza():
    for selected_item in siatkaDanych.selection():
        wybranyWiersz = siatkaDanych.item(selected_item)
        wybraneWartosci = wybranyWiersz['values']
        zrobOknoEdycji(wybraneWartosci)
        break


def wyborWierszaKrotkaOcena(dane, siatkaDanychOcen):
    zrobOknoEdycjiOcen(dane, siatkaDanychOcen)


def wyborWierszaKrotka(dane):
    zrobOknoEdycji(dane)


def aktualizujOcene(dane, siatkaDanychOcen):
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute(f"update oceny set przedmiot=:pprzedmiot, ocena=:pocena where oid=:pid", {
        'pprzedmiot': dane[1],
        'pocena': dane[2],
        'pid': dane[0]
    })

    dbPolaczenie.commit()
    dbPolaczenie.close()
    showRekordyOcen(siatkaDanychOcen, dane[3])


def zrobOknoEdycjiOcen(wartosci, siatkaDanychOcen):
    noweOkno = Toplevel()
    noweOkno.grab_set()
    noweOkno.title("Edycja")
    noweOkno.config(bg='grey')

    labelPrzedmiot = Label(noweOkno, text="Przedmiot: ").grid(row=0, column=0)
    przedmiotEntry = Entry(noweOkno, width=30)
    przedmiotEntry.insert(0, wartosci[1])
    przedmiotEntry.grid(row=0, column=1)

    labelOcena = Label(noweOkno, text="Ocena: ", width=15).grid(row=1, column=0)
    ocenaEntry = Entry(noweOkno, width=30)
    ocenaEntry.insert(0, wartosci[2])
    ocenaEntry.grid(row=1, column=1)

    def zrob():
        dane = (wartosci[0], przedmiotEntry.get(), ocenaEntry.get(), wartosci[3])
        aktualizujOcene(dane, siatkaDanychOcen)
        noweOkno.destroy()

    updateGuzik = Button(noweOkno, text="Aktualizuj", font=('Verdana', 8,), command=lambda: zrob())
    updateGuzik.grid(row=1, column=0, columnspan=1)


def showRekordyOcen(siatkaDanychOcen, id):
    siatkaDanychOcen.delete(*siatkaDanychOcen.get_children())
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute("select oid,* from oceny where idstudenta=:pidstud", {
        'pidstud': id
    })
    wynikZapytania = dbKursor.fetchall()
    for wierszDanych in wynikZapytania:
        siatkaDanychOcen.insert('', END, values=wierszDanych)
    dbPolaczenie.commit()
    dbPolaczenie.close()


def wyborWierszaOcen(event):
    for selected_item in event.widget.selection():
        wybranyWiersz = event.widget.item(selected_item)
        wybraneWartosci = wybranyWiersz['values']
        zrobOknoEdycjiOcen(wybraneWartosci, event.widget)
        break


def zrobOknoOcen(id):
    noweOkno = Toplevel()
    noweOkno.grab_set()
    noweOkno.title("Oceny")
    noweOkno.config(border=1, bg='grey')

    kolumny = ('koid', 'kprzedmiot', 'kocena')

    siatkaDanychOcen = ttk.Treeview(noweOkno, columns=kolumny, show='headings', height=8)
    siatkaDanychOcen.column('koid', minwidth=8, width=30)
    siatkaDanychOcen.column('kprzedmiot', minwidth=8, width=120)
    siatkaDanychOcen.column('kocena', minwidth=8, width=70)

    siatkaDanychOcen.heading('koid', text='ID')
    siatkaDanychOcen.heading('kprzedmiot', text='Przedmiot')
    siatkaDanychOcen.heading('kocena', text='Ocena')

    showRekordyOcen(siatkaDanychOcen, id)

    siatkaDanychOcen.bind('<<TreeviewSelect>>', wyborWierszaOcen)

    siatkaDanychOcen.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(noweOkno, orient=VERTICAL, command=siatkaDanychOcen.yview)
    siatkaDanychOcen.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky='ns')

    def dodajTemp():
        dodajOcene(id)

        dbPolaczenie = sqlite3.connect('dziekanat.db')
        dbKursor = dbPolaczenie.cursor()
        dbKursor.execute("SELECT oid, * FROM oceny WHERE rowid = (SELECT max(rowid) FROM oceny);")
        wynik = dbKursor.fetchall()[0]
        dbPolaczenie.commit()
        dbPolaczenie.close()
        wyborWierszaKrotkaOcena(wynik, siatkaDanychOcen)

    def showSR(siatkaDanychOcen, id):
        siatkaDanychOcen.delete(*siatkaDanychOcen.get_children())
        dbPolaczenie = sqlite3.connect('dziekanat.db')
        dbKursor = dbPolaczenie.cursor()
        dbKursor.execute("select przedmiot, AVG(ocena) from oceny where idstudenta=:pidstud GROUP BY przedmiot", {
            'pidstud': id
        })
        wynikZapytania = dbKursor.fetchall()
        for wierszDanych in wynikZapytania:
            siatkaDanychOcen.insert('', END, values=wierszDanych)
        dbPolaczenie.commit()
        dbPolaczenie.close()

    def showSrednia():
        noweOkno = Toplevel()
        noweOkno.grab_set()
        noweOkno.title("Srednia")
        noweOkno.config(border=1, bg='grey')

        kolumny = ('kprzedmiot', 'ksrednia')

        siatkaDanychOcen = ttk.Treeview(noweOkno, columns=kolumny, show='headings', height=8)
        siatkaDanychOcen.column('kprzedmiot', minwidth=8, width=170)
        siatkaDanychOcen.column('ksrednia', minwidth=8, width=170)

        siatkaDanychOcen.heading('kprzedmiot', text='Przedmiot')
        siatkaDanychOcen.heading('ksrednia', text='Średnia')

        showSR(siatkaDanychOcen, id)

        siatkaDanychOcen.bind('<<TreeviewSelect>>', wyborWierszaOcen)

        siatkaDanychOcen.grid(row=0, column=0, sticky='nsew')
        scrollbar = ttk.Scrollbar(noweOkno, orient=VERTICAL, command=siatkaDanychOcen.yview)
        siatkaDanychOcen.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=2, sticky='ns')

    dodajGuzik = Button(noweOkno, text="Dodaj", command=dodajTemp, width=20, font=('Verdana', 15,))
    dodajGuzik.grid(row=1, column=0)
    sredniaGuzik = Button(noweOkno, text="Pokaż średnią", command=showSrednia, width=20, font=('Verdana', 15,))
    sredniaGuzik.grid(row=2, column=0)


def zrobOknoEdycji(wartosci):
    noweOkno = Toplevel()
    noweOkno.grab_set()
    noweOkno.title("Edycja")
    noweOkno.config(border=1, bg='grey')

    labelImie = Label(noweOkno, text="Imię: ", width=25, font=('Verdana', 8,)).grid(row=0, column=0)
    imieEntry = Entry(noweOkno, width=30)
    imieEntry.insert(0, wartosci[1])
    imieEntry.grid(row=0, column=1)

    labelNazwisko = Label(noweOkno, text="Nazwisko: ", width=25, font=('Verdana', 8,)).grid(row=1, column=0)
    nazwiskoEntry = Entry(noweOkno, width=30)
    nazwiskoEntry.insert(0, wartosci[2])
    nazwiskoEntry.grid(row=1, column=1)

    labelAdres = Label(noweOkno, text="Adres: ", width=25, font=('Verdana', 8,)).grid(row=2, column=0)
    adresEntry = Entry(noweOkno, width=30)
    adresEntry.insert(0, wartosci[3])
    adresEntry.grid(row=2, column=1)

    labelPesel = Label(noweOkno, text="PESEL: ", width=25, font=('Verdana', 8,)).grid(row=3, column=0)
    peselEntry = Entry(noweOkno, width=30)
    peselEntry.insert(0, wartosci[4])
    peselEntry.grid(row=3, column=1)

    labelAlbum = Label(noweOkno, text="Album: ", width=25, font=('Verdana', 8,)).grid(row=4, column=0)
    albumEntry = Entry(noweOkno, width=30)
    albumEntry.insert(0, wartosci[5])
    albumEntry.grid(row=4, column=1)

    def zrob():
        dane = (wartosci[0], imieEntry.get(), nazwiskoEntry.get(), adresEntry.get(), peselEntry.get(), albumEntry.get())
        aktualizujOsobe(dane)
        noweOkno.destroy()
    updateGuzik = Button(noweOkno,width=25, text="Aktualizuj", font=('Verdana', 8,), command=lambda: zrob())
    updateGuzik.grid(row=6, column=1)

    def oce():
        zrobOknoOcen(wartosci[0])
        noweOkno.destroy()
    ocenyGuzik = Button(noweOkno, width=25, text="Dodaj", font=('Verdana', 8,), command=lambda: zrob())
    ocenyGuzik.grid(row=6, column=0)
    ocenyGuzik = Button(noweOkno,width=25, text="Oceny", font=('Verdana', 8,), command=lambda: oce())
    ocenyGuzik.grid(row=6, column=1)


def aktualizujOsobe(dane):
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute(
        f"update studenci set imie=:pimie, nazwisko=:pnazwisko, adres=:padres, pesel=:ppesel, album=:palbum where oid=:pid",
        {
            'pimie': dane[1],
            'pnazwisko': dane[2],
            'padres': dane[3],
            'ppesel': dane[4],
            'palbum': dane[5],
            'pid': dane[0]
        })

    dbPolaczenie.commit()
    dbPolaczenie.close()
    showRekordy()


def dodajOcene(id):
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute("Insert into oceny values (:p_przedmiot, :p_ocena, :p_idStudenta)",
                     {
                         'p_przedmiot': "Default",
                         'p_ocena': "Default",
                         'p_idStudenta': id
                     })
    dbPolaczenie.commit()
    dbPolaczenie.close()


def dodajStudenta():
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute("Insert into studenci values (:p_imie, :p_nazwisko, :p_adres, :p_pesel, :p_album)",
                     {
                         'p_imie': "Default",
                         'p_nazwisko': "Default",
                         'p_adres': "Default",
                         'p_pesel': "Default",
                         'p_album': 0
                     })
    dbPolaczenie.commit()
    dbPolaczenie.close()


root = Tk()
root.title("Baza Studentów")
root.config(bg='grey')

kolumny = ('koid', 'kimie', 'knazw', 'kadres', 'kpesel', 'kalbum')

siatkaDanych = ttk.Treeview(root, columns=kolumny, show='headings', height=8)
style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 12,))
siatkaDanych.column('koid', minwidth=8, width=80, anchor='center' )
siatkaDanych.column('kimie', minwidth=8, width=80, anchor='center')
siatkaDanych.column('knazw', minwidth=8, width=80, anchor='center')
siatkaDanych.column('kadres', minwidth=8, width=80, anchor='center')
siatkaDanych.column('kpesel', minwidth=8, width=80, anchor='center')
siatkaDanych.column('kalbum', minwidth=8, width=80, anchor='center')

siatkaDanych.heading('koid', text='ID')
siatkaDanych.heading('kimie', text='Imię')
siatkaDanych.heading('knazw', text='Nazwisko')
siatkaDanych.heading('kadres', text='Adres')
siatkaDanych.heading('kpesel', text='PESEL')
siatkaDanych.heading('kalbum', text='Album')
showRekordy()



siatkaDanych.grid(row=0, column=0, sticky='nsew', columnspan="3")
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=siatkaDanych.yview)
siatkaDanych.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=3, sticky='ns')


def dodajTemp():
    dodajStudenta()
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute("SELECT oid, * FROM studenci WHERE rowid = (SELECT max(rowid) FROM studenci);")
    wynik = dbKursor.fetchall()[0]
    dbPolaczenie.commit()
    dbPolaczenie.close()
    wyborWierszaKrotka(wynik)


def usunAll():
    dbPolaczenie = sqlite3.connect('dziekanat.db')
    dbKursor = dbPolaczenie.cursor()
    dbKursor.execute("DELETE FROM studenci;")
    dbPolaczenie.commit()
    dbPolaczenie.close()

    showRekordy()

dodajGuzik = Button(root, text="Dodaj Studenta", command=dodajTemp, width=20, font=('Verdana', 15,),)
dodajGuzik.grid(row=1, column=0)

czyscGuzik = Button(root, text="Usuń Studentów", command=usunAll, width=20, font=('Verdana', 15,))
czyscGuzik.grid(row=1, column=1)

czyscGuzik = Button(root, text="Edytuj Studentów", command=wyborWiersza, width=20, font=('Verdana', 15,))
czyscGuzik.grid(row=1, column=2)

root.mainloop()