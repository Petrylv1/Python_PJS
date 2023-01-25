import tkinter as tk

def button_clicked(button):
    global player
    if button["text"] == " ":
        button["text"] = player
        check_for_winner()
        switch_player()

def check_for_winner():
    global winner
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != " ":
            winner = buttons[i][0]["text"]
            end_game()
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != " ":
            winner = buttons[0][i]["text"]
            end_game()
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        winner = buttons[0][0]["text"]
        end_game()
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        winner = buttons[0][2]["text"]
        end_game()

def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"
    player_label["text"] = f"Gracz: {player}"
    
def show_winner():
    winner_window = tk.Toplevel(root)
    winner_window.title("Wynik")
    winner_label = tk.Label(winner_window, text=f"Wygrał gracz {winner}!", font=('Arial 14 bold'))
    winner_label.pack()
    ok_button = tk.Button(winner_window, text="OK", command=winner_window.destroy)
    ok_button.pack()

def end_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["state"] = "disabled"
    show_winner()

#tworzenie okna gry
root = tk.Tk()
root.title("Kółko i krzyżyk")

#tworzenie tablicy przycisków
buttons = []
for i in range(3):
    button_row = []
    for j in range(3):
        button = tk.Button(root, text=" ", width=15, height=5, font=('Arial 14 bold'))
        button.grid(row=i, column=j)
        button_row.append(button)
        button.config(command=lambda b=button: button_clicked(b))
    buttons.append(button_row)       
player = "X"
player_label = tk.Label(root, text=f"Gracz: {player}",font=('Arial 14 bold'))
player_label.grid(row=3, column=0, columnspan=3, pady=10)

winner=None
root.mainloop()