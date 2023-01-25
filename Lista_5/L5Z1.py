import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from collections import Counter

def sprawdzanie_strony():
    website = wprowadzanie_adresu.get()
    tag = tag_var.get()
    try:
        page = requests.get(website)
        soup = BeautifulSoup(page.content, 'html.parser')
        tag_content = soup.find_all(tag)
        tag_content = [tag.get_text() for tag in tag_content]
        tag_content = " ".join(tag_content)
        slowa = tag_content.split()
        liczenie_slow = Counter(slowa)
        najczestsze = liczenie_slow.most_common(1)
        messagebox.showinfo("Najczęściej występujące słowo", najczestsze[0][0])
    except:
        messagebox.showerror("Błąd", "Nie udało się połączyć z stroną internetową")

root = tk.Tk()
root.title("Sprawdzanie słów na stronie internetowej")

tytul_strony = tk.Label(root, text="Adres strony internetowej:")
tytul_strony.pack()

wprowadzanie_adresu = tk.Entry(root)
wprowadzanie_adresu.pack()

tag_var = tk.StringVar(value='h1')
tag_label = tk.Label(root, text="Wybierz znacznik:")
tag_label.pack()

lista = tk.OptionMenu(root, tag_var, 'h1', 'h2', 'p', 'ol')
lista.pack()

btn = tk.Button(root, text="Sprawdź", command=sprawdzanie_strony)
btn.pack()

root.mainloop()
