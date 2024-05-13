import tkinter as tk
from tkinter import messagebox
import random

words = [
    ("apple", "A fruit that is commonly red or green."),
    ("banana", "A yellow fruit that grows on trees."),
    ("orange", "A citrus fruit that is commonly orange in color."),
    ("grapes", "Small, round fruit that grows in clusters."),
    ("strawberry", "A red fruit with seeds on the outside."),
    ("watermelon", "A large fruit with green skin and red flesh."),
    ("pineapple", "A tropical fruit with a spiky outer skin."),
    ("mango", "A sweet and juicy tropical fruit."),
    ("kiwi", "A small, brown fruit with green flesh."),
    ("peach", "A fuzzy fruit with a juicy, sweet taste.")
]

word_to_guess, hint = random.choice(words)

guessed_letters = []
attempts = 6

window = tk.Tk()
window.title("Hangman")
window.configure(bg="#ADD8E6")

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

hint_label = tk.Label(window, text=f"HINT: {hint}", font=("Consolas", 10), bg="#FFB6C1", fg="black")
hint_label.pack(pady=5)


def is_game_over():
    return check_win() or check_loss()


def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)


def check_loss():
    return attempts == 0


def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            messagebox.showinfo("Hangman", f"You've already guessed '{letter}'")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo("Hangman", "Congratulations! You win!⭐")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Hangman", "You lose! The word was: " + word_to_guess)
                reset_game()
        letter_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Hangman", "Please enter a single letter.")


def reset_game():
    global word_to_guess, hint, guessed_letters, attempts
    word_to_guess, hint = random.choice(words)
    guessed_letters = []
    attempts = 6
    hint_label.config(text=f"HINT: {hint}")
    update_word_display()
    update_attempts_display()
    draw_hangman()


def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
        display_word += " "
    word_label.config(text=display_word)


def update_attempts_display():
    attempts_label.config(text=f"Attempts left: {attempts}")


def draw_hangman():
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(125, 125, 175, 175, width=4, fill="#FFFF99", tags="hangman")
    if attempts < 5:
        canvas.create_line(150, 175, 150, 225, width=4, tags="hangman")
    if attempts < 4:
        canvas.create_line(150, 200, 125, 175, width=4, tags="hangman")
    if attempts < 3:
        canvas.create_line(150, 200, 175, 175, width=4, tags="hangman")
    if attempts < 2:
        canvas.create_line(150, 225, 125, 250, width=4, tags="hangman")
    if attempts < 1:
        canvas.create_line(150, 225, 175, 250, width=4, tags="hangman")


def on_enter_press(event):
    guess_letter()


button_frame = tk.Frame(window, bg="#ADD8E6")

word_label = tk.Label(window, text="", font=("Consolas", 24), bg="#ADD8E6")
attempts_label = tk.Label(window, text="", font=("Consolas", 16), bg="#ADD8E6")
letter_entry = tk.Entry(window, width=10, font=("Consolas", 16))
guess_button = tk.Button(button_frame, text="GUESS", command=guess_letter, font=("Consolas", 16), bg="#FFFF99")
reset_button = tk.Button(button_frame, text="RESET", command=reset_game, font=("Consolas", 16), bg="#FF9999")
letter_entry.bind('<Return>', on_enter_press)

canvas = tk.Canvas(window, width=300, height=300, bg="#ADD8E6")
canvas.create_line(50, 270, 250, 270, width=4)
canvas.create_line(200, 270, 200, 100, width=4)
canvas.create_line(100, 100, 200, 100, width=4)
canvas.create_line(150, 100, 150, 120, width=4)
canvas.pack()

word_label.pack()
attempts_label.pack()
letter_entry.pack()

button_frame.pack(pady=10)
guess_button.pack(side=tk.LEFT, padx=(0, 5))
reset_button.pack(side=tk.LEFT)

update_word_display()
update_attempts_display()
draw_hangman()

window.mainloop()
