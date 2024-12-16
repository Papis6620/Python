import tkinter as tk
import random

def play(user_choice):
    choices = {0: "Papier", 1: "Kamień", 2: "Nożyce"}
    computer_choice = random.randint(0, 2)
    user_label.config(text=f"Twój wybór: {choices[user_choice]}")
    computer_label.config(text = f"Wybór komputera: {choices[computer_choice]}")

    if user_choice == computer_choice:
        result = "Remis"
    elif (user_choice == 0 and computer_choice == 1) or \
        (user_choice == 1 and computer_choice == 2) or \
            (user_choice == 2 and computer_choice == 0):
        result = "Wygrałeś"
    else:
        result = "Przegrałeś"

    result_label.config(text=result)

root = tk.Tk()
root.title("Papier Kamień Nożyce")

title_label = tk.Label(root, text="Wybierz Papier, Kamień lub Nożyce", font=("Arial", 16))
user_label = tk.Label(root, text="Twój wybór: ", font=("Arial", 14))
computer_label = tk.Label(root, text="Twój komputera: ", font=("Arial", 14))
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))

title_label.pack(pady=10)
user_label.pack()
computer_label.pack()
result_label.pack(pady=20)

tk.Button(root, text="Papier", font=("Arial, 14"), command=lambda: play(0)).pack(side=tk.LEFT, padx = 20, pady=10)
tk.Button(root, text="Kamień", font=("Arial, 14"), command=lambda: play(1)).pack(side=tk.LEFT, padx = 20, pady=10)
tk.Button(root, text="Nożyce", font=("Arial, 14"), command=lambda: play(2)).pack(side=tk.LEFT, padx = 20, pady=10)

root.mainloop()