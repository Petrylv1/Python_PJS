import tkinter as tk


def button_clicked(button):
    global player
    if button["text"] == " ":
        button["text"] = player
        check_for_winner()
        switch_player()


def check_for_winner():
    global winner
    for i in range(board_size):
        if all(buttons[i][j]["text"] == player for j in range(board_size)):
            winner = player
            end_game()
        if all(buttons[j][i]["text"] == player for j in range(board_size)):
            winner = player
            end_game()
    if all(buttons[i][i]["text"] == player for i in range(board_size)):
        winner = player
        end_game()
    if all(buttons[i][board_size - i - 1]["text"] == player for i in range(board_size)):
        winner = player
        end_game()
    if board_size > 3:
        for i in range(board_size):
            for j in range(board_size):
                if buttons[i][j]["text"] == player:
                    if (
                        check_for_2_diagonals(i, j)
                        or check_for_2_rows(i, j)
                        or check_for_2_columns(i, j)
                    ):
                        winner = player
                        end_game()


def check_for_2_diagonals(i, j):
    if i == j:
        diagonal = [buttons[x][x]["text"] for x in range(board_size)]
    elif i + j == board_size - 1:
        diagonal = [buttons[x][board_size - x - 1]["text"] for x in range(board_size)]
    else:
        return False
    if diagonal.count(player) == board_size - 2:
        return True
        return False


def check_for_2_rows(i, j):
    row = [buttons[i][x]["text"] for x in range(board_size)]
    if row.count(player) == board_size - 2:
        return True
    return False


def check_for_2_columns(i, j):
    column = [buttons[x][j]["text"] for x in range(board_size)]
    if column.count(player) == board_size - 2:
        return True
    return False


def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"
        player_label["text"] = f"Gracz: {player}"


def end_game():
    for i in range(board_size):
        for j in range(board_size):
            buttons[i][j]["state"] = "disabled"
    winner_label = tk.Label(root, text=f"Wygrał gracz {winner}!")
    winner_label.grid(row=board_size, column=0, columnspan=board_size, pady=10)


def get_board_size():
    global board_size


board_size = int(size_entry.get())
create_board()


def create_board():
    global buttons
buttons = []
for i in range(board_size):
    button_row = []
for j in range(board_size):
    button = tk.Button(root, text=" ", width=15, height=5)
button.grid(row=i, column=j)
button_row.append(button)
button.config(command=lambda b=button: button_clicked(b))
buttons.append(button_row)

root = tk.Tk()
root.title("Kółko i krzyżyk")

size_label = tk.Label(root, text="Rozmiar planszy:")
size_label.grid(row=0, column=0, padx=10, pady=10)
size_entry = tk.Entry(root)
size_entry.grid(row=0, column=1, padx=10, pady=10)
size_button = tk.Button(root, text="Ustaw", command=get_board_size)
size_button.grid(row=0, column=2, padx=10, pady=10)

player = "X"
player_label = tk.Label(root, text=f"Gracz: {player}")
player_label.grid(row=1, column=0, columnspan=board_size, pady=10)

winner = None
board_size = 3
create_board()
root.mainloop()
