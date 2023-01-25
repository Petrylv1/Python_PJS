import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urljoin

def sprawdzanie_strony():
    website = wprowadzanie_adresu.get()
    tag = tag_var.get()
    try:
        page = requests.get(website)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all('a')
        links = [urljoin(website, link.get('href')) for link in links]
        for link in links:
            try:
                link_page = requests.get(link)
                link_soup = BeautifulSoup(link_page.content, 'html.parser')
                tag_content = link_soup.find_all(tag)
                tag_content = [tag.get_text() for tag in tag_content]
                tag_content = " ".join(tag_content)
                slowa = tag_content.split()
                liczenie_slow = Counter(slowa)
                najczestsze = liczenie_slow.most_common(2)
                messagebox.showinfo("Najczęściej występujące słowo", f"1. {najczestsze[0][0]}\n2. {najczestsze[1][0]}")
            except:
                messagebox.showerror("Błąd", "Nie udało się połączyć z podstroną")
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
